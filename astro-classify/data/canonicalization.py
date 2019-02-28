import os
import sys


def canonicalize(data_folder_path, output_path=''):
    path = data_folder_path
    files = os.listdir(path)
    values = set()

    for file in files:
        file_data = open(os.path.join(path, file), 'r')
        for line in file_data:
            if line.strip().strip('\n') != '':
                value = line.strip('\n')
                values.add(value)
    output_file = 'Master.txt'
    if output_path != '':
        output_file = os.path.join(output_path, output_file)
    write_file = open(output_file, 'w')
    ordered_values = list(values)
    ordered_values.sort()
    for value in ordered_values:
        write_file.write(value + '\n')


if __name__ == "__main__":
    if len(sys.argv) == 2:
        canonicalize(sys.argv[1])
    elif len(sys.argv) == 3:
        canonicalize(sys.argv[1], sys.argv[2])
    else:
        raise ValueError('Expects an argument of the folder containing the data files')
