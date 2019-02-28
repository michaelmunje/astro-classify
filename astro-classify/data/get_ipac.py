from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
# from selenium.webdriver.common.by import By 
# from selenium.webdriver.support.ui import WebDriverWait 
# from selenium.webdriver.support import expected_conditions as EC 
# from selenium.common.exceptions import TimeoutException

# option = webdriver.ChromeOptions()
# option.add_argument(“ — incognito”)

# url = 'https://heasarc.gsfc.nasa.gov/db-perl/W3Browse/w3table.pl?tablehead=name%3Dcgmw&Action=More+Options'

# driver = webdriver.Chrome()

# driver.implicitly_wait(30)
# driver.get(url)

file_name = 'BrowseTargets.13984.1551225386'

def extract_galaxy_names(file_name):
    file = open(file_name, 'r')
    galaxy_names = []

    for line in file.readlines()[6:]:
        s = line.split('|')[1].split('|')[0]
        s = s.rstrip()
        galaxy_names.append(s)
    
    df = pd.DataFrame(galaxy_names, columns = ['names'])
    
    return df

g_df = extract_galaxy_names(file_name)

print(g_df)


