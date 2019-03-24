import os
from helpers import get_inline_script_output


root_dir = os.getcwd()
raw_data_dir = root_dir + '/data/mine/raw'
abs_raw_data_path = os.path.abspath(raw_data_dir)


def query_to_txt(filepath, command):
    try:
        with open(filepath, "w") as text_file:
            text_file.write(get_inline_script_output(command))
    except:
        print("Failed getting data for " + '.'.split(('/'.split(filepath)[-1]))[0] + ". Trying again...")
        query_to_txt(filepath, command)


def run_table_query(table_name):
    print("Running query for " + table_name)
    filepath = abs_raw_data_path + '/' + table_name + ".txt"
    print("File to save to: " + filepath)
    command = "java -jar xamin.jar table=" + table_name + " fields=Standard Format=aligned > '" + abs_raw_data_path \
              + '/' + table_name + ".txt'"
    filepath = abs_raw_data_path + '/' + table_name + ".txt"
    query_to_txt(filepath, command)