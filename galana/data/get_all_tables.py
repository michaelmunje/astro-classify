import os
from multiprocessing import Pool
from ..data import get_all_tables_names
from ..data import run_table_query


def get_all_tables():
    print("Retrieving all table names...")
    table_names = get_all_tables_names()
    print(table_names)
    os.chdir('utils')
    print("Running all table queries....")
    pool = Pool()
    pool.map(run_table_query, table_names)
    os.chdir('..')
