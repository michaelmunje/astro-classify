import pandas as pd


def extract_data(filepath):
    file = open(filepath, 'r')
    galaxy_names = []

    data_found = False

    for line in file.readlines():
        if '|' in line and len(line) > 1:
            s = line.split('|')[1].split('|')[0]
            s = s.rstrip()
            if data_found:
                galaxy_names.append(s)
            else:
                if s == "name":
                    data_found = True

    df = pd.DataFrame(galaxy_names, columns=['names'])

    return df
