#!/usr/bin/python
from bs4 import BeautifulSoup

doc  = BeautifulSoup(open("target/nfl-teams-2013-REG-Overall.html"), "html.parser")


nfl_afc_header = doc.select("tr.thd1.AFCcolors td")
nfl_afc_conference = doc.select("tr.thd2 > td")
nfl_afc_conference_header = doc.select("tr.thd2 td a")
nfl_teams = doc.select("tr.tbdy1 td a")
nfl_teams_stats = doc.select("tr.tbdy1 td")
nfl_teams_links = doc.select("tr.tbdy1 td a")



#nfl_nfc_header = doc.select("tr.thd1.NFCcolors td")

# print AFC conference
#print nfl_afc_header[0].string.strip()

# get NFL conferences
#for child in nfl_afc_conference:
#	if child.string:
#		print child.string

# get statistics header
#for child in nfl_afc_conference_header:
#	if child.string:
#		print child.string

# get nfl teams
#for child in nfl_afc_teams:
#	if child.string:
#		print child.string.strip()

# get nfl teams stats
#for child in nfl_teams_stats:
#	if child.string:
#		print child.string
#	else:
#		team_name = child.find('a')
#		print team_name.string.strip()

#cprint nfl_teams_stats

# get nfl team sites
#base_url="http://www.nfl.com/"
#for child in nfl_teams_links:
#	print base_url+child["href"]

#print nfl_nfc_header[0].string.strip()
