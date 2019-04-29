from PIL import Image
import os
import random
import numpy as np

image_path = os.getcwd() + '/252342.jpg'
new_path = os.getcwd() + '/new_color.jpg'
pic = Image.open(image_path)

# # Get the size of the image
# width, height = pic.size

# # Process every pixel
# for x in range(width):
#     for y in range(height):
#         current_color = pic.getpixel((x,y))
#         new_color = tuple(random.sample(range(0, 256), 3))
#         pic.putpixel((x,y), new_color)
#         pic.save(new_path)
#     print('Processed', x)
if pic.mode in ('RGBA', 'LA'):
    # background color default to black
    background = Image.new(pic.mode[:-1], pic.size)
    background.paste(pic, pic.split()[-1])
    pic = background
data = np.array(pic)   # "data" is a height x width x 4 numpy array
red, green, blue = data.T # Temporarily unpack the bands for readability
 
# Replace white with red...
# white_areas = (red < 255) & (blue < 255) & (green < 255)
# data[..., :][white_areas.T] = (255, 0, 0) # Transpose back needed
random.seed(43)
rand_colors = random.sample(range(0,256), 3)
data[..., 0] = np.where(red < 256-rand_colors[0], red, red + rand_colors[0])
data[..., 1] = np.where(green < 256-rand_colors[1], green, green + rand_colors[1])
data[..., 2] = np.where(blue < 256-rand_colors[2], blue, blue + rand_colors[2])

im2 = Image.fromarray(data)
im2.save(new_path, quality=95)