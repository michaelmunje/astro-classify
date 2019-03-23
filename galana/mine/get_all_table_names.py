import os
import subprocess


root_dir = os.getcwd()
xamin_script_loc = root_dir + "/utils/get_all_tables.sh"


def get_script_output(script_location):
    process = subprocess.Popen(script_location, stdout=subprocess.PIPE)
    out, err = process.communicate()
    return out.decode("utf-8")


def get_all_tables():
    return get_script_output(xamin_script_loc)