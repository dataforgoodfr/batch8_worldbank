import requests
import os
'''
Script to download dataset from https://climateknowledgeportal.worldbank.org/api/data/get-download-data
'''

# Destination
PATH = '/media/NAS-Divers/dev/datasets/WorldBank/precipitation/'

nature_of_data = ['projection', 'historical']
countries_code = ['FRA']
countries_name = ['France']

variables = ['pr']

past_time_series = ["1901-1930", "1931-1960", "1961-1990", "1901-2016", "1991-2016"]
futu_time_series = ["2020_2039", "2040_2059", "2060_2079", "2080_2099"]

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

for nature in nature_of_data:
    time_series=past_time_series if nature == 'historical' else futu_time_series
    data_type = '' if nature == 'historical' else  '/mavg'
    projection = '' if nature == 'historical' else '/rcp85'
    for period in time_series:
        country_code = 'FRA'
        country_name = 'France'
        filename = '_'.join([nature, period, country_code, country_name]) + '.csv'
        url = 'https://climateknowledgeportal.worldbank.org/api/data/get-download-data/' \
            + f'{nature}{data_type}/pr{projection}/{period}/{country_code}/{country_name}'
        destination = os.path.join(PATH, filename)
        print(url, '->', destination)

        r = requests.get(url)
        if r.status_code != 200:
            print(f'ERROR HTTP : {r.status_code} for {url}')
            continue
        if len(r.content) < 1_000:
            print(f'ERROR HTTP content too small : ', r.content)
            continue
        with open(destination, 'wb') as f:
            f.write(r.content)