#!python

# Author : Satyendra
# Date : 06-Oct-2021

#https://chaos-data.projectdiscovery.io/index.json

from urllib.request import urlopen
import requests, zipfile, io
import os
import json


print('Download Starting...')

#Extracts the zip file from URL saved in chaoes-db.txt
def downloader():
	with open('/root/celestial/chaos-db.txt', 'r') as text:
		links = text.read().splitlines()
		print("Data Extraction Starts from zip file URLs taken from chaos-db.txt")
		for url in links:
			print("Extracting data from : ",url)
			r = requests.get(url, stream=True)
			z = zipfile.ZipFile(io.BytesIO(r.content))
			z.extractall("/root/celestial/chaos-db-text")


#Below function parses the URL given fron chaos-db index file and saves URL in a file
def urlparser():
	indexjson = requests.get(url='https://chaos-data.projectdiscovery.io/index.json')
	urls = (indexjson.json())
	parsed_url = [urls['URL'] for urls in urls]
	print("index.json file is parsed")
	final_urls = ('\n'.join(parsed_url))
	print("Saving final parsed URL to chaos-db.txt file!")
	with open('chaos-db.txt', 'w') as f:
		print(final_urls, file=f)

def merger():
	cmd = ('cat *.txt>/root/celestial/all.txt')
	os.chdir("/root/celestial/chaos-db-text")
	os.system(cmd)

urlparser()

downloader()

merger()

print('Download completed!')
