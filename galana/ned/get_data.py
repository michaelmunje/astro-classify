import pandas as pd
from astroquery.ned import Ned


def query_object(astro_object):
    return Ned.query_object(astro_object).to_pandas()


def query_objects(list_of_astro_objects):
    result_tables = [Ned.query_object(astro_object).to_pandas() for astro_object in list_of_astro_objects]
    df_tables = pd.concat(result_tables, sort=False)
    df_tables = df_tables.dropna(axis=1)
    df_tables.head()
    df_tables = df_tables.drop(['No.'], axis=1)
    return df_tables
