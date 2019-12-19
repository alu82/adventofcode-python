import os
import colorama
from aoc.Utils import drawMixPanel
from operator import add

COLORS =  {
    '#' : colorama.Fore.BLUE,
    '@' : colorama.Fore.GREEN
}

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

def getAdjacentPositions(position):
    adjacents = []
    for direction in DIRECTIONS:
        adjacents.append(tuple(map(add, position, direction)))
    return adjacents

def getEdge(a, b):
    return tuple(sorted((a, b)))

def nextStep(paths, endings):
    newEndings = set([])
    for ending in endings:
        adjacents = getAdjacentPositions(ending)
        paths.pop(ending, None)
        for adjacent in adjacents:
            if adjacent in paths:
                newEndings.add(adjacent)
    return newEndings

def getDistance(a, b, paths):
    posA = list(filter(lambda node: paths[node] == a, paths))[0]    
    posB = list(filter(lambda node: paths[node] == b, paths))[0] 

    endings = set([posA])
    drawMixPanel(paths, COLORS)

    workingPaths = paths.copy()
    distance = 0
    while posB not in endings:
        endings = nextStep(workingPaths, endings)
        distance += 1

    return distance

def getDistanceMap(paths):
    nodes = dict(filter(lambda item: item[1] != '.', paths.items()))
    print(nodes)

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
    #drawMixPanel(area, COLORS)
    paths = dict(filter(lambda item: item[1] != '#', area.items()))
    print(getDistance('B', 'g', paths))
    getDistanceMap(paths)

# Open input files and get intcodeprogram
script_dir = os.path.dirname(__file__)
inputFile = open(script_dir + "/input", "r")

part1(inputFile)