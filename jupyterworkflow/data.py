import os
from urllib.request import urlretrieve
import pandas as pd
URL="https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"
def get_fremont_data(filename='Fremont.csv', url = URL, force_download=False):
    if not force_download or os.path.exist(filename):
        urlretrieve(url, 'Fremont.csv')

    data = pd.read_csv('Fremont.csv', index_col='Date', parse_dates=True)
    return data
