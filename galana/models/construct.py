from keras.models import Sequential
from keras_preprocessing.image import ImageDataGenerator as IDG
from keras.layers import Dense, Flatten, Dropout
from keras.layers import Conv2D, MaxPooling2D
from keras.applications import inception_v3
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint, EarlyStopping
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

    df_headers = list(train_df.columns)

    train_datagen = IDG(rescale=1. / 255., shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
    valid_datagen = IDG(rescale=1. / 255.)

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

    print("CLASS INDICES:", train_generator.class_indices)

    if transfer:
        model = construct_transfer_model()
    else:
        model = construct_model()

    STEP_SIZE_TRAIN = train_generator.n // train_generator.batch_size + 1
    STEP_SIZE_VALID = valid_generator.n // valid_generator.batch_size + 1

    print("Training model...")

    checkpoint = ModelCheckpoint(model_paths.checkpoint_path, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
    early_stopping = EarlyStopping(monitor='val_loss', patience=2)
    callbacks_list = [checkpoint, early_stopping]

    model.fit_generator(generator=train_generator,
                        steps_per_epoch=STEP_SIZE_TRAIN,
                        validation_data=valid_generator,
                        validation_steps=STEP_SIZE_VALID,
                        callbacks=callbacks_list,
                        epochs=100)

    model.save(model_paths.checkpoint_overall_path, overwrite=True)

    print("Saved model to: " + model_paths.checkpoint_overall_path)
