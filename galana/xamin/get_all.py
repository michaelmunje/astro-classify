import os
from multiprocessing import Pool
from .get import run_table_query
from .get_all_names import get_all_names


def get_all_tables(is_multiprocessing=False):
    """
`   Queries all galactic tables and saves them to data/mine/raw/
    :param is_multiprocessing: Specifies to multiprocess queries
    Warning: Does not seem to be good for servers
    """
    print("Retrieving all database names...")
    table_names = get_all_names()
    print(table_names)
    os.chdir('utils')
    print("Running all table queries....")
    if is_multiprocessing:
        pool = Pool()
        pool.map(run_table_query, table_names)
    else:
        for table in table_names:
            run_table_query(table)
    os.chdir('..')
