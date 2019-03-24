import os
from multiprocessing import Pool
from .get import run_table_query
from .get_all_names import get_all_names


def get_all_tables():
    print("Retrieving all database names...")
    table_names = get_all_names()
    print(table_names)
    os.chdir('utils')
    print("Running all table queries....")
    pool = Pool()
    pool.map(run_table_query, table_names)
    os.chdir('..')
