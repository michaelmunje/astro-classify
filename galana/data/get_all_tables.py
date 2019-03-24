import os
from multiprocessing import Pool
from ..data import get_all_tables_names
from ..helpers import get_inline_script_output

root_dir = os.getcwd()
raw_data_dir = root_dir + '/data/mine/raw'
abs_raw_data_path = os.path.abspath(raw_data_dir)


def run_table_query(table_name):
    print("Running query for " + table_name)
    filepath = abs_raw_data_path + '/' + table_name + ".txt"
    print("File to save to: " + filepath)
    command = "java -jar xamin.jar table=" + table_name + " fields=Standard Format=aligned > '" + abs_raw_data_path \
              + '/' + table_name + ".txt'"
    filepath = abs_raw_data_path + '/' + table_name + ".txt"
    with open(filepath, "w") as text_file:
        text_file.write(get_inline_script_output(command))


def get_all_tables():
    print("Retrieving all table names...")
    table_names = get_all_tables_names()
    print(table_names)
    os.chdir('utils')
    print("Running all table queries....")
    pool = Pool()
    pool.map(run_table_query, table_names)
    os.chdir('..')
