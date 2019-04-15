import tensorflow as tf
from PIL import Image, ImageFilter
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os
import random
import numpy as np
import pathlib as pl
from multiprocessing import Pool

kaggle_path = os.getcwd() + '/data/kaggle'
old_test_path = kaggle_path + '/images_test_rev1'
old_train_path = kaggle_path + '/images_training_rev1'
new_test_path = kaggle_path + '/images_manip_test'
new_train_path = kaggle_path + '/images_manip_train'
pl.Path(new_test_path).mkdir(parents=True, exist_ok=True)
pl.Path(new_train_path).mkdir(parents=True, exist_ok=True)

def app_old_test_path(f):
    return old_test_path + '/' + f

def app_old_train_path(f):
    return old_train_path + '/' + f

def app_new_test_path(f):
    return new_test_path + '/' + f

def app_new_train_path(f):
    return new_train_path + '/' + f

def construct_new_path_list(start_f, list_size, path):
    temp = []
    for _ in range(list_size):
        temp.append(path + '/' + str(start_f) + '.jpg')
        start_f += 1
    
    return temp

def pair_lists(list1, list2):
    temp = []
    for l1, l2 in zip(list1, list2):
        temp.append((l1, l2))
    
    return temp

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

def recolor_image(image_path, new_path):
    image = mpimg.imread(image_path)

    # Create a TensorFlow Variable
    x = tf.Variable(image, name='x', dtype=tf.float32)

    model = tf.global_variables_initializer()

    with tf.Session() as session:
        noise = tf.random_normal(shape=tf.shape(x), mean=0.0, stddev=1.0, dtype=tf.float32)
        x = tf.add(x, noise)
        session.run(model)
        result = session.run(x)

    plt.imshow(result)
    plt.show()



def temp():
    test_list = sorted(os.listdir(old_test_path))
    train_list = sorted(os.listdir(old_train_path))

    test_name_start = int(test_list[-1].split('.')[0]) + 1
    train_name_start = int(train_list[-1].split('.')[0]) + 1

    test_paths = list(map(app_old_test_path, test_list))
    train_paths = list(map(app_old_train_path, train_list))

    new_test_paths = construct_new_path_list(test_name_start, len(test_list), new_test_path)
    new_train_paths = construct_new_path_list(train_name_start, len(train_list), new_train_path)

    pair_test = pair_lists(test_paths, new_test_paths)
    pair_train = pair_lists(train_paths, new_train_paths) 

    # pool = Pool()
    # pool.starmap(recolor_image, pair_test)
    # pool.starmap(recolor_image, pair_train)
    recolor_image(test_paths[0], new_test_paths[0])




