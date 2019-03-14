#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import os
from astroquery.ned import Ned 

def extract_galaxy_names(filename):
    file = open(filename, 'r')
    galaxy_names = []

    data_found = False

    for line in file.readlines():
        if '|' in line and len(line) > 1:
            s = line.split('|')[1].split('|')[0]
            s = s.rstrip()
            if (data_found):
                galaxy_names.append(s)
            else:
                if (s == "name"):
                    data_found = True

    df = pd.DataFrame(galaxy_names, columns=['names'])

    return df

def retreive_tables(filepath):
    g_names = list(extract_galaxy_names(file_name)['names'])
    result_tables = [Ned.query_object(g).to_pandas() for g in g_names]
    df_tables = pd.concat(result_tables, sort=False)
    df_tables = df_tables.dropna(axis=1)
    df_tables.head()
    df_tables = df_tables.drop(['No.'], axis=1)
    
    return df_tables

file_path = os.getcwd() + '/RAW_INPUT_DATA_CGMW'
df_tables = retreive_tables(file_path)






