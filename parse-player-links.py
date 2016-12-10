#!/usr/bin/python
import sys
import glob
import errno
import re
from bs4 import BeautifulSoup

path = 'target/nfl-player-links-*.html'
files = glob.glob(path)
for file in files:
    doc  = BeautifulSoup(open(file), "html.parser")
    
    file_output_name = file + ".csv"
    file_output = open(file_output_name, "w")

    nfl_player_links = []
    
    #nfl_player_links_selector = doc.select('a[href*="player/"]')
    nfl_player_links_selector = doc.find_all(href=re.compile("/player/"))

    #print nfl_player_links_selector

    for i in nfl_player_links_selector:
        print i['href']
        link =  i['href']
        file_output.write(link)
        file_output.write("\n")

        file_output.close

 