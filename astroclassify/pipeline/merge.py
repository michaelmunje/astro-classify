import os
import sys


def merge(data_folder_path, output_filepath):
    files = os.listdir(data_folder_path)
    values = set()

    for file in files:
        file_data = open(os.path.join(data_folder_path, file), 'r')
        for line in file_data:
            if line.strip().strip('\n') != '':
                value = line.strip('\n')
                values.add(value)
    # if output_path is not valid, throw an exception
    write_file = open(output_filepath, 'w')
    for value in values:
        write_file.write(value + '\n')


if __name__ == "__main__":
    if len(sys.argv) == 3:
        merge(sys.argv[1], sys.argv[2])
    else:
        raise ValueError('Expects a data folder path and output file path.')
