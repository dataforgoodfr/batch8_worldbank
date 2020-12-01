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

rcp_projection = ['rcp26', 'rcp45','rcp60', 'rcp85']

"""
r20mm" class="mapRadioAR5" isannual="No" value="r20mm" variableid="27" optionname="Days with Rainfall > 20mm" varunit="Days">Number of Days with Rainfall &gt; 20mm</option>
r50mm" class="mapRadioAR5" isannual="No" value="r50mm" variableid="28" optionname="Days with Rainfall > 50mm" varunit="Days">Number of Days with Rainfall &gt; 50mm</option>
r95ptot" class="mapRadioAR5" isannual="No" value="r95ptot" variableid="29" optionname="Rainfall of Very Wet Days" varunit="Percentage">Rainfall Amount from Very Wet Days</option>
rx1day class="mapRadioAR5" isannual="No" value="rx1day" variableid="30" optionname="Maximum Daily Rainfall" varunit="mm">Largest Single Day Rainfall</option>
rx5day" class="mapRadioAR5" isannual="No" value="rx5day" variableid="33" optionname="Maximum 5-day Rainfall" varunit="mm">Largest 5-day Cumulative Rainfall</option>
rx1dayreturnlevel10" "Maximum Daily Rainfall (10-yr RL)" varunit="mm">Expected Daily Rainfall Maximum in 10 Years (10-yr Return Level)</option>
rx5dayreturnlevel10" "Maximum 5-day Rainfall (10-yr RL)" varunit="mm">Expected 5-day Cumulative Rainfall Maximum in 10 Years (10-yr Return Level)</option>
rx1dayreturnlevel25" "Maximum Daily Rainfall (25-yr RL)" varunit="mm">Expected Daily Rainfall Maximum in 25 Years (25-yr Return Level)</option>
rx5dayreturnlevel25"Expected 5-day Cumulative Rainfall Maximum in 25 Years (25-yr Return Level)</option>
rxmonthreturnlevel10" "Maximum Monthly Rainfall (10-yr RL)" varunit="mm">Expected Largest Monthly Rainfall Amount in 10 Years (10-yr Return Level)</option>
rxmonthreturnlevel25" class="mapRadioAR5" isannual="Yes" value="rxmonthreturnlevel25" variableid="37" optionname="Maximum Monthly Rainfall (25-yr RL)" varunit
"""
all_metrics = ['mavg', 'r20mm', 'r50mm', 'r95ptot', 'rx1day', 'rx5day', 'rx1dayreturnlevel10', 'rx5dayreturnlevel10', 'rx1dayreturnlevel25', 'rx5dayreturnlevel25', 'rxmonthreturnlevel10', 'rxmonthreturnlevel25']

past_time_series = ["1901-2016"]
futu_time_series = ["2020_2039", "2040_2059", "2060_2079", "2080_2099"]


#debug = True
debug = False

if debug :
    countries_code = ['FRA', 'TUV', 'AFG']
    countries_name = ['France', 'Tuvalu', 'Afganisthan']
    futu_time_series = ["2020_2039", "2060_2079"]
    all_metrics = ['mavg', 'r20mm', 'rx5dayreturnlevel10']
    rcp_projection = ['rcp26', 'rcp85']
else:
    # Read countries list
    df = pd.read_csv('../../datasets/worldbank_countries.csv')
    countries_code = df.code.to_list()
    countries_name = df.name.to_list()



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


def get_url(url, destination, country_code):
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
        
        if country_code == 'PRK':
            to_replace = bytes('Korea, Democratic People’s Republic of', 'utf-8') #
            content = content.replace(to_replace, b'Korea')
        with open(destination, 'wb') as f:
            f.write(content)
        return True
    except:
        logger.error(f'Unexpected ERROR for {url}: {sys.exc_info()[0]}')
        return False
            

nb_iter = 0
#asyncloop = asyncio.get_event_loop()
#tasks = []

print("Starting download, see download.log for infos.")

with concurrent.futures.ThreadPoolExecutor(max_workers=32) as executor:
    futures = []
    for country_code, country_name in zip(countries_code, countries_name):
        for nature in nature_of_data:
            time_series=past_time_series if nature == 'historical' else futu_time_series
            #data_type = '' if nature == 'historical' else  '/mavg'
            metrics = ['mavg'] if nature == 'historical' else all_metrics
            rcp = [''] if nature == 'historical' else rcp_projection
            for period in time_series:
                for metric in metrics:
                    for projection in rcp :
                        if metric == 'mavg':
                            metric_param = 'mavg/pr' if nature != 'historical' else 'pr'
#                        elif metric == 'pr':
#                            metric_param = ''
                        else:
                            metric_param = 'manom/' + metric
                        projection = '' if nature == 'historical' else '/' + projection
                        #projection = '/' + projection
                        nb_iter += 1
                        # Build URL
                        url = 'https://climateknowledgeportal.worldbank.org/api/data/get-download-data/' \
                            + f'{nature}/{metric_param}{projection}/{period}/{country_code}/{urllib.parse.quote_plus(country_name)}'
                            #+ f'{nature}{data_type}/{metric_param}{projection}/{period}/{country_code}/{urllib.parse.quote_plus(country_name)}'
                        # build destination name
                        filename = '_'.join([nature, period, country_code, projection, metric]) + '.csv'
                        filename = filename.replace('/', '')
                        destination = os.path.join(PATH, filename)
                        #tasks.append(asyncloop.create_task(get_url(url, destination)))
                        futures.append(executor.submit(get_url, url=url, destination=destination, country_code=country_code))
    for future in concurrent.futures.as_completed(futures):
        #print(future.result())
        logger.debug(f'Done {future.result()}')
# for task in tasks:
#     await task

logger.info(f'Done after {nb_iter} iterations.')

# PAST :
#https://climateknowledgeportal.worldbank.org/api/data/get-download-data/historical/pr/1931-1960/AND/Andorra (OK)
# Future
# PRCP
# https://climateknowledgeportal.worldbank.org/api/data/get-download-data/projection/manom/r50mm/rcp45/2040_2059/SSD/South%20Sudan
# https://climateknowledgeportal.worldbank.org/api/data/get-download-data/projection/mavg/pr/rcp26/2020_2039/ALB/Albania  (OK)
# https://climateknowledgeportal.worldbank.org/api/data/get-download-data/projection/mavg/pr/rcp85/2060_2079/BDI/Burundi  (OK)
# 
#https://climateknowledgeportal.worldbank.org/api/data/get-download-data/projection/manom/r50mm/rcp60/2020_2039/ALB/Albania (OK)
#https://climateknowledgeportal.worldbank.org/api/data/get-download-data/historical/manom/pr/1901-2016/ZWE/Zimbabwe (404)
#https://climateknowledgeportal.worldbank.org/api/data/get-download-data/historical/mavg/pr/1901-2016/ZWE/Zimbabwe (404)
#https://climateknowledgeportal.worldbank.org/api/data/get-download-data/projection/mavg//pr//2020_2039/GAB/Gabon (404)