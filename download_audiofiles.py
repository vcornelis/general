import urllib2 as ul2
import requests as rq
import pandas as pd
import numpy as np
import os
import re
from bs4 import BeautifulSoup as bs 

os.chdir("/Users/cornelisvletter/desktop")

#Studies van 2015
link = "http://hetlichtdeslevens.nl/studies/audio.html"
website = rq.get(link)

soup = bs(website.content, "html.parser")

findFiles = soup.find_all("h5")
findLinks = soup.find_all("audio")
#findDate
#findContent

preekTitels = []

for titles in findFiles:
	preekTitels.append(titles.text)

preekLinks = []

for i in range(0,len(findLinks)):
	temp = findLinks[i]
	temp = temp["src"]
	preekLinks.append(temp)
		
data = pd.DataFrame(preekTitels)
data.columns = ['Titel']
data['Audio'] = preekLinks

data.to_csv('test.csv', sep=';', encoding='utf-8')

os.chdir("/Users/cornelisvletter/desktop/progs/personal/Preken")

i = 0
for mp3 in preekLinks:
	i += 1
	openURL = ul2.urlopen(mp3)
	filename = 'preek_2015_%s.mp3' % i
	output = open(filename, 'wb')
	output.write(openURL.read())
	output.close()

"""
#moet nog loopen over de eerdere jaren.

#Studies 2014 en eerder

years = range(2014, 2000, -1)

for year in years:
	location = '/Users/cornelisvletter/desktop/progs/personal/Preken/Jaar_%s' % year
	os.chdir(location)

	link = 'http://www.hetlichtdeslevens.nl/studies/audio%s.html' % year
	page = rq.get(link)

	soup = bs(page.content, 'html.parser')

	getLinks = soup.find_all('a')

	
for link in getLinks:
	if '.mp3' in link:
		print link.get('href')
		print link.text

"""
	
