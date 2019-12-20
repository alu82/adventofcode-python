import os
from string import ascii_uppercase as UPPER
import math
from operator import add

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

PASSAGE = '.'
WALL = '#'

class Portal:

    def __init__(self, pos1, pos2):
        self.pos1 = pos1
        self.pos2 = pos2


class Dijkstra:

    def __init__(self, nodes):
        self.distance = {}
        self.pred = {}
        self.done = {}
        for node in nodes:
            self.distance[node] = math.inf
            self.pred[node] = None

    def shortest(self, start, end):
        pass

def getNeighbors(position):
    adjacents = []
    for direction in DIRECTIONS:
        adjacents.append(tuple(map(add, position, direction)))
    return adjacents

def getPassageTile(maze, neighbors):
    for neighbor in neighbors:
        tile = maze.get(neighbor, WALL)
        if tile == PASSAGE:
            return neighbor
    return None

def getLetterTile(maze, neighbors):
    for neighbor in neighbors:
        tile = maze.get(neighbor, WALL)
        if tile in UPPER:
            return neighbor
    return None


def getMaze(input):
    maze = {}
    col = 0
    row = 0

    for line in input:
        for char in line:
            maze[(col, row)] = char
            col += 1
        row += 1
        col = 0
    return maze

def getPortals(maze):
    letters = dict(filter(lambda item: item[1] in UPPER, maze.items()))
    portals = {}
    for pos, letter in letters.items():
        neighbors = getNeighbors(pos)
        passageTile = getPassageTile(maze, neighbors)
        letterTile = getLetterTile(maze, neighbors)
        if passageTile is not None and letterTile is not None:
            diff = letterTile[0] - pos[0] + letterTile[1] - pos[1]
            if diff < 0:
                portalName = maze[letterTile] + letter
            else:
                portalName = letter + maze[letterTile]
            portalTiles = portals.get(portalName, [])
            portalTiles.append(passageTile)
            portals[portalName] = portalTiles
    return portals
    
# Open input files and get intcodeprogram
script_dir = os.path.dirname(__file__)
inputFile = open(script_dir + "/input", "r")

maze = getMaze(inputFile)
getPortals(maze)

