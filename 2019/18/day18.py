import os
import colorama
from aoc.Utils import drawMixPanel

COLORS =  {
    '#' : colorama.Fore.BLUE,
    '@' : colorama.Fore.GREEN
}

def getDistance(posA, posB, area):
    distance = 0
    

    return distance


def getArea(input):
    panel = {}
    col = 0
    row = 0

    for line in input:
        for char in line.strip():
            panel[(col, row)] = char
            col += 1
        row += 1
        col = 0
    return panel


def part1(input):
    area = getArea(input)
    drawMixPanel(area, COLORS)


# Open input files and get intcodeprogram
script_dir = os.path.dirname(__file__)
inputFile = open(script_dir + "/input", "r")

part1(inputFile)