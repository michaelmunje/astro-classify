import os
from .helpers import get_script_output


root_dir = os.getcwd()
xamin_script_loc = root_dir + "/utils/get_all_tables.sh"


def get_all_names():
    os.chdir('utils')
    clean_list = list()
    try:
        table_names = get_script_output(xamin_script_loc).split('\n')[1:-5]
        clean_list = list((table_name.strip() for table_name in table_names))
        os.chdir('..')
    except:
        print("Bad connection. Attempting again...")
        os.chdir('..')
        return get_all_names()
    if len(clean_list) == 0:
        return get_all_names()
    return clean_list
