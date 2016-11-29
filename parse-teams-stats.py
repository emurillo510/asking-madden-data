#!/usr/bin/python

from bs4 import BeautifulSoup

html_doc = "nfl-teams-stats.html"

doc = BeautifulSoup(open(html_doc), 'html.parser')

team_stats_header=[]

# gets year
year = doc.find("option", selected='selected')
print "year: " + year.text.strip()

# gets team name
team_name = doc.select("table.team-stats tr.thd2 td")[1]
print "team_name: " + team_name.text.strip()

# team stats types
team_stat_types = doc.select("tr.thd1 > td")
#print team_stat_types

# team stats 
team_stats_header_data = doc.select("table.team-stats tr.tbdy1 td.first")
#print team_stats_header
#for child in team_stats_header_data:
#  print child.text.strip()

team_stats_header.append("Year")
team_stats_header.append("Team Name")

for i in team_stats_header_data:
  team_stats_header.append(i.text.strip())


team_stats_row = []

team_stats_row.append(year.text.strip())
team_stats_row.append(team_name.text.strip())

team_stats_for = doc.select("table.team-stats tr.tbdy1 td.first + td")
for child in team_stats_for:
    #print child.text.strip()
    team_stats_row.append(child.text.strip())

#team_stats_opp = doc.select("table.team-stats tr.tbdy1 > td:nth-of-type(3)")
#for child in team_stats_opp:
#  print child.text.strip()
#  team_stats_row.append(child.text.strip())

print ",".join(team_stats_header)
print ",".join(team_stats_row)

# selector: <table class="data-table1 team-stats">
# format: [stat,colts,opp] 
# columns: 3 rows: 16
# gets team stats

team_stats = [] 
# team_stats = doc.select("tr.tbdy1 ")

# format: [Player,Att,Comp,Yds,Comp %,Yds/Att,TD,TD %,INT,INT %,Long,Sck,Sack/Lost,Rating]
# columns: 14 rows: n (unknown)
# gets passing stats
# passing_stats = doc.select("tr.thd1 > td") 

# format: [Player,Att,Yds,Yds/Att,Long,TD] 
# columns: 6 rows: n (unknown)
# gets rushing stats
# rushing_stats = doc.select("tr.thd1 > td") 

# format: [Player,Rec,Yds,Yds/Rec,Long,TD] 
# columns: 6 rows: n (unknown)
# gets receiving stats
# recv_stats = doc.select("tr.thd1 > td") 

# format: [Player,1-19 A,1-19 M,20-29 A,20-29 M,30-39 A,30-39 M,40-49 A,40-49 M,50+ A,50+ M]
# columns: 11 rows: n (unknown)
# gets field goal stats
# fg_stats = doc.select("tr.thd1 > td") 

# format: [Player,Punts,Avg,Touchbacks/g,IN 20,Long,Blck] 
# columns: 6 rows: n (unknown)
# gets punting stats
# punting_stats = doc.select("tr.thd1 > td") 

# format: [Player,Returns,FC,Yds/Ret,Long,TD]
# columns: 6 rows: n (unknown)
# gets punt return stats 
# punt_rtn_stats = doc.select("tr.thd1 > td") 

# format: [Player,Returns,Yds,Yds/Ret,Long,TD]
# columns: 6 rows: n (unknown)
# gets kick return stats
# kick_rtn_stats = doc.select("tr.thd1 > td") 


# format: [Player,Comb,Total,Assist,Sck,Fumb] 
# columns: 6 rows: n (unknown)
# defense stats
# def_stats = doc.select("tr.thd1 > td") 

# format: [Player,Int,Yds,Yds/Int,Long,TD] 
# columns: 6 rows: n (unknown)
# interception stats
# int_stats = doc.select("tr.thd1 > td") 
