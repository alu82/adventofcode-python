import os
import copy
from math import pow 

BUG = "#"
EMPTY = "."

class RecursiveGrid:

    def __init__(self, grid):
        self.levels = {}
        self.levels[0] = grid

    def biodiversity(self):
        layouts = set()
        newLayout = self
        while not newLayout.toString() in layouts:
            layouts.add(newLayout.toString())
            newLayout = newLayout.next()
        return newLayout.biodiversityRating()

    def biodiversityRating(self):
        power = 0
        rating = 0
        for tile in self.toString():
            if tile == BUG:
                rating += pow(2, power)
            power += 1
        return rating

    def toString(self):
        string = ""
        for row in range(len(self.levels[0])):
            for col in range(len(self.levels[0][row])):
                string += self.levels[0][row][col]
        return string

    def next(self):
        nextGrid = copy.deepcopy(self.levels[0])
        for row in range(len(self.levels[0])):
            for col in range(len(self.levels[0][row])):
                nextGrid[row][col] = self.calcNext(row, col)
        return RecursiveGrid(nextGrid)

    def calcNext(self, row, col):
        adjacentBugs = self.countAdjacentBugs(row, col)
        value = self.getGridValue([row, col])
        if value == BUG and adjacentBugs != 1:
            return EMPTY
        elif value == EMPTY and (adjacentBugs == 1 or adjacentBugs == 2):
            return BUG
        return value

    def countAdjacentBugs(self, row, col):
        bugs = 0
        for tile in self.getAdjacentTiles(row, col):
            bugs += 1 if self.getGridValue(tile) == BUG else 0
        return bugs

    def getAdjacentTiles(self, row, col):
        adjacentTiles = []
        tiles = [[row-1, col],[row, col+1],[row+1, col],[row, col-1]]
        for tile in tiles:
            if tile[0] >= 0 and tile[0] < len(self.levels[0]):
                if tile[1] >= 0 and tile[1] < len(self.levels[0][tile[0]]):
                    adjacentTiles.append(tile)
        return adjacentTiles

    def getGridValue(self, tile):
        return self.levels[0][tile[0]][tile[1]]

 
def part1(grid):
    recursiveGrid = RecursiveGrid(grid)
    return recursiveGrid.biodiversity()

# Open input files and get intcodeprogram
script_dir = os.path.dirname(__file__)
with open(script_dir + "/input", "r") as myInput:
    grid = [list(line.replace("\n", "")) for line in myInput.readlines()]
    print(part1(grid))
