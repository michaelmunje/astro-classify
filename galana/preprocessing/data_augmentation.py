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

NUM_MANIPS = 2

def apply_full_path(path, f_list):
    lamb = lambda p,f : p + '/' + f
    return list(map(lamb, [path]*len(f_list), f_list))

def construct_new_path_list(start_f, list_size, path):
    temp = []
    for _ in range(list_size):
        temp.append(path + '/' + str(start_f) + '.jpg')
        start_f += 1
    
    return temp, start_f

def recolor_image_old(image_path, new_path):
    pic = Image.open(image_path)
    if pic.mode in ('RGBA', 'LA'):
        # background color default to black
        background = Image.new(pic.mode[:-1], pic.size)
        background.paste(pic, pic.split()[-1])
        pic = background
    
    data = np.array(pic)
    red, green, blue = data.T

    random.seed(256)
    rand_colors = random.sample(range(0,256), 3)
    data[..., 0] = np.where(red < 256-rand_colors[0], red, red + rand_colors[0]).T
    data[..., 1] = np.where(green < 256-rand_colors[1], green, green + rand_colors[1]).T
    data[..., 2] = np.where(blue < 256-rand_colors[2], blue, blue + rand_colors[2]).T

    im2 = Image.fromarray(data)
    im2.save(new_path, quality=95)
    print('Saved this path', new_path)

def noisy_image(image_path, new_path):
    image = mpimg.imread(image_path)
    
    tf.random.set_random_seed(1234)
    # Create a TensorFlow Variable
    x = tf.Variable(image, name='x', dtype=tf.float32)

    model = tf.global_variables_initializer()

    with tf.Session() as session:
        # noise = tf.random_normal(shape=tf.shape(x), mean=0.0, stddev=0.0, dtype=tf.float32)
        noise = tf.random_uniform(shape=tf.shape(x), minval=0, maxval=0.75, dtype=tf.float32)
        x = tf.multiply(x, noise)
        session.run(model)
        result = session.run(x)

    plt.imsave(new_path, result)

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
        print('Incorrect value assinged')
    image.save(new_path)
    print('Filter', new_path)

def handle_images():
    train_list = sorted(os.listdir(old_train_path))
    train_size = len(train_list)
    train_name_start = int(train_list[-1].split('.')[0]) + 1

    hcs = handle_csvs(train_name_start, NUM_MANIPS)
    hcs.to_csv(comb_csv)

    train_paths = apply_full_path(old_train_path, train_list)

    new_train_paths, _ = construct_new_path_list(train_name_start, train_size*NUM_MANIPS, new_train_path)
    
    np.random.seed(1234)
    rand_hue_trains = np.random.uniform(0, 1.0, size=train_size)
    rand_rot_trains = np.random.uniform(0, 360.0, size=train_size)
    rand_filter_trains = np.random.randint(0, 3, size=train_size)
    
    zip_color_train = list(zip(train_paths, new_train_paths[:train_size], rand_hue_trains))
    zip_rot_train = list(zip(train_paths, new_train_paths[train_size:train_size*2], rand_rot_trains))
    zip_filt_train = list(zip(train_paths, new_train_paths[train_size*2:train_size*3], rand_filter_trains))

    return zip_rot_train, zip_filt_train

def handle_csvs(start, num_of_manips):
    orig_df = pd.read_csv(solutions_csv)
    orig_df = orig_df.sort_values(by=['GalaxyID'])
    df_size = len(orig_df.index)

    new_dfs = []
    new_dfs.append(orig_df)
    for n in range(num_of_manips):
        temp = orig_df.copy()
        s = start + (start*n)
        temp['GalaxyID'] = np.arange(s, s+df_size)
        new_dfs.append(temp)
    
    return pd.concat(new_dfs)

def augment_images():
    rot_trains, filt_trains = handle_images()
    
    pool = Pool()
    pool.starmap(filter_image, filt_trains)
    # pool.starmap(recolor_image, zip_color_test)
    # pool.starmap(recolor_image, zip_color_train)




