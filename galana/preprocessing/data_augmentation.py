import tensorflow as tf
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import os
import numpy as np
import pathlib as pl
from multiprocessing import Pool
import pandas as pd

BASE_TRAIN_PATH = ''
BASE_COLOR_PATH = ''
BASE_ROTATE_PATH = ''
BASE_FILTER_PATH = ''


def recolor_image(image_name, new_image_name, rand):

    image = Image.open(BASE_TRAIN_PATH + image_name)

    model = tf.global_variables_initializer()

    with tf.Session() as session:
        image = tf.image.adjust_hue(image, rand)
        tf_img = tf.image.convert_image_dtype(image, tf.float32)
        session.run(model)
        result = session.run(tf_img)

    plt.imsave(BASE_COLOR_PATH + new_image_name, result)
    print('Recolor  ', new_image_name + ' Original: ' + image_name)


def rotate_image(image_name, new_image_name, rand):

    image = Image.open(BASE_TRAIN_PATH + image_name)
    image = image.rotate(rand)
    image.save(BASE_ROTATE_PATH + new_image_name)
    print('Rotate  ', new_image_name + ' Original: ' + image_name)


def filter_image(image_name, new_image_name, f_type):

    image = Image.open(BASE_TRAIN_PATH + image_name)
    filter_types = [image.filter(ImageFilter.GaussianBlur(3)),
                    image.filter(ImageFilter.MedianFilter(3)),
                    image.filter(ImageFilter.ModeFilter(3))]

    if (0 <= f_type and f_type < 3):
        filter_types[f_type]
    else:
        print('Incorrect value assigned')

    image.save(BASE_FILTER_PATH + new_image_name)
    print('Filter  ', new_image_name + ' Original: ' + image_name)


def handle_images(sol_path, augment_sol_path, num_of_manips):
    train_list = sorted(os.listdir(BASE_TRAIN_PATH))
    train_size = len(train_list)
    train_name_start = int(train_list[-1].split('.')[0]) + 1

    hcs = update_solutions(train_name_start, num_of_manips, sol_path, augment_sol_path)
    hcs.to_csv(augment_sol_path, index=False)

    all_augment_paths = [[str(train_name_start + i + train_size * aug_no) +
                          '.jpg' for i in range(train_size * num_of_manips)]
                         for aug_no in range(3)]

    np.random.seed(1234)

    rand_rot_trains = np.random.uniform(0, 360.0, size=train_size)
    rand_hue_trains = np.random.uniform(0, 1.0, size=train_size)
    rand_filter_trains = np.random.randint(0, 3, size=train_size)

    zip_col_train = list(zip(train_list[:train_size], all_augment_paths[0], rand_hue_trains))
    zip_rot_train = list(zip(train_list[train_size:train_size * 2], all_augment_paths[1], rand_rot_trains))
    zip_filt_train = list(zip(train_list[train_size * 2:train_size * 3], all_augment_paths[2], rand_filter_trains))

    return zip_col_train, zip_rot_train, zip_filt_train


def update_solutions(start, num_of_manips, sol_path, updated_sol_path):
    df = pd.read_csv(sol_path)
    df = df.sort_values(by=['GalaxyID'])

    new_dfs = []
    new_dfs.append(df)
    for n in range(num_of_manips):
        temp = df.copy()
        s = start + (start * n)
        temp['GalaxyID'] = np.arange(s, s + len(df.index))
        new_dfs.append(temp)

    return pd.concat(new_dfs)


def augment_images(train_path, sol_path):
    NUM_MANIPS = 3
    base_path = '/'.join(train_path.split('/')[:-2])
    augment_paths = [base_path + '/train_augment/' + augment_path for augment_path in ['color', 'rotate', 'filter']]

    base_sol_path = '/'.join(sol_path.split('/')[:-1])
    augment_sol_path = base_sol_path + '/augment_' + sol_path.split('/')[-1]

    for aug_path in augment_paths:
        pl.Path(aug_path).mkdir(parents=True, exist_ok=True)

    global BASE_TRAIN_PATH, BASE_COLOR_PATH, BASE_ROTATE_PATH, BASE_FILTER_PATH

    BASE_TRAIN_PATH = train_path
    BASE_COLOR_PATH = augment_paths[0] + '/'
    BASE_ROTATE_PATH = augment_paths[1] + '/'
    BASE_FILTER_PATH = augment_paths[2] + '/'

    color_train, rot_trains, filt_trains = handle_images(sol_path, augment_sol_path, NUM_MANIPS)

    pool = Pool()
    pool.starmap(recolor_image, color_train)
    pool.starmap(rotate_image, rot_trains)
    pool.starmap(filter_image, filt_trains)

    # (os.rename(augment_path + '/' + f, model_paths.train_image_path + '/' + f) for f in os.listdir(augment_path) for augment_path in model_paths.new_paths)
