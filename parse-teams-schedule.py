#!/usr/bin/python

from bs4 import BeautifulSoup

html_doc = "nfl-teams-schedules.html"

doc = BeautifulSoup(open(html_doc), 'html.parser')

schedule_team_header = []

# get season year
year = doc.find("option", selected='selected')
#print year.text

# get season type
season_type = doc.select_one("tr > td:nth-of-type(1)")
#print season_type.text.strip()

# get schedule header
schedule_header = doc.select("tr.thd2 > td")
#for i in schedule_header:
#	print i.text.strip()

schedule_team_header.append("Year")
schedule_team_header.append("Season Type")
for i in schedule_header:
	#print i.text.strip()
	schedule_team_header.append(str(i.text.strip()))

print ",".join(schedule_team_header)


year = doc.find("option", selected='selected')
print year.text.strip()

season = doc.find('td', colspan=11)
print season.text.strip()

game_week = doc.select('table.data-table1 tr.tbdy1 td.first')
#print game_week

game_date = doc.select('table.data-table1 tr.tbdy1 td.first + td')
#for i in game_date:
#	print i.text.strip()

game_matchup_start = doc.select('table.data-table1 tr.tbdy1 td a')

#for idx, val in enumerate(game_matchup_start):

	#print "current: " + str(idx) + ":" + unicode(val.text.strip())
	#if( idx%6 == 0 or idx == 0):
		#print "=========================="
		#print "Visitors: " + unicode(val.text.strip())
	#if( idx%6 == 1 or idx == 1 ):
		#print "Home: " + unicode(val.text.strip())
		#print "==========================="

game_scheduled_time = doc.select('table.data-table1 tr.tbdy1 td a')

#for idx, val in enumerate(game_scheduled_time):
	#print "current: " + str(idx) + ":" + unicode(val.text.strip())
	#if( idx % 6 == 2 or idx == 2):
		#print "Time(ET): " + unicode(val.text.strip())

game_attendence = doc.select('table.data-table1 tr.tbdy1 td')

#for idx, val in enumerate(game_attendence):
#	#print "current: " + str(idx) + ":" + unicode(val.text.strip())
#	if "," in unicode(val.text.strip()):
#	  if( idx % 8 == 4 or idx == 4 or idx % 8 == 7):
#	    print val.text.strip()

game_top_passer = doc.select("table.data-table1 tr.tbdy1 td a")

#for idx, val in enumerate(game_top_passer):
#	if(len(val.text.strip()) > 3 and val.text.strip() != "Final"):
#	  print val.text.strip()

#game_top_rusher = doc.select("top_rusher")
game_top_rusher = doc.select("table.data-table1 tr.tbdy1 td a")

#game_top_receiver = doc.select("top_receiver")
game_top_receiver = doc.select("table.data-table1 tr.tbdy1 td a")

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