#!/usr/bin/python
from bs4 import BeautifulSoup

doc  = BeautifulSoup(open("nfl-teams.html"), "html.parser")

print doc
