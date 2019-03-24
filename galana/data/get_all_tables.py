from multiprocessing import Pool
import os
from data import get_all_tables_names
import subprocess
from helpers import get_inline_script_output

root_dir = os.getcwd()
data_dir = root_dir + 'data/mine/'
table_script = root_dir + "/utils/get_table.sh"


def get_all_tables():
    print("")
    os.chdir('utils')
    table_names =  get_all_tables_names()

    p = Pool()
    p.map(run_table_query, table_names)
    os.chdir('..')
    
def run_table_query(table_name):
    command = "java -jar xamin.jar table=" + table_name + " fields=Standard Format=aligned > '../data/tables/" + table_name + ".txt'"
    get_inline_script_output(command)