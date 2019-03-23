import os
import subprocess


root_dir = os.getcwd()
xamin_script_loc = root_dir + "/utils/get_all_tables.sh"


def get_script_output(script_location):
    process = subprocess.Popen(script_location, stdout=subprocess.PIPE)
    out, err = process.communicate()
    table_list = out.decode("utf-8").split('\n')[1:-5]
    clean_list = list((table_name.strip() for table_name in table_list))
    return clean_list


def get_all_tables():
    os.chdir('utils')
    return get_script_output(xamin_script_loc)