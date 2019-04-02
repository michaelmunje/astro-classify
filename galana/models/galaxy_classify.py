from keras.models import Sequential
from keras_preprocessing.image import ImageDataGenerator as IDG
from keras.layers import Dense, Flatten, Dropout
from keras.layers import Conv2D, MaxPooling2D, Cropping2D
from keras.applications import inception_v3
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint
import pandas as pd
import os


test_image_path = ""
test_image_files = ""
train_image_path = ""
train_image_files = ""
train_solutions = ""
test_file = ""
output_model_file = ""
output_model_weights = ""
checkpoint_path = ""


def populate_paths():
    test_image_path = os.getcwd() + '/data/kaggle/images_test_rev1/'
    test_image_files = os.listdir(test_image_path)
    train_image_path = os.getcwd() + '/data/kaggle/images_training_rev1/'
    train_image_files = os.listdir(train_image_path)
    train_solutions = os.getcwd() + '/data/kaggle/training_solutions_rev1.csv'
    test_file = os.getcwd() + '/data/kaggle/all_zeros_benchmark.csv'
    output_model_file = os.getcwd() + '/data/kaggle/galaxy_classifier_model.json'
    output_model_weights = os.getcwd() + '/data/kaggle/galaxy_classifier_weights.h5'
    checkpoint_path = "data/kaggle/checkpoint-{epoch:02d}-{val_acc:.2f}.hdf5"

def read_galaxy_zoo(filepath):
    df = pd.read_csv(filepath)

    df['GalaxyID'] = df['GalaxyID'].astype(str)

    df['Spiral'] = df['Class1.2'] * df['Class2.2']
    df['Irregular'] = df['Class6.1'] * (df['Class1.1'] + (df['Class1.2'] * df['Class2.1']))
    df['Elliptical'] = df['Class6.2'] * (df['Class1.1'] + (df['Class1.2'] * df['Class2.1']))
    df['Other'] = 1 - df['Elliptical'] - df['Irregular'] - df['Spiral']

    df = df.drop(columns=['Class1.1', 'Class1.2', 'Class1.3', 'Class2.1',
            'Class2.2', 'Class3.1', 'Class3.2', 'Class4.1',
            'Class4.2', 'Class5.1', 'Class5.2', 'Class5.3', 'Class5.4',
            'Class6.1', 'Class6.2', 'Class7.1', 'Class7.2',
            'Class7.3', 'Class8.1', 'Class8.2', 'Class8.3', 'Class8.4', 'Class8.5',
            'Class8.6', 'Class8.7', 'Class9.1', 'Class9.2', 'Class9.3', 'Class10.1',
            'Class10.2', 'Class10.3', 'Class11.1', 'Class11.2', 'Class11.3', 'Class11.4',
            'Class11.5', 'Class11.6'])

    df['Type'] = df.loc[:, 'Spiral':'Other'].idxmax(axis=1)

    df = df.drop(columns=['Spiral', 'Elliptical', 'Irregular', 'Other'])

    return df


def append_ext(fn):
    return fn + ".jpg"


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

def summary():



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


def train_model(transfer=False):
    populate_paths()
    traindf = read_galaxy_zoo(train_solutions)

    traindf["GalaxyID"] = traindf["GalaxyID"].apply(append_ext)
    df_headers = list(traindf.columns)

    datagen = IDG(rescale=1./255., validation_split=0.20)

    # Create generators
    train_generator = datagen.flow_from_dataframe(
        dataframe=traindf,
        directory=train_image_path,
        x_col=df_headers[0],
        y_col=df_headers[1],
        subset="training",
        class_mode='categorical',
        batch_size=24,
        seed=42,
        target_size=(424, 424))

    valid_generator = datagen.flow_from_dataframe(
        dataframe=traindf,
        directory=train_image_path,
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

    STEP_SIZE_TRAIN = train_generator.n//train_generator.batch_size
    STEP_SIZE_VALID = valid_generator.n//valid_generator.batch_size

    print("Training model...")

    checkpoint = ModelCheckpoint(checkpoint_path, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
    callbacks_list = [checkpoint]

    model.fit_generator(generator=train_generator,
                        steps_per_epoch=STEP_SIZE_TRAIN,
                        validation_data=valid_generator,
                        validation_steps=STEP_SIZE_VALID,
                        callbacks=callbacks_list,
                        epochs=30)

    model_json = model.to_json()
    with open(output_model_file, "w") as json_file:
        json_file.write(model_json)

    model.save_weights(output_model_weights, overwrite=True)

    print("Saved model to: " + output_model_file)
    print("Saved weights to: " + output_model_weights)
