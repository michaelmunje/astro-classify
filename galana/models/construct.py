from keras.models import Sequential
from keras_preprocessing.image import ImageDataGenerator as IDG
from keras.layers import Dense, Flatten, Dropout
from keras.layers import Conv2D, MaxPooling2D, Cropping2D
from keras.applications import inception_v3
from keras.optimizers import Adam, SGD
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.models import model_from_json
import pandas as pd


def construct_outer_layer_transfer():

    base_model = inception_v3.InceptionV3(include_top=False, weights='imagenet', pooling='avg', input_shape=[200, 200, 3])

    model = Sequential([
        base_model,
        Dense(1024, activation='relu'),
        Dropout(0.5),
        Dense(512, activation='relu'),
        Dense(4, activation='softmax')
    ])

    for layer in base_model.layers:
        layer.trainable = False

    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    return model


def fine_tune_transfer(model):

    for layer in model.layers:
        layer.trainable = True

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
        Dense(4, activation='softmax')
    ])

    model.compile(loss='categorical_crossentropy',
                  optimizer='Adam',
                  metrics=['accuracy'])

    return model


def train_model(model_paths, transfer=False):

    traindf = pd.read_csv(model_paths.clean_train_solutions)

    df_headers = list(traindf.columns)

    datagen = IDG(rescale=1. / 255., validation_split=0.20)

    # Create generators
    train_generator = datagen.flow_from_dataframe(
        dataframe=traindf,
        directory=model_paths.train_image_path,
        x_col=df_headers[0],
        y_col=df_headers[1],
        subset="training",
        class_mode='categorical',
        batch_size=24,
        seed=42,
        target_size=(200, 200))

    valid_generator = datagen.flow_from_dataframe(
        dataframe=traindf,
        directory=model_paths.train_image_path,
        x_col=df_headers[0],
        y_col=df_headers[1],
        subset="validation",
        class_mode='categorical',
        batch_size=24,
        seed=42,
        target_size=(200, 200))

    if transfer:
        model = construct_outer_layer_transfer()
    else:
        model = construct_model()

    # print("Saved model to: " + model_paths.output_model_file)

    STEP_SIZE_TRAIN = train_generator.n // train_generator.batch_size
    STEP_SIZE_VALID = valid_generator.n // valid_generator.batch_size

    print("Training model...")

    checkpoint = ModelCheckpoint(model_paths.checkpoint_path, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
    early_stopping = EarlyStopping(monitor='val_loss', patience=2)
    callbacks_list = [checkpoint, early_stopping]

    # print("Saved model to: " + model_paths.output_model_file)

    model.fit_generator(generator=train_generator,
                        steps_per_epoch=STEP_SIZE_TRAIN,
                        validation_data=valid_generator,
                        validation_steps=STEP_SIZE_VALID,
                        callbacks=callbacks_list,
                        epochs=30)

    # # Model reconstruction from JSON file
    # with open('data/kaggle/galaxy_classifier_model.json', 'r') as f:
    #     model = model_from_json(f.read())

    # Load weights into the new model
    # model.load_weights('data/kaggle/checkpoint-04-0.74.hdf5')

    if transfer:
        model = fine_tune_transfer(model)
        model.fit_generator(generator=train_generator,
                            steps_per_epoch=STEP_SIZE_TRAIN,
                            validation_data=valid_generator,
                            validation_steps=STEP_SIZE_VALID,
                            callbacks=callbacks_list,
                            epochs=30)

    model_json = model.to_json()
    with open(model_paths.output_model_file, "w") as json_file:
        json_file.write(model_json)

    model.save_weights(model_paths.output_model_weights, overwrite=True)

    print("Saved model to: " + model_paths.output_model_file)
    print("Saved weights to: " + model_paths.output_model_weights)

    y_preds = model.evaluate_generator(generator=valid_generator, steps=STEP_SIZE_VALID)

    pd.DataFrame(y_preds).to_csv(model_paths.valid_preds)

    # valid_generator.get_classes()

    print("Saved validation predictions to: " + model_paths.valid_preds)
    print("Saved validation true to: " + model_paths.valid_true)
