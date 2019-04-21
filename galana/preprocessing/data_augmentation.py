import tensorflow as tf
from PIL import Image, ImageFilter
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os
import random
import numpy as np
import pathlib as pl
from multiprocessing import Pool
import pandas as pd

kaggle_path = os.getcwd() + '/data/kaggle'
old_train_path = kaggle_path + '/images_training_rev1'
new_train_path = kaggle_path + '/images_manip_train'
solutions_csv = kaggle_path + '/training_solutions_rev1.csv'
comb_csv = kaggle_path + '/updated_solutions.csv'
pl.Path(new_train_path).mkdir(parents=True, exist_ok=True)

NUM_MANIPS = 3


def apply_full_path(path, f_list):
    lamb = lambda p, f: p + '/' + f
    return list(map(lamb, [path] * len(f_list), f_list))
    # return [lambda f: path + '/' + f for f in f_list]


def construct_new_path_list(start_f, list_size, path):
    temp = []
    for i in range(list_size):
        temp.append(path + '/' + str(start_f + i) + '.jpg')

    return temp


def recolor_image(image_path, new_path, rand):
    image = Image.open(image_path)

    model = tf.global_variables_initializer()

    with tf.Session() as session:
        image = tf.image.adjust_hue(image, rand)
        tf_img = tf.image.convert_image_dtype(image, tf.float32)
        session.run(model)
        result = session.run(tf_img)

    plt.imsave(new_path, result)
    print('Recolor', new_path)


def rotate_image(image_path, new_path, rand):
    image = Image.open(image_path)
    image = image.rotate(rand)
    image.save(new_path)
    print('Rotate', new_path)


def filter_image(image_path, new_path, f_type):
    image = Image.open(image_path)
    if f_type == 0:
        image.filter(ImageFilter.GaussianBlur(3))
    elif f_type == 1:
        image.filter(ImageFilter.MedianFilter(3))
    elif f_type == 2:
        image.filter(ImageFilter.ModeFilter(3))
    else:
        print('Incorrect value assigned')
    image.save(new_path)
    print('Filter', new_path)


def handle_images():
    train_list = sorted(os.listdir(old_train_path))
    train_size = len(train_list)
    train_name_start = int(train_list[-1].split('.')[0]) + 1

    hcs = handle_csvs(train_name_start, NUM_MANIPS)
    hcs.to_csv(comb_csv, index=False)

    train_paths = apply_full_path(old_train_path, train_list)

    new_train_paths = construct_new_path_list(train_name_start, train_size * NUM_MANIPS, new_train_path)

    np.random.seed(1234)
    rand_hue_trains = np.random.uniform(0, 1.0, size=train_size)
    rand_rot_trains = np.random.uniform(0, 360.0, size=train_size)
    rand_filter_trains = np.random.randint(0, 3, size=train_size)

    zip_color_train = list(zip(train_paths, new_train_paths[:train_size], rand_hue_trains))
    zip_rot_train = list(zip(train_paths, new_train_paths[train_size:train_size * 2], rand_rot_trains))
    zip_filt_train = list(zip(train_paths, new_train_paths[train_size * 2:train_size * 3], rand_filter_trains))

    return zip_color_train, zip_rot_train, zip_filt_train


def handle_csvs(start, num_of_manips):
    orig_df = pd.read_csv(solutions_csv)
    orig_df = orig_df.sort_values(by=['GalaxyID'])
    df_size = len(orig_df.index)

    new_dfs = []
    new_dfs.append(orig_df)
    for n in range(num_of_manips):
        temp = orig_df.copy()
        s = start + (start * n)
        temp['GalaxyID'] = np.arange(s, s + df_size)
        new_dfs.append(temp)

    return pd.concat(new_dfs)


def augment_images():
    color_train, rot_trains, filt_trains = handle_images()

    pool = Pool()
    pool.starmap(recolor_image, color_train)
    pool.starmap(filter_image, filt_trains)
    pool.starmap(rotate_image, rot_trains)

    (os.rename(new_train_path + '/' + f, old_train_path + '/' + f) for f in os.listdir(new_train_path))
