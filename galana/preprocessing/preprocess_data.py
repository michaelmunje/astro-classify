from pipeline import extract_data
import os

root_dir = os.getcwd()
clean_dir = root_dir + "data/tables/clean"


def preprocess_data(filepath):
    df = extract_data(filepath)
    filename = '/'.split(filepath)[-1]
    df.to_csv(clean_dir + filename)
