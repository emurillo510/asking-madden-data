#!/usr/bin/python

from bs4 import BeautifulSoup

soup = BeautifulSoup("<html>data</data>", "html.parser")

print soup

