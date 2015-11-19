#Project: Asking Madden
Author(s): Elton Murillo
========================
Creation Date: 11-3-2015
========================
ABOUT
=====

This project is strictly educational. My main goal is that I want to become a domain expert for data regarding the NFL. It will also allow me apply the Pomdoro Technique, learn Python, and Docker.

DOCUMENTATION
===

1. COMPATIBILITY AND REQUIREMENTS
-------

1. GNU bash, version 3.2.57(1)-release (x86_64-apple-darwin15)
2. Python 2.7.10
3. Beautiful Soup 4.4.0 
 

2. HOW TO BUILD
----------------

1. use bash to run the shell scripts.
2. pip install beautifulsoup4.
3. you can run the individual scripts. Scripts description below.


3. FILE(S)
----------

1. get-teams-schedules.py
   * Python script to aggregate all team schedule for season.
2. get-teams-standings.sh
   * Shell script to aggregate all team standings for season.
3. get-teams-stats.py
   * Python script to aggregate team stats for season.
4. parse-teams-schedule.py
   * Python script to parse team schedules.
5. parse-teams-standings.py 
   * Python script to parse team standings.

4. FILE DIRECTORY
-----------------

1. / - Root folder containing scripts to aggregate for now. ( Needs clean-up later )
2. target/ - Folder where output file(s) go.

CONTACT
========
1. phone: (415) 312-0534
2. e-mail: elton.murillo@yahoo.com

TODO
===
* Parse Team Stats
* Create Pseudo Code inside get-team-stats.sh
* Create Pseudo Code inside parse-team-stats.py
* Parse Player Stats
* Get all Player links for every team for every season
* Test if all files are converted to CSV correctly.
* Mock frontend for application
* Create database schema for application

Application Flow
===

- [home]
- [search player]
- [results]
- [player page]
- [search team]
- [results]
- [team page]
- [search season]
- [results]
- [season page]

