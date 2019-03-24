from .extract_data import extract_data
import os

root_dir = os.getcwd()
clean_dir = root_dir + "data/tables/clean"


def preprocess_data(filepath, output_path=clean_dir):
    df = extract_data(filepath)
    filename = '/'.split(filepath)[-1]
    df.to_csv(output_path + '/' + filename)


def preprocess_folder(folderpath, output_path=clean_dir):
    for filename in os.listdir(folderpath):
        preprocess_data(filename, output_path)
