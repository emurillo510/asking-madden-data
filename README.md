#Project: Asking Madden
Author(s): Elton Murillo
========================
Creation Date: 11-03-2015
========================
ABOUT
=====

Asking Madden is a data aggregation project which scrapes NFL.com and ESPN.com (shhhh) for teams and player statistics. This data will be used for project-oden, data visualization and helping win millions of dollars.

DOCUMENTATION
===

1. COMPATIBILITY AND REQUIREMENTS
-------

1. GNU bash, version 3.2.57(1)-release (x86_64-apple-darwin15) or Linux elton-ThinkPad-X220 4.4.0-31-generic #50-Ubuntu SMP Wed Jul 13 00:07:12 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux

2. Python 2.7.10
3. Beautiful Soup 4.4.0 
 

2. HOW TO BUILD
----------------

1. Use bash to run the shell scripts.
2. pip install beautifulsoup4.
3. For documentation, please refer to section 3.


3. FILE(S)
----------

1.  get-teams-schedules.py
   * Python script to aggregate all team schedule for season.
2.  get-teams-standings.sh
   * Shell script to aggregate all team standings for season.
3.  get-teams-stats.py
   * Python script to aggregate team stats for season.
4.  parse-teams-schedule.py
   * Python script to parse team schedules.
5.  parse-teams-standings.py 
   * Python script to parse team standings.
6.  get-player-careerstats.py
   * Shell script to aggregate all player career stats for season.
7.  get-player-combine.py
    * Shell script to aggregate all player combine stats for season.
8.  get-player-draft.py
    * Shell script to aggregate all player draft data for season.
9.  get-player-gamelogs.py
    * Shell script to aggregate all player gamelogs for season.
10. get-player-gamesplits.py
    * Shell script to aggregate all player gamesplits for season.
11. get-player-situationalstats.py
    * Shell script to aggregate all player situational stats for season.

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
* Parse Player Stats
* Test if all files are converted to CSV correctly.
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

