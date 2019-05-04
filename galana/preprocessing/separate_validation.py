import os
import pandas as pd


def move_valids(train_path, valid_path, valids):
    for valid in valids:
        os.rename(train_path + valid, valid_path + valid)


def create_valids(train_path, valid_path, clean_all_sols, clean_train_sols, valid_sols):

    df = pd.read_csv(clean_all_sols)

    df_valid = df.sample(frac=0.2, random_state=43)
    df = df.drop(df_valid.index)

    df.to_csv(clean_train_sols, index=False)
    df_valid.to_csv(valid_sols, index=False)

    valids = list(df_valid['GalaxyID'])
    move_valids(train_path, valid_path, valids)

