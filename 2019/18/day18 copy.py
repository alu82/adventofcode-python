import os
import colorama
from aoc.Utils import drawMixPanel
from operator import add
from string import ascii_lowercase as keys
from string import ascii_uppercase as doors
import math

YOU = '@'
PASSAGE = '.'
WALL = '#'

COLORS =  {
    WALL : colorama.Fore.BLUE,
    YOU : colorama.Fore.GREEN
}

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

class Path:

    def __init__(self, area, position, path, keys):
        self.area = area
        self.position = position
        self.path = path
        self.keys = keys
    
    def goTo(self, node):
        itemPosition = list(filter(lambda pos: self.area[pos] == node[0], self.area))[0]
        if node[0] in keys:
            self.keys.add(node[0])
        self.path.append(node)
        self.area[itemPosition] = YOU
        self.area[self.position] = PASSAGE
        self.position = itemPosition
    
    def getNextNodes(self):
        workingArea = self.area.copy()
        nextNodes = set()
        distance = 0
        starts = set([self.position])

        while len(starts) > 0:
            distance += 1
            starts = self.nextStep(workingArea, starts)
            tmpStarts = set()
            for start in starts:
                if self.area[start] in keys:
                    nextNodes.add((self.area[start], distance))
                    tmpStarts.add(start)
                if self.area[start] in doors and not self.foundKeyForDoor(self.area[start]):
                    tmpStarts.add(start)
            starts = starts - tmpStarts
        return nextNodes

    def foundKeyForDoor(self, door):
        return str.lower(door) in self.keys
            
    def nextStep(self, paths, starts):
        newStarts = set([])
        for start in starts:
            adjacents = self.getAdjacentPositions(start)
            paths.pop(start, None)
            for adjacent in adjacents:
                if adjacent in paths:
                    newStarts.add(adjacent)
        return newStarts

    def getAdjacentPositions(self, position):
        adjacents = []
        for direction in DIRECTIONS:
            adjacents.append(tuple(map(add, position, direction)))
        return adjacents

    def getPathLength(self):
        pathLength = 0
        for step in self.path:
            pathLength += step[1]
        return pathLength


class PathFinder:

    def __init__(self, area):
        self.paths = []
        self.area = dict(filter(lambda item: item[1] != WALL, area.items()))
        self.start = list(filter(lambda node: area[node] == YOU, area))[0]

    def nearestNeighbor(self):
        path = Path(self.area.copy(), self.start, [], set())
        nextNodes = path.getNextNodes()
        while len(nextNodes) > 0:
            nearest = min(nextNodes, key=lambda node:node[1])
            path.goTo(nearest)
            nextNodes = path.getNextNodes()
        return path.getPathLength()

    def findShortestPathLength(self):
        path = Path(self.area.copy(), self.start, [], set())
        self.paths.append(path)
        self.handlePath(path, self.nearestNeighbor())
        shortestPathLength = math.inf
        for p in self.paths:
            if p.getPathLength() < shortestPathLength:
                shortestPathLength = p.getPathLength()
                print(p.path)
        return shortestPathLength

    def clonePath(self, path):
        return Path(path.area.copy(), path.position, path.path.copy(), path.keys.copy())

    def handlePath(self, path, upperBound):
        if path.getPathLength() < upperBound:
            nextNodes = path.getNextNodes()
            print(path.path)
            for nextNode in nextNodes:
                newPath = self.clonePath(path)
                self.paths.append(newPath)
                newPath.goTo(nextNode)
                self.handlePath(newPath, upperBound)
            if len(nextNodes) > 0:
                self.paths.remove(path)
        else:
            self.paths.remove(path)

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
    pathFinder = PathFinder(area)
    return pathFinder.findShortestPathLength()

# Open input files and get intcodeprogram
script_dir = os.path.dirname(__file__)
inputFile = open(script_dir + "/input", "r")

print(part1(inputFile))
