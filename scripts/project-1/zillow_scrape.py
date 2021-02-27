import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import numpy as np
import pandas as pd
import regex as re
import requests
import lxml
from lxml.html.soupparser import fromstring
import prettify
import numbers
import htmltext

def yummy(soup, main_df):
    df = pd.DataFrame()
    for i in soup:
        address = soup.find_all(class_='list-card-addr')
        price = list(soup.find_all(class_='list-card-price'))
        beds = list(soup.find_all("ul", class_="list-card-details"))
        link = soup.find_all(class_='list-card-link')

        # create dataframe columns out of variables
        df['prices'] = price
        df['address'] = address
        df['beds'] = beds

    # create empty url list
    urls = []

    # loop through url, pull the href and strip out the address tag
    for link in soup.find_all("article"):
        href = link.find('a', class_="list-card-link")
        addresses = href.find('address')
        addresses.extract()
        urls.append(href)

    # import urls into a links column
    df['links'] = urls
    df['links'] = df['links'].astype('str')

    # remove html tags
    df['links'] = df['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
    df['links'] = df['links'].replace('" tabindex="0"></a>', ' ', regex=True)

    #append to main df
    return main_df.append(df, ignore_index=True)

# set some display settings for notebooks
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# add headers in case you use chromedriver (captchas are no fun); namely used for chromedriver
req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

# create url variables for each zillow page
with requests.Session() as s:
    city = 'austin/'  # *****change this city to what you want!!!!*****

    urls = ['https://www.zillow.com/homes/for_sale/' + city]
    urls += ['https://www.zillow.com/homes/for_sale/' + city + '/' + str(i) + "_p/" for i in range(2,12)]

    url_links = [s.get(url, headers=req_headers) for url in urls]

# add contents of urls to soup variable from each url
page_links = [BeautifulSoup(r.content, 'html.parser') for r in url_links]

df = pd.DataFrame()
for soup in page_links:
    df = yummy(soup, df)

# convert columns to str
df['prices'] = df['prices'].astype('str')
df['address'] = df['address'].astype('str')
df['beds'] = df['beds'].astype('str')

# remove html tags
df['prices'] = df['prices'].replace('<div class="list-card-price">', ' ', regex=True)
df['address'] = df['address'].replace('<address class="list-card-addr">', ' ', regex=True)
df['prices'] = df['prices'].replace('</div>', ' ', regex=True)
df['address'] = df['address'].replace('</address>', ' ', regex=True)
df['prices'] = df['prices'].str.replace(r'\D', '')

# remove half of price
prices_copy = df['prices'].copy()
for index, value in prices_copy.items():
    df['prices'][index] = df['prices'][index][0:int(len(df['prices'][index])/2)]

# remove html tags from beds column
df['beds'] = df.beds.replace('<ul class="list-card-details"><li class="">', ' ', regex=True)
df['beds'] = df['beds'].replace('<abbr class="list-card-label"> <!-- -->bd</abbr></li><li class="">', ' ', regex=True)
df['beds'] = df['beds'].replace('<abbr class="list-card-label"> <!-- -->bds</abbr></li><li class="">', ' ', regex=True)
df['beds'] = df['beds'].replace('<abbr class="list-card-label"> <!-- -->ba</abbr></li><li class="">', ' ', regex=True)
df['beds'] = df['beds'].replace('<abbr class="list-card-label"> <!-- -->sqft</abbr></li><li class="list-card-statusText">', ' ', regex=True)

df[['no_beds']] = df.beds.str.slice(start = 0, stop = 2)
df[['baths']] = df.beds.str.slice(start = 2, stop = 4)
df[['sqft']] = df.beds.str.slice(start = 4, stop = 10)

df['sqft'] = df['sqft'].replace('-','', regex=True)

# remove commas from sq_feet and convert to float
df.replace(',', '', regex=True, inplace=True)

# drop nulls
df = df[(df['prices'] != '') & (df['prices'] != ' ')]

# convert column to float
df['prices'] = df['prices'].astype('float')
# d['sq_feet'] = df['sq_feet'].astype('float')

# remove spaces from link column
df['links'] = df.links.str.replace(' ', '')

print('The column datatypes are:')
print(df.dtypes)
print('The dataframe shape is:', df.shape)

# rearrange the columns
df1 = df[['prices', 'address', 'no_beds', 'baths', 'sqft']]

df1.to_csv('out.csv', index=False)