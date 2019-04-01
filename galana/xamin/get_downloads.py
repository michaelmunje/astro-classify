from .get_all_names import get_all_names
import urllib.request
import os
import gzip

get_root = os.getcwd()
gz_dir = get_root + '/galana/data/gz_tables/'

def download_tables():
    galaxy_names = get_all_names()

    for gn in galaxy_names:
        url = 'https://heasarc.gsfc.nasa.gov/FTP/heasarc/dbase/tdat_files/heasarc_' + gn + '.tdat.gz'
        urllib.request.urlretrieve(url, gz_dir + gn + '.tdat.gz')
        os.chmod(gz_dir + gn + '.tdat.gz', 0o660)
    
    

# def parse_tables():
#     gz_files = 