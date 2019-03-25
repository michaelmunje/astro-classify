from .extract_data import extract_data
import os
import pathlib as pl

root_dir = os.getcwd()
clean_dir = root_dir + "data/tables/clean"


def preprocess_file(filepath, output_path=clean_dir):
    df = extract_data(filepath)
    filename = filepath.split('/')[-1]
    df.to_csv(output_path + '/' + filename)


def preprocess_folder(folderpath, output_path=clean_dir):
    pl.Path(output_path).mkdir(parents=True, exist_ok=True)
    for filename in os.listdir(folderpath):
        preprocess_file(folderpath + '/' + filename, output_path)
