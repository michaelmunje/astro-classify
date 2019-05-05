from keras.models import Sequential
from keras_preprocessing.image import ImageDataGenerator as IDG
from keras.layers import Dense, Flatten, Dropout
from keras.layers import Conv2D, MaxPooling2D
from keras.applications import inception_v3
from keras.optimizers import Adam, SGD
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.models import model_from_json, load_model
import pandas as pd


def construct_transfer_model():

    base_model = inception_v3.InceptionV3(include_top=False, weights='imagenet', pooling='avg', input_shape=[200, 200, 3])

    model = Sequential([
        base_model,
        Dense(1024, activation='relu'),
        Dropout(0.5),
        Dense(512, activation='relu'),
        Dense(3, activation='softmax')
    ])

    model.compile(loss='categorical_crossentropy',
                  optimizer=Adam(lr=0.000001),
                  metrics=['accuracy'])

    return model


def construct_model():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=[200, 200, 3]),
        Conv2D(32, (3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Dropout(0.25),
        Conv2D(64, (3, 3), activation='relu'),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Dropout(0.25),
        Flatten(),
        Dense(512, activation='relu'),
        Dropout(0.5),
        Dense(3, activation='softmax')
    ])

    model.compile(loss='categorical_crossentropy',
                  optimizer='Adam',
                  metrics=['accuracy'])

    return model


def train_model(model_paths, transfer=False):

    print("SETTING UP TRAINING...")

    train_df = pd.read_csv(model_paths.augmented_train_solutions)
    valid_df = pd.read_csv(model_paths.valid_solutions)
    # test_df = pd.read_csv(model_paths.test_solutions)

    df_headers = list(train_df.columns)

    train_datagen = IDG(rescale=1. / 255., shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
    valid_datagen = IDG(rescale=1. / 255.)
    # test_datagen = IDG(rescale=1. / 255.)

    # Create generators
    train_generator = train_datagen.flow_from_dataframe(
        dataframe=train_df,
        directory=model_paths.train_image_path,
        x_col=df_headers[0],
        y_col=df_headers[1],
        class_mode='categorical',
        shuffle=True,
        batch_size=24,
        seed=42,
        target_size=(200, 200))

    valid_generator = valid_datagen.flow_from_dataframe(
        dataframe=valid_df,
        directory=model_paths.valid_image_path,
        x_col=df_headers[0],
        y_col=df_headers[1],
        class_mode='categorical',
        shuffle=False,
        batch_size=24,
        seed=42,
        target_size=(200, 200))

    # test_generator = test_datagen.flow_from_dataframe(
    #     dataframe=test_df,
    #     directory=model_paths.test_image_path,
    #     x_col=df_headers[0],
    #     y_col=df_headers[1],
    #     class_mode='categorical',
    #     shuffle=False,
    #     batch_size=24,
    #     seed=42,
    #     target_size=(200, 200))

    print("CLASS INDICES:", train_generator.class_indices)

    if transfer:
        model = construct_transfer_model()
    else:
        model = construct_model()

    print("Saved model architecture to: " + model_paths.output_model_file)

    STEP_SIZE_TRAIN = train_generator.n // train_generator.batch_size + 1
    STEP_SIZE_VALID = valid_generator.n // valid_generator.batch_size + 1

    print("Training model...")

    checkpoint = ModelCheckpoint(model_paths.checkpoint_path, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
    early_stopping = EarlyStopping(monitor='val_loss', patience=3)
    callbacks_list = [checkpoint, early_stopping]

    # model.fit_generator(generator=train_generator,
    #                     steps_per_epoch=STEP_SIZE_TRAIN,
    #                     validation_data=valid_generator,
    #                     validation_steps=STEP_SIZE_VALID,
    #                     callbacks=callbacks_list,
    #                     epochs=100)

    model_json = model.to_json()
    with open(model_paths.output_model_file, "w") as json_file:
        json_file.write(model_json)

    model.save_weights(model_paths.checkpoint_overall_path, overwrite=True)

    print("Saved model to: " + model_paths.output_model_file)
    print("Saved weights to: " + model_paths.output_model_weights)

    # to do: abstract below out of file

    # Model reconstruction from JSON file
    with open(model_paths.output_model_file, 'r') as f:
        model = model_from_json(f.read())

    # Load weights into the new model
    model.load_weights(model_paths.checkpoint_overall_path)

    y_all_preds = model.predict_generator(generator=valid_generator, steps=STEP_SIZE_VALID, use_multiprocessing=True)

    y_preds = list(y_all_preds.argmax(axis=-1))

    y_actuals = valid_generator.classes

    pd.DataFrame(y_preds).to_csv(model_paths.valid_preds, index=False)

    pd.DataFrame(y_actuals).to_csv(model_paths.valid_true, index=False)

    print("Saved predictions to: " + model_paths.valid_preds)

    print("Saved actuals to: " + model_paths.valid_true)

