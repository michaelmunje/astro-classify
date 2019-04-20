import pandas as pd


def strip_list(input_list):
    if input_list[0] == '':
        input_list = input_list[1:]
    if input_list[-1] == '':
        input_list = input_list[:-1]
    return input_list


def extract_data(filepath):
    file = open(filepath, 'r')
    df = pd.DataFrame()

    header_found = False
    current_index = 0

    for line in file.readlines():
        if '|' in line and len(line) > 1:
            row = line.split('|')
            row = [value.strip() for value in row]
            row = strip_list(row)
            row = [value if value != '' else 'null' for value in row]
            if header_found is True:
                df.loc[current_index] = row
                current_index += 1
            else:
                if header_found is False:
                    header_found = True
                    df = pd.DataFrame(columns=row)
    return df


def extract_galaxy_names(filename):
    return list(extract_data(filename)['name'])
