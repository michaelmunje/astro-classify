import pandas as pd
import os
from astroquery.ned import Ned


def retrieve_tables(filepath, galaxy_names):
    result_tables = [Ned.query_object(g).to_pandas() for g in galaxy_names]
    df_tables = pd.concat(result_tables, sort=False)
    df_tables = df_tables.dropna(axis=1)
    df_tables.head()
    df_tables = df_tables.drop(['No.'], axis=1)
    return df_tables


def get_cgmw():
    file_path = os.getcwd() + '/RAW_INPUT_DATA_CGMW'
    df_tables = retrieve_tables(file_path)
