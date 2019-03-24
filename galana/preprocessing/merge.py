import os


def merge(data_folder_path, output_filepath):
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
