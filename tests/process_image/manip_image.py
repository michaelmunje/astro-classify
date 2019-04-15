from PIL import Image, ImageFilter
import os
import random
import numpy as np

image_path = os.getcwd() + '/252342.jpg'
new_path = os.getcwd() + '/manip.jpg'
pic = Image.open(image_path)

# im2 = pic.filter(ImageFilter.GaussianBlur(radius=5))
im2 = pic.rotate(45)

im2.save(new_path, quality=95)