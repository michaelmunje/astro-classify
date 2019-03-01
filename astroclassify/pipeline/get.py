import os
import pathlib as pl
import urllib.request
import zipfile


def get_data(url, data_name, is_zip = True):
    root_dir = os.getcwd()
    data_dir = os.path.abspath(root_dir + f"/../../../data/")
    galaxy_dir = data_dir + '/' + data_name
    pl.Path(data_dir).mkdir(parents=True, exist_ok=True)
    os.chdir(data_dir)

    fname = "tmp"
    if is_zip:
        fname += ".zip"

    urllib.request.urlretrieve(url, filename=fname)
    pl.Path(galaxy_dir).mkdir(parents=True, exist_ok=True)

    if is_zip:
        zip_ref = zipfile.ZipFile(data_dir + '/' + fname, 'r')
        zip_ref.extractall(galaxy_dir)
        zip_ref.close()

    print("Finished downloading data.")


if __name__ == "__main__":
    print("")  # TODO: Add command line arguments
