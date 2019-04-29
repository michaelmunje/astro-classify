import tensorflow as tf
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import os
import numpy as np
from multiprocessing import Pool
import pathlib as pl
import pandas as pd

BASE_TRAIN_PATH = ''
BASE_COLOR_PATH = ''
BASE_ROTATE_PATH = ''
BASE_FILTER_PATH = ''
NUM_OF_MANIPS = 3


def recolor_image(color_trains):

    model = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(model)

    for image_name, new_image_name, rand in color_trains:

        if not os.path.isfile(BASE_COLOR_PATH + new_image_name):

            image = Image.open(BASE_TRAIN_PATH + image_name)

            image = tf.image.adjust_hue(image, rand)
            tf_img = tf.image.convert_image_dtype(image, tf.float32)

            result = sess.run(tf_img)

            plt.imsave(BASE_COLOR_PATH + new_image_name, result)

            print('Recolor ', new_image_name + ' Original: ' + image_name)

    sess.close()
    tf.reset_default_graph()


def rotate_image(image_name, new_image_name, rand):

    image = Image.open(BASE_TRAIN_PATH + image_name)
    image = image.rotate(rand)
    image.save(BASE_ROTATE_PATH + new_image_name)
    print('Rotate ', new_image_name + ' Original: ' + image_name)


def filter_image(image_name, new_image_name, f_type):

    image = Image.open(BASE_TRAIN_PATH + image_name)
    filter_types = [ImageFilter.GaussianBlur(3),
                    ImageFilter.MedianFilter(3),
                    ImageFilter.ModeFilter(3)]

    if 0 <= f_type < 3:
        image.filter(filter_types[f_type])
    else:
        print('Incorrect value assigned')

    image.save(BASE_FILTER_PATH + new_image_name)
    print('Filter ', new_image_name + ' Original: ' + image_name)


def handle_images(sol_path):
    train_list = sorted(os.listdir(BASE_TRAIN_PATH))

    df = pd.read_csv(sol_path)
    df['GalaxyID'] = df['GalaxyID'].apply(lambda f: f[:-4]).astype(int)
    df = df.sort_values(by=['GalaxyID'])

    train_name_start = df.iloc[-1, ]['GalaxyID'] + 1
    train_size = len(df['GalaxyID'])

    all_augment_paths = [[str(train_name_start + i + train_size * aug_no) +
                          '.jpg' for i in range(train_size * NUM_OF_MANIPS)]
                         for aug_no in range(NUM_OF_MANIPS)]

    np.random.seed(1234)

    rand_rot_trains = np.random.uniform(0, 360.0, size=train_size)
    rand_hue_trains = np.random.uniform(0, 1.0, size=train_size)
    rand_filter_trains = np.random.randint(0, 3, size=train_size)

    zip_col_train = list(zip(train_list, all_augment_paths[0], rand_hue_trains))
    zip_rot_train = list(zip(train_list, all_augment_paths[1], rand_rot_trains))
    zip_filt_train = list(zip(train_list, all_augment_paths[2], rand_filter_trains))

    return zip_col_train, zip_rot_train, zip_filt_train


def update_solutions(sol_path, updated_sol_path):

    df = pd.read_csv(sol_path)
    df['GalaxyID'] = df['GalaxyID'].apply(lambda f: f[:-4]).astype(int)

    df = df.sort_values(by=['GalaxyID'])

    train_name_start = df.iloc[-1, ]['GalaxyID'] + 1

    train_size = len(df['GalaxyID'])

    df = pd.concat([df] * NUM_OF_MANIPS, ignore_index=True)

    for i in range(NUM_OF_MANIPS):
        print("Processing augment csv update ", (i + 1), " / ", NUM_OF_MANIPS)
        df.update(df.iloc[train_size * (i + 1): train_size * (i + 2), ]['GalaxyID'].apply
                  (lambda id_num: train_name_start + id_num + train_size * i))

    df["GalaxyID"] = df["GalaxyID"].astype(int)

    df["GalaxyID"] = df["GalaxyID"].astype(str).apply(lambda x: x + ".jpg")

    df.to_csv(updated_sol_path, index=False)


def augment_images(train_path, sol_path):
    augments = ['color', 'rotate', 'filter']
    base_path = '/'.join(train_path.split('/')[:-2])
    augment_paths = [base_path + '/train_augment/' + augment_path for augment_path in augments]

    for augment_path in augment_paths:
        pl.Path(augment_path).mkdir(parents=True, exist_ok=True)

    global BASE_TRAIN_PATH, BASE_COLOR_PATH, BASE_ROTATE_PATH, BASE_FILTER_PATH

    BASE_TRAIN_PATH = train_path
    BASE_COLOR_PATH = augment_paths[0] + '/'
    BASE_ROTATE_PATH = augment_paths[1] + '/'
    BASE_FILTER_PATH = augment_paths[2] + '/'

    color_trains, rot_trains, filt_trains = handle_images(sol_path)

    batch_size = 100
    for i in range(len(color_trains) // batch_size):
        print("Batch ", (i + 1), " out of ", (len(color_trains) // batch_size))
        recolor_image(color_trains[batch_size * i: batch_size * (i + 1) if i != (len(color_trains) // batch_size - 1) else len(color_trains)])

    pool = Pool()

    pool.starmap(rotate_image, rot_trains)
    pool.starmap(filter_image, filt_trains)

    (os.rename(augment_path + '/' + f, train_path + '/' + f) for f in os.listdir(augment_path) for augment_path in augment_paths)
