#!/usr/bin/python
import json
import requests
import time
import random

import sys
import glob
import errno

from fake_useragent import UserAgent

ua = UserAgent()

baseUrl="http://www.nfl.com"
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36"
headers = {'User-Agent': user_agent}


#`doc = requests.get("http://www.nfl.com/player/jaredabbrederis/2543775/profile")

path = 'target/nfl-player-links-*.html.csv'
counter = 0

files = glob.glob(path)
for fileName in files:
   f = open(fileName, 'r')
   for line in f:
      suffix = line.rstrip('\n')
      suffix = suffix.replace('profile', 'careerstats')
      print suffix
      page = baseUrl + suffix

      doc = requests.get(page, headers=headers)
      print doc.text

      outputfilename = "target/nfl-player-careerstats-" + str(counter) + ".html"
      output = open(outputfilename,'w')
      output.write(doc.text)
      output.close
      counter += 1
      time.sleep(random.randint(1,10))
