import os
from helpers import get_script_output


root_dir = os.getcwd()
xamin_script_loc = root_dir + "/utils/get_all_tables.sh"


def get_all_tables_names():
    os.chdir('utils')
    table_names = get_script_output(xamin_script_loc).split('\n')[1:-5]
    clean_list = list((table_name.strip() for table_name in table_names))
    os.chdir('..')
    return clean_list
