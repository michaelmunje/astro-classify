import pandas as pd
from astroquery.simbad import Simbad
from astroquery.ned import Ned
import os
import pathlib as pl
import numpy as np
import json
import time

root_dir = os.getcwd()
ipac_dir = root_dir + 'data/ipac/'
table_dir = root_dir + '/data/mine/tables/'
alias_file = root_dir + '/data/mine/aliases.json'

pl.Path(ipac_dir).mkdir(parents=True, exist_ok=True)
pl.Path(table_dir).mkdir(parents=True, exist_ok=True)


def query_object(astro_object):
    return Ned.query_object(astro_object).to_pandas()


def get_aliases(list_of_astro_objects):
    downloaded_names = dict()
    result_tables = []
    for i, obj in enumerate(list_of_astro_objects):
        print('Processing ', i + 1, ' / ', len(list_of_astro_objects))
        if obj not in downloaded_names.keys() and obj not in downloaded_names.values():
            ids = Simbad.query_objectids(obj)
            if ids:
                downloaded_names[obj] = [np.asarray(ids.as_array(), dtype=str)]

    import json
    with open(alias_file, 'w') as fp:
        json.dump(downloaded_names, fp)


def get_aliases_from_data():
    pd_list = [pd.read_csv(table_dir + f, sep=',') for f in os.listdir(table_dir) if
               os.path.isfile(os.path.join(table_dir, f))]

    astro_object_list = []
    for pdl in pd_list:
        for name in pdl['name']:
            astro_object_list.append(name)

    get_aliases(astro_object_list)
