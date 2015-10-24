#!/bin/sh

baseUrl="http://www.nfl.com/standings?category=league&season=2015-REG&split=Overall"

#YYYY-REG, YYYY-PRE
SEASONS=( REG PRE )

#Overall, Home, Road, Division, AFC, NFC, Grass, Turf, Indoors, Outdoors, Overtime
SPLITS=( "Overall" "Home" "Road" "Division" "AFC" "NFC" "Grass" "Turf" "Indoors" "Outdoors" "Overtime" )

outputFile="target/nfl-teams.html"

echo "Calling ${baseUrl}..."

echo ${SEASONS[@]}
echo ${SPLITS[@]}

for year in {2000..2015}
do
    for season in ${SEASONS[@]}
    do
        for split in ${SPLITS[@]}
        do
            curl -v "http://www.nfl.com/standings?category=div&season=$year-$season&split=$split" -o "target/nfl-teams-$year-$season-$split.html"
            sleep $[ ( $RANDOM % 10 )  + 1 ]s
        done
    done
done

echo "Saving to ${outputFile}"
