import os
import pandas as pd


def remove_others(training_path, clean_train_sols):

    df = pd.read_csv(clean_train_sols)

    print("Removing bad entries...")

    num_of_others = 0

    for index, row in df.iterrows():
        if row['Type'] == 'Other':
            os.remove(training_path + row['GalaxyID'])
            df.drop([index], inplace=True)
            num_of_others += 1

    print("Other entries deleted: ", num_of_others)

    df.to_csv(clean_train_sols)
