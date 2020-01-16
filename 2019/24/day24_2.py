import os
import copy
from math import pow 

BUG = "#"
EMPTY = "."
DIM = 5

class RecursiveGrid:

    def __init__(self, grid):
        self.levels = {}
        self.levels[0] = grid
        self.expandRecursiveGrid()
        
    def buildGridLevel(self):
        return [[EMPTY for _ in range(DIM)] for _ in range(DIM)]

    def isInfected(self, grid):
        infected = False
        for row in grid:
            infected = infected or (BUG in row)
        return infected
    
    def expandRecursiveGrid(self):
        minDepth = min(self.levels.keys())
        maxDepth = max(self.levels.keys())
        minLevel = self.levels[minDepth]
        maxLevel = self.levels[maxDepth]
        if self.isInfected(minLevel):
            self.levels[minDepth-1] = self.buildGridLevel()
        if self.isInfected(maxLevel):
            self.levels[maxDepth+1] = self.buildGridLevel()

    def next(self):
        nextLevels = copy.deepcopy(self.levels)
        for level in self.levels.keys():
            for row in range(DIM):
                for col in range(DIM):
                    if row != 2 or col != 2:
                        nextLevels[level][row][col] = self.calcNext(level, row, col)
        self.levels = nextLevels
        self.expandRecursiveGrid()

    def calcNext(self, level, row, col):
        adjacentBugs = self.countAdjacentBugs(level, row, col)
        value = self.getGridValue(level, row, col)
        if value == BUG and adjacentBugs != 1:
            return EMPTY
        elif value == EMPTY and (adjacentBugs == 1 or adjacentBugs == 2):
            return BUG
        return value
    
    def countAdjacentBugs(self, level, row, col):
        bugs = 0
        for aLevel, aRow, aCol in self.getAdjacentTiles(level, row, col):
            bugs += 1 if self.getGridValue(aLevel, aRow, aCol) == BUG else 0
        return bugs
    
    def getAdjacentTiles(self, level, row, col):
        adjacentTiles = []

        if row == 1 and col == 2:
            for i in range(DIM):
                adjacentTiles.append((level+1,0,i))
        if row == 2 and col == 3:
            for i in range(DIM):
                adjacentTiles.append((level+1,i,DIM-1))
        if row == 3 and col == 2:
            for i in range(DIM):
                adjacentTiles.append((level+1,DIM-1,i))
        if row == 2 and col == 1:
            for i in range(DIM):
                adjacentTiles.append((level+1,i,0))

        for cRow, cCol in [(row-1, col),(row, col+1),(row+1, col),(row, col-1)]:
            if cRow == -1:
                adjacentTiles.append((level-1,1,2))
            if cRow == DIM:
                adjacentTiles.append((level-1,3,2))
            if cCol == -1:
                adjacentTiles.append((level-1,2,1))
            if cCol == DIM:
                adjacentTiles.append((level-1,2,3))
            
            if cRow != 2 or cCol != 2:
                if cRow >= 0 and cRow < DIM:
                    if cCol >= 0 and cCol < DIM:
                        adjacentTiles.append((level, cRow, cCol))
            
        return adjacentTiles

    def getGridValue(self, level, row, col):
        value = None
        if level in self.levels:
            value = self.levels[level][row][col]
        return value
    
    def countBugs(self):
        bugs = 0
        for level in self.levels.keys():
            for row in range(DIM):
                for col in range(DIM):
                    bugs += 1 if self.getGridValue(level, row, col) == BUG else 0
        return bugs

    def toString(self):
        string = ""
        for level in sorted(self.levels.keys()):
            string += "Depth " + str(level) + ":\n"
            for row in range(DIM):
                for col in range(DIM):
                    string += self.levels[level][row][col]
                string += "\n"
        return string

def part2(grid):
    recursiveGrid = RecursiveGrid(grid)
    for _ in range(200):
        recursiveGrid.next()
    return recursiveGrid.countBugs()
    
# Open input files and get intcodeprogram
script_dir = os.path.dirname(__file__)
with open(script_dir + "/input", "r") as myInput:
    grid = [list(line.replace("\n", "")) for line in myInput.readlines()]
    print(part2(grid))
