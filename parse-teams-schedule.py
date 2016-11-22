#!/usr/bin/python

from bs4 import BeautifulSoup

html_doc = "nfl-teams-schedules.html"

doc = BeautifulSoup(open(html_doc), 'html.parser')

# get season year
year = doc.find("option", selected='selected')
print year.text

# get season type
season_type = doc.select_one("tr > td.DETcolors")
print season_type.text.strip()

# get schedule header
schedule_header = doc.select("tr.thd2 > td")
for i in schedule_header:
	print i.text.strip()

# get week_schedule
#week_schedule = doc.select("tr.tbdy1 td")
#for i in week_schedule:
#	print i.text.strip()

# get week played
# get game date
# get game time
# get game attendence
# get game top passer
# get game top rusher
# get game top receiver