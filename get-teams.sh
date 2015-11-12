#!/bin/sh

baseUrl="http://www.nfl.com/standings?category=league&season=2015-REG&split=Overall"
userAgent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36"

#YYYY-REG, YYYY-PRE
SEASONS=( REG PRE )

#Overall, Home, Road, Division, AFC, NFC, Grass, Turf, Indoors, Outdoors, Overtime
# Pages with 18 columns: Grass, Home, Indoors, Outdoors, Overall, Overtime, Road, Turf
SPLITS_18=( "Overall" "Home" "Road" "Grass" "Turf" "Indoors" "Outdoors" "Overtime" )

# Pages with 13 columnsL: AFC, NFC, Division
SPLITS_13=( "AFC" "NFC" "Division")

outputFile="target/nfl-teams.html"

echo "Calling ${baseUrl}..."

echo ${SEASONS[@]}
echo ${SPLITS_18[@]}

for year in {2002..2015}
do
    for season in ${SEASONS[@]}
    do
        for split in ${SPLITS_18[@]}
        do
            curl -A "$userAgent" "http://www.nfl.com/standings?category=div&season=$year-$season&split=$split" -o "target/nfl-teams-$year-$season-$split.html"
            sleep $[ ( $RANDOM % 10 )  + 1 ]s
            echo "Saving to target/nfl-teams-$year-$season-$split.html"
        done
    done
done

