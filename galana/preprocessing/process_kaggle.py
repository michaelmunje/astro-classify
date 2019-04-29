import pandas as pd
import pathlib as pl
import os


def append_ext(fn):
    return fn + ".jpg"


def process_kaggle(filepath, out_filepath):

    df = pd.read_csv(filepath)

    df['GalaxyID'] = df['GalaxyID'].astype(str)

    df["GalaxyID"] = df["GalaxyID"].apply(append_ext)

    df['Spiral'] = df['Class1.2'] * df['Class2.2']
    df['Irregular'] = df['Class6.1'] * (df['Class1.1'] + (df['Class1.2'] * df['Class2.1']))
    df['Elliptical'] = df['Class6.2'] * (df['Class1.1'] + (df['Class1.2'] * df['Class2.1']))
    df['Other'] = 1 - df['Elliptical'] - df['Irregular'] - df['Spiral']

    df = df.drop(columns=['Class1.1', 'Class1.2', 'Class1.3', 'Class2.1',
                          'Class2.2', 'Class3.1', 'Class3.2', 'Class4.1',
                          'Class4.2', 'Class5.1', 'Class5.2', 'Class5.3', 'Class5.4',
                          'Class6.1', 'Class6.2', 'Class7.1', 'Class7.2',
                          'Class7.3', 'Class8.1', 'Class8.2', 'Class8.3', 'Class8.4', 'Class8.5',
                          'Class8.6', 'Class8.7', 'Class9.1', 'Class9.2', 'Class9.3', 'Class10.1',
                          'Class10.2', 'Class10.3', 'Class11.1', 'Class11.2', 'Class11.3', 'Class11.4',
                          'Class11.5', 'Class11.6'])

    df['Type'] = df.loc[:, 'Spiral':'Other'].idxmax(axis=1)

    df = df.drop(columns=['Spiral', 'Elliptical', 'Irregular', 'Other'])

    pl.Path(os.path.dirname(out_filepath)).mkdir(parents=True, exist_ok=True)

    df.to_csv(out_filepath, index=False)
