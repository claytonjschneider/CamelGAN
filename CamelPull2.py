import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import webbrowser, time, sys, requests, os, bs4

import pprint


site = 'https://www.opensea.io/assets/camelsnft?search[resultModel]=ASSETS&search[sortAscending]=false'
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get(site)

browser.implicitly_wait(10)

req = urllib.request.Request(site, headers=hdr)

html = urlopen(req)
bs = BeautifulSoup(html, 'html5lib')

images = bs.findAll('img', {'class': 'Image--image'})
for img in images:
    # if img.has_attr('src'):
    print(img)
