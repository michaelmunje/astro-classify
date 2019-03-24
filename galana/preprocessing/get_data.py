#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import os
from astroquery.ned import Ned 
from .extract_data import extract_galaxy_names


def retreive_tables(filepath):
    g_names = list(extract_galaxy_names(file_path)['names'])
    result_tables = [Ned.query_object(g).to_pandas() for g in g_names]
    df_tables = pd.concat(result_tables, sort=False)
    df_tables = df_tables.dropna(axis=1)
    df_tables.head()
    df_tables = df_tables.drop(['No.'], axis=1)
    
    return df_tables


def get_cgmw():
    file_path = os.getcwd() + '/RAW_INPUT_DATA_CGMW'
    df_tables = retreive_tables(file_path)
