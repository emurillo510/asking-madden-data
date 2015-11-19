#!/usr/bin/python

from bs4 import BeautifulSoup

html_doc = "nfl-teams-stats.html"

doc = BeautifulSoup(open(html_doc), 'html.parser')