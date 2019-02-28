import pandas as pd


def extract_galaxy_names(filename):
    file = open(filename, 'r')
    galaxy_names = []

    for line in file.readlines()[6:]:
        s = line.split('|')[1].split('|')[0]
        s = s.rstrip()
        galaxy_names.append(s)
    
    df = pd.DataFrame(galaxy_names, columns = ['names'])
    
    return df


if __name__ == "__main__":
    print("")  # TODO: Add command line arguments


