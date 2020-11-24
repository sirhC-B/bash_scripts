#! /usr/bin/python

import json
import urllib.request

url = "https://blockchain.info/ticker"

rawdata = urllib.request.urlopen(url)

data = rawdata.read()
data = data[21:28]

print(data.decode("utf-8") + " USD")
