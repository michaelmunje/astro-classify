from keras.models import Sequential
from keras_preprocessing.image import ImageDataGenerator as IDG
from keras.layers import Dense, Flatten, Dropout
from keras.layers import Conv2D, MaxPooling2D, Cropping2D
from keras.applications import inception_v3
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint
import pandas as pd


def construct_transfer_model():
    model = Sequential([
        Cropping2D(cropping=((64, 63), (64, 63)), input_shape=[424, 424, 3]),
        inception_v3.InceptionV3(include_top=False, weights='imagenet', pooling='avg'),
        Dense(1024, activation='relu'),
        Dense(1024, activation='relu'),
        Dense(512, activation='relu'),
        Dense(4, activation='softmax')
    ])

    model.compile(loss='categorical_crossentropy',
                  optimizer=Adam(lr=0.000001),
                  metrics=['accuracy'])

    return model


def construct_model():
    model = Sequential([
        Cropping2D(cropping=((100, 100), (100, 100)), input_shape=[424, 424, 3]),
        Conv2D(32, (3, 3), activation='relu'),
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
        target_size=(424, 424))

    valid_generator = datagen.flow_from_dataframe(
        dataframe=traindf,
        directory=model_paths.train_image_path,
        x_col=df_headers[0],
        y_col=df_headers[1],
        subset="validation",
        class_mode='categorical',
        batch_size=24,
        seed=42,
        target_size=(424, 424))

    if transfer:
        model = construct_transfer_model()
    else:
        model = construct_model()

    STEP_SIZE_TRAIN = train_generator.n // train_generator.batch_size
    STEP_SIZE_VALID = valid_generator.n // valid_generator.batch_size

    print("Training model...")

    checkpoint = ModelCheckpoint(model_paths.checkpoint_path, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
    callbacks_list = [checkpoint]

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
    print("Saved validation true to: " + model_paths.valid_)
