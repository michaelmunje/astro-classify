from .get_all_names import get_all_names
import urllib.request
import os
import gzip
import re

get_root = os.getcwd()
gz_dir = get_root + '/galana/data/gz_tables/'

def download_tables():
    galaxy_names = get_all_names()

    for gn in galaxy_names:
        url = 'https://heasarc.gsfc.nasa.gov/FTP/heasarc/dbase/tdat_files/heasarc_' + gn + '.tdat.gz'
        urllib.request.urlretrieve(url, gz_dir + gn + '.tdat.gz')
        os.chmod(gz_dir + gn + '.tdat.gz', 0o660)

def parse_file(file_content):
    colum_names = ''
    save_index = -1
    for i,line in enumerate(file_content):
        if re.search('line[1]', line):
            print('Found the line')
            print(line[:8])
            print(i)
            exit(0)

def handle_gz_tables():
    temp_files = os.listdir(gz_dir)
    gz_files = []
    for tf in temp_files:
        if tf.endswith('.tdat.gz'):
            gz_files.append(tf)

    for gf in gz_files:
        with gzip.open(gz_dir + gf, mode='rt') as f:
            file_content = f.read()
            file_content = file_content.split('\n')
            
            parse_file(file_content)
                

                