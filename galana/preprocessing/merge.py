import os
import pathlib as pl


def merge(data_folder_path, output_filepath):
    pl.Path(os.path.dirname(output_filepath)).mkdir(parents=True, exist_ok=True)
    files = os.listdir(data_folder_path)
    values = list()

    for file in files:
        file_data = open(os.path.join(data_folder_path, file), 'r')
        for line in file_data:
            if line.strip().strip('\n') != '':
                value = line.strip('\n')
                values.append(value)
    values.sort()
    # if output_path is not valid, throw an exception
    write_file = open(output_filepath, 'w')
    for value in values:
        write_file.write(value + '\n')
