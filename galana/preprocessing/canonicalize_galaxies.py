import pandas as pd
from astroquery.simbad import Simbad
import os
import pathlib as pl
import numpy as np
import json

root_dir = os.getcwd()
ipac_dir = root_dir + 'data/ipac/'
table_dir = root_dir + '/data/mine/tables/'
alias_file = root_dir + '/data/mine/aliases.json'

pl.Path(ipac_dir).mkdir(parents=True, exist_ok=True)
pl.Path(table_dir).mkdir(parents=True, exist_ok=True)


def canonicalize_galaxies():

    downloaded_names = dict()

    for table_csv in filter(lambda x: True if x.endswith("csv") else False, os.listdir(table_dir)):

        df = pd.read_csv(table_dir + table_csv)
        for index, name in enumerate(df['name']):

            print('Processing ', index + 1, ' / ', len(df['name']), ' in file: ', table_csv)

            found_key = False
            for key, value in downloaded_names:
                if name in value:
                    df.iloc[index,]['name'] = key
                    break
                elif name == key:
                    found_key = True
                    break

            if not found_key:
                ids = Simbad.query_objectids(name)
                downloaded_names[name] = [np.asarray(ids.as_array(), dtype=str)] if ids else []
            
        df.to_csv(table_csv)

    with open(alias_file, 'w') as fp:
        json.dump(downloaded_names, fp)
