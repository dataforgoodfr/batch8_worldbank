# -*- coding: utf-8 -*-
import requests
import os, sys
import pandas as pd
import urllib.parse
import logging
#import asyncio
import concurrent.futures
from pathlib import Path
'''
Script to download dataset from https://climateknowledgeportal.worldbank.org/api/data/get-download-data
'''
DATASET_FOLDER = '../../datasets/'

# Destination
PATH = os.path.join(DATASET_FOLDER, 'precipitation/')

nature_of_data = ['projection', 'historical']

# Read countries list
df = pd.read_csv('../../datasets/worldbank_countries.csv')
countries_code = df.code.to_list()
countries_name = df.name.to_list()

variables = ['pr']

past_time_series = ["1901-2016"]
futu_time_series = ["2020_2039", "2040_2059", "2060_2079", "2080_2099"]

logger = logging.getLogger("download")
formatter = logging.Formatter("%(asctime)s -  %(name)-12s %(levelname)-8s %(message)s")
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler("download.log")
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.info(f'Starting...')
'''
Pour la construire : https://climateknowledgeportal.worldbank.org/api/data/get-download-data
/ projection/historical (2 options)
/ mavg/manom for mean/change (2 options)
/ climate variable pr/tas for precipitation/temperature (45 options in futur, 2 in past)
/ Scenario : rcp85 (4 options in futur, 0 in past)
/ period : 2080_2099 (4 options in futur, 5 in past)
/ country code (197 options)
/ country name (197 options)

https://climateknowledgeportal.worldbank.org/api/data/get-download-data
/historical/pr/1931-1960/FRA/France

https://climateknowledgeportal.worldbank.org/api/data/get-download-data
/projection/mavg/pr/rcp85/2060_2079/FRA/France

https://climateknowledgeportal.worldbank.org/api/data/get-download-data
/projection/mavg/pr/rcp85/2080-2099/FRA/France


	https://climateknowledgeportal.worldbank.org/api/data/get-download-data/projection/mavg/pr/rcp85/2060_2079/FRA/France
    https://climateknowledgeportal.worldbank.org/api/data/get-download-data/projection/mavg/pr/rcp85/2060-2079/FRA/France

'''


def get_url(url, destination):
    if Path(destination).is_file():
        logger.info(f'{destination} already exist ! No download.')
        return False
    logger.debug(f'{url} -> {destination}')
    # Retreive the content
    try:
        r = requests.get(url)
        content = r.content
        if r.status_code != 200:
            logger.error(f'ERROR HTTP : {r.status_code} for {url}')
            return False
        if len(r.content) < 1_000:
            logger.error(f'ERROR HTTP content too small : {content} for {url}')
            return False
        
        with open(destination, 'wb') as f:
            f.write(content)
        return True
    except:
        logger.error(f'Unexpected ERROR for {url}: {sys.exc_info()[0]}')
        return False
            

nb_iter = 0
#asyncloop = asyncio.get_event_loop()
#tasks = []
with concurrent.futures.ThreadPoolExecutor(max_workers=32) as executor:
    futures = []
    for country_code, country_name in zip(countries_code, countries_name):
        for nature in nature_of_data:
            time_series=past_time_series if nature == 'historical' else futu_time_series
            data_type = '' if nature == 'historical' else  '/mavg'
            projection = '' if nature == 'historical' else '/rcp85'
            for period in time_series:
                nb_iter += 1
                # Build URL
                url = 'https://climateknowledgeportal.worldbank.org/api/data/get-download-data/' \
                    + f'{nature}{data_type}/pr{projection}/{period}/{country_code}/{urllib.parse.quote_plus(country_name)}'
                # build destination name
                filename = '_'.join([nature, period, country_code]) + '.csv'
                destination = os.path.join(PATH, filename)
                #tasks.append(asyncloop.create_task(get_url(url, destination)))
                futures.append(executor.submit(get_url, url=url, destination=destination))
    for future in concurrent.futures.as_completed(futures):
        #print(future.result())
        logger.debug(f'Done {future.result()}')
# for task in tasks:
#     await task

logger.info(f'Done after {nb_iter} iterations.')
# https://climateknowledgeportal.worldbank.org/api/data/get-download-data/projection/mavg/pr/rcp85/2060_2079/BDI/Burundi