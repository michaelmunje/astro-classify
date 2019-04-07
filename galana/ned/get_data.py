import pandas as pd
from astroquery.ned import Ned
import os
import pathlib as pl
import time

get_root = os.getcwd()
ipac_dir = get_root + 'data/ipac/'
table_dir = get_root + '/data/mine/tables/'
pl.Path(ipac_dir).mkdir(parents=True, exist_ok=True)
pl.Path(table_dir).mkdir(parents=True, exist_ok=True)

def query_object(astro_object):
    return Ned.query_object(astro_object).to_pandas()

def query_objects(list_of_astro_objects):
    # result_tables = [Ned.query_object(astro_object).to_pandas() for astro_object in list_of_astro_objects]
    result_tables = []
    for i in range(0, len(list_of_astro_objects), 15):
        print('Going through', i, 'to', i+14)
        for obj in list_of_astro_objects[i:i+15]:
            result_tables.append(Ned.query_object(obj).to_pandas())
        time.sleep(10)
    df_tables = pd.concat(result_tables, sort=False)
    df_tables = df_tables.dropna(axis=1)
    df_tables.head()
    df_tables = df_tables.drop(['No.'], axis=1)
    return df_tables

def get_list_of_objects():
    pd_list = [pd.read_csv(table_dir + f, sep=',') for f in os.listdir(table_dir) if os.path.isfile(os.path.join(table_dir, f))]
    
    astro_object_list = []
    for pdl in pd_list:
        for name in pdl['name']:
            astro_object_list.append(name)
    
    dfs = query_objects(astro_object_list)

    print(dfs.head())
