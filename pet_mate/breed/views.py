# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from urllib2 import urlopen

from django.shortcuts import render

from bs4 import BeautifulSoup
# Create your views here.
def scrap_breed(requests):
    url = 'http://dogtime.com/dog-breeds'
    site = urlopen(url).read()
    soup = BeautifulSoup(site, 'html.parser')


    links = soup.find_all('a', attrs={'class':'post-title'})

    for a in links:
        description_url = a['href']
        breed_name = a.string

        site = urlopen(description_url)
        soup = BeautifulSoup(site, 'html.parser')
        # description = soup.find_all('div', attrs={'class', 'category-article-main'})[0]
        description = soup.find_all('header')[1].p
        thumbnail = soup.find_all('img')[1]['src']

        print(thumbnail)
        print('')
