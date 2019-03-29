from keras.models import Model
from keras_preprocessing.image import ImageDataGenerator as IDG
from keras.layers import Dense, Activation, Flatten, Dropout, BatchNormalization, Input
from keras.layers import Conv2D, MaxPooling2D
from keras import regularizers, optimizers
import pandas as pd
import numpy as np
import os


test_image_path = os.getcwd() + '/../../data/kaggle/images_test_rev1'
test_image_files = os.listdir(test_image_path)
train_image_path = os.getcwd() + '/../../data/kaggle/images_training_rev1'
train_image_files = os.listdir(train_image_path)
train_solutions = os.getcwd() + '/../../data/kaggle/training_solutions_rev1.csv'
test_file = os.getcwd() + '/../../data/kaggle/all_zeros_benchmark.csv'

df_headers = list()
model = Model()


def append_ext(fn):
    return fn + ".jpg"


def generator_wrapper(generator):
    for batch_x,batch_y in generator:
        yield (batch_x,[batch_y[:,i] for i in range(len(df_headers)-1)])


def construct_model(df_headers):
    inp = Input(shape = (424,424,3))
    x = Conv2D(32, (3, 3), padding = 'same')(inp)
    x = Activation('relu')(x)
    x = Conv2D(32, (3, 3))(x)
    x = Activation('relu')(x)
    x = MaxPooling2D(pool_size = (2, 2))(x)
    x = Dropout(0.25)(x)
    x = Conv2D(64, (3, 3), padding = 'same')(x)
    x = Activation('relu')(x)
    x = Conv2D(64, (3, 3))(x)
    x = Activation('relu')(x)
    x = MaxPooling2D(pool_size = (2, 2))(x)
    x = Dropout(0.25)(x)
    x = Flatten()(x)
    x = Dense(512)(x)
    x = Activation('relu')(x)
    x = Dropout(0.5)(x)

    outputs = []
    losses = ['binary_crossentropy']*(len(df_headers)-1)
    for _ in range(len(df_headers)-1):
        outputs.append(Dense(1, activation = 'sigmoid')(x))
    model = Model(inp,outputs)
    model.compile(optimizers.rmsprop(lr = 0.0001, decay = 1e-6),
    loss=losses,metrics=["accuracy"])
    
    return model


def train_model():

    traindf = pd.read_csv(train_solutions, dtype=str)
    testdf = pd.read_csv(test_file, dtype=str)

    traindf["GalaxyID"] = traindf["GalaxyID"].apply(append_ext)
    testdf["GalaxyID"] = testdf["GalaxyID"].apply(append_ext)
    df_headers = list(traindf.columns)
    test_headers = list(testdf.columns)

    datagen = IDG(rescale=1./255., validation_split=0.25)
    test_datagen = IDG(rescale=1./255.)

    # Create generators
    train_generator=datagen.flow_from_dataframe(
        dataframe=traindf,
        directory=train_image_path,
        x_col=df_headers[0],
        y_col=df_headers[1:],
        subset="training",
        batch_size=32,
        seed=42,
        shuffle=True,
        class_mode="other",
        target_size=(424,424))

    valid_generator=datagen.flow_from_dataframe(
        dataframe=traindf,
        directory=train_image_path,
        x_col=df_headers[0],
        y_col=df_headers[1:],
        subset="validation",
        batch_size=32,
        seed=42,
        shuffle=True,
        class_mode="other",
        target_size=(424,424))

    test_generator = test_datagen.flow_from_dataframe(
        dataframe=testdf,
        directory=test_image_path,
        x_col=test_headers[0],
        y_col=test_headers[1:],
        batch_size=32,
        seed=42,
        shuffle=False,
        class_mode=None,
        target_size=(424,424))

    model = construct_model(df_headers)

    # Train the model
    STEP_SIZE_TRAIN=train_generator.n//train_generator.batch_size
    STEP_SIZE_VALID=valid_generator.n//valid_generator.batch_size
    STEP_SIZE_TEST=test_generator.n//test_generator.batch_size
    model.fit_generator(generator=generator_wrapper(train_generator),
                        steps_per_epoch=STEP_SIZE_TRAIN,
                        validation_data=generator_wrapper(valid_generator),
                        validation_steps=STEP_SIZE_VALID,
                        epochs=1,verbose=2)

    # Predict Model
    test_generator.reset()
    pred = model.predict_generator(test_generator,
                                  steps=STEP_SIZE_TEST,
                                  verbose=1)


