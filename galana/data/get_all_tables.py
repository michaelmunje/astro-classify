from multiprocessing import Pool
import os
from data import get_all_tables_names
import subprocess
from helpers import get_inline_script_output

root_dir = os.getcwd()
data_dir = root_dir + '/data/mine/'


def run_table_query(table_name):
    print("Running query for " + table_name )
    print("Dir: " + os.getcwd())
    command = "java -jar xamin.jar table=" + table_name + " fields=Standard Format=aligned > '../galana/data/tables/" \
              + table_name + ".txt'"
    get_inline_script_output(command)


def get_all_tables():
    table_names = get_all_tables_names()
    os.chdir('utils')
    p = Pool()
    p.map(run_table_query, table_names)
    os.chdir('..')
