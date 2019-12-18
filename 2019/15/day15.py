import os
import itertools
from aoc.IntcodeComputer import IntcodeComputer
from aoc.Utils import drawPanel
import colorama
from random import randrange

WALL = 0
MOVED = 1
FOUND = 2
UNKNOWN = 99
DROID = 'repair droid'
OXYGEN = 98


NORTH = 1
SOUTH =  2
WEST = 3
EAST = 4

colors = {
    UNKNOWN: colorama.Fore.BLACK,
    WALL: colorama.Fore.BLUE,
    DROID: colorama.Fore.YELLOW,
    MOVED: colorama.Fore.GREEN,
    FOUND: colorama.Fore.RED,
    OXYGEN: colorama.Fore.WHITE
}

movements = {
    NORTH: (0,-1),
    SOUTH: (0,1),
    WEST: (-1,0),
    EAST: (1,0)
}

class Pathfinder:
    BACK = 0
    EXPLORE = 1

    def __init__(self):
        self.path = set([])

    def getNextMove(self, droidPosition, path, area):
        nextMoves = []
        self.path.add(droidPosition)

        nPos = addPos(droidPosition, movements[NORTH])
        sPos = addPos(droidPosition, movements[SOUTH])
        wPos = addPos(droidPosition, movements[WEST])
        ePos = addPos(droidPosition, movements[EAST])

        northPos = area.get(nPos, UNKNOWN)
        southPos = area.get(sPos, UNKNOWN)
        westPos = area.get(wPos, UNKNOWN)
        eastPos = area.get(ePos, UNKNOWN)

        if northPos == UNKNOWN:
            nextMoves.append(NORTH)
        if southPos == UNKNOWN:
            nextMoves.append(SOUTH)
        if westPos == UNKNOWN:
            nextMoves.append(WEST)
        if eastPos == UNKNOWN:
            nextMoves.append(EAST)
        
        # if there is no unknown option go forward on an existing path if possible, maybe there will be something unknown there
        if len(nextMoves) == 0:
            if self.isPossibleNextMove(nPos, northPos):
                nextMoves.append(NORTH)
            if self.isPossibleNextMove(sPos, southPos):
                nextMoves.append(SOUTH)
            if self.isPossibleNextMove(wPos, westPos):
                nextMoves.append(WEST)
            if self.isPossibleNextMove(ePos, eastPos):
                nextMoves.append(EAST)

        if len(nextMoves) > 0:
            return nextMoves[randrange(len(nextMoves))]
        else:
            return None
    
    def isPossibleNextMove(self, pos, posInfo):
        return pos not in self.path and (posInfo == MOVED or posInfo == DROID or posInfo == FOUND)

def addPos(position1, position2):
    return (position1[0] + position2[0], position1[1] + position2[1])

def findPath(program, area, maxLength):
    droidControl = IntcodeComputer(program, [])
    droidPosition = (0,0)
    area[droidPosition] = DROID
    pathFinder = Pathfinder()
    path = []
    shortestPath = maxLength
    while len(path) <= maxLength:
        nextMovement = pathFinder.getNextMove(droidPosition, path, area)
        if(nextMovement is not None):
            droidControl.addArgument(nextMovement)
            droidControl.run()
            output = droidControl.getLastOutput()
            headingPosition = addPos(droidPosition, movements[nextMovement])
            if output == WALL:
                area[headingPosition] = WALL
            elif output == MOVED:
                area[droidPosition] = MOVED
                droidPosition = headingPosition
                area[droidPosition] = DROID
                path.append(nextMovement)
            elif output == FOUND:
                area[droidPosition] = MOVED
                droidPosition = headingPosition
                area[droidPosition] = FOUND
                path.append(nextMovement)
                if len(path) < shortestPath:
                    shortestPath = len(path)
        else:
            break
    return (shortestPath, area)

def getMap(program):
    area = {}
    for i in range(50000): # it will prbably work with fewer iterations
        area = findPath(program.copy(), area, 2000)[1]
        if(i%1000==0):
            print(i)
    return area

def canFillWithOxygen(area, position):
    return area[position] != OXYGEN and (area[position] ==  MOVED or area[position] == DROID)

def fillWithOxygen(area):
    foundLocation = list(filter(lambda k: area[k] == FOUND, area.keys()))[0]
    area[foundLocation] = OXYGEN
    minutes = 0
    fullWithOxygen = False
    while not fullWithOxygen:
        oxygenLocations = list(filter(lambda k: area[k] == FOUND or area[k] == OXYGEN, area.keys()))
        fullWithOxygen = True
        for location in oxygenLocations:
            adjacentPositions = [addPos(location, movements[NORTH]), addPos(location, movements[SOUTH]), addPos(location, movements[WEST]), addPos(location, movements[EAST])]
            for adjacent in adjacentPositions:
                if adjacent in area:
                    if canFillWithOxygen(area, adjacent):
                        area[adjacent] = OXYGEN
                        fullWithOxygen = False
        if not fullWithOxygen:
            minutes += 1
    drawPanel(area, colors, UNKNOWN)
    return minutes


def part1(program):
    maxLength = 1000
    for _ in range(3000):
        length = findPath(program.copy(), {}, maxLength)[0]
        if(length < maxLength):
            maxLength = length
            print(maxLength)

def part2(program):
    area = getMap(program.copy())
    minutes = fillWithOxygen(area)
    print(minutes)

# Open input files and get intcodeprogram 
script_dir = os.path.dirname(__file__)
inputFile = open(script_dir + "/input", "r")
line = inputFile.readline()
program = line.split(",")

part1(program.copy())
part2(program.copy())