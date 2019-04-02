from .get_all_names import get_all_names
from .helpers import get_inline_script_output
import os
import gzip
import re
import pandas as pd
from multiprocessing import Pool

get_root = os.getcwd()
gz_dir = get_root + '/data/mine/gz_tables/'
table_dir = get_root + '/data/mine/tables/'

def download_tables(gn):
    command = 'wget -O ' + gz_dir + gn + ".tdat.gz " + "https://heasarc.gsfc.nasa.gov/FTP/heasarc/dbase/tdat_files/heasarc_" + gn + ".tdat.gz"
    get_inline_script_output(command)

def multi_core_download():
    pool = Pool()
    galaxy_names = get_all_names()
    pool.map(download_tables, galaxy_names)

def parse_file(file_content):
    colum_names = ''
    save_index = -1
    df = pd.DataFrame()
    row_index = 0

    for i,line in enumerate(file_content):
        if re.search('line\[1\]', line):
            colum_names = line.split(' ')
            colum_names = colum_names[2:]

        if re.search('<DATA>', line):
            save_index = i
            break
    
    df = pd.DataFrame(columns=colum_names)
    for line in file_content[save_index+1:-2]:
        line_list = line.split('|')
        line_list = line_list[:-1]
        line_list = [value.strip() for value in line_list]
        line_list = [value if value != '' else 'null' for value in line_list]
        df.loc[row_index] = line_list
        row_index += 1
    
    return df

def handle_gz_tables(gf):
    with gzip.open(gz_dir + gf, mode='rt') as f:
        file_content = f.read()
        file_content = file_content.split('\n')
        df = parse_file(file_content)

        file_name = gf.split('.')
        df.to_csv(table_dir + file_name[0] + '.csv', sep=',')

def mc_gz_to_csv():
    temp_files = os.listdir(gz_dir)
    gz_files = []

    for tf in temp_files:
        if tf.endswith('.tdat.gz'):
            gz_files.append(tf)
    
    pool = Pool()
    pool.map(handle_gz_tables, gz_files)
    
                

                