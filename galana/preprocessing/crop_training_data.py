from PIL import Image
import os.path


def crop_all(training_path):
    images = os.listdir(training_path)
    num_of_images = len(images)
    for index, img in enumerate(images):
        print("Cropping img ", index + 1, " / ", num_of_images)
        fullpath = os.path.join(training_path, img)
        if os.path.isfile(fullpath):
            im = Image.open(fullpath)
            imCrop = im.crop((112, 112, 312, 312))
            imCrop.save(fullpath)
