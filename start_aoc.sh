#!/bin/bash 
# Create the folder and file structure for a new year of advent of code
# Create the folder for the year, create a folder for each day and create files dayxx.py and puzzle_input 

Help()
{
    echo "Create the folder/file structure for a year of Advent of Code."
    echo 
    echo "Syntax: start_aoc.sh year [h]"
    echo 
    echo "Creates the folder structure advent-of-code/year/"
    echo "Creates a folder for each day: dayxx/"
    echo "Adds 2 files to each folder: "
    echo "    dayxx.py"
    echo "    puzzle_input"
    echo
    echo "Also adds the following comments to dayxx.py"
    echo "    # Advent of Code - year"
    echo "    ## Day dayxx"
}

while getopts ":h" option; do
    case $option in
    h)
        Help
        exit;;
    \?)
        echo "Error: Invalid option"
        exit;;
    esac
done

year=$1;
cd ~/Documents/advent-of-code/

for i in {1..9}; 
do
mkdir -p $year/day0$i;
touch $year/day0$i/day0$i.py 
echo "# Advent of Code - $year" >> $year/day0$i/day0$i.py 
echo "## Day $i" >> $year/day0$i/day0$i.py 
echo "
with open('puzzle_input') as file:
# with open('test_input') as file:
    lines = file.readlines()" >> $year/day0$i/day0$i.py 
touch $year/day0$i/puzzle_input
touch $year/day0$i/test_input
done

for i in {10..25};
do
mkdir -p $year/day$i;
touch $year/day$i/day$i.py 
echo "# Advent of Code - $year" >> $year/day$i/day$i.py 
echo "## Day $i" >> $year/day$i/day$i.py 
echo "
with open('puzzle_input') as file:
# with open('test_input') as file:
    lines = file.readlines()" >> $year/day$i/day$i.py 
touch $year/day$i/puzzle_input
touch $year/day$i/test_input
done

echo "Created folder/file structure for Advent of Code $year"
echo "Have fun!"