import numpy as np
import os

def getDirection(command):
    return command[0]

def getNumberOfSteps(command):
    return int(command[1:])

def markPanel(wireNr, panel, row, col):
    currentValue = panel[row, col]
    if currentValue == 0:
        panel[row, col] = wireNr
    elif currentValue != wireNr:
        panel[row, col] = -1


def moveWire(wireNr, panel, commands, startRow, startCol):
    currentRow = startRow
    currentCol = startCol
    for command in commands:
        direction = getDirection(command)
        steps = getNumberOfSteps(command)
        for i in range(steps):
            if direction == 'U':
                currentRow = currentRow-1
            elif direction == 'D':
                currentRow = currentRow+1
            elif direction == 'L':
                currentCol = currentCol-1
            elif direction == 'R':
                currentCol = currentCol+1
            markPanel(wireNr, panel, currentRow, currentCol)

def searchClosestCrossingDistance(panel, startRow, startCol, dimension):
    closest = 999999
    for row in range(dim):
        for col in range(dim):
            if panel[row][col] == -1:
                tmpClosest = abs(startRow-row) + abs(startCol - col)
                if(tmpClosest < closest):
                    closest = tmpClosest
    return closest

def calcStepsToPosition(panel, commands, startRow, startCol, endRow, endCol):
    totalSteps = 0
    currentRow = startRow
    currentCol = startCol
    for command in commands:
        direction = getDirection(command)
        steps = getNumberOfSteps(command)
        for i in range(steps):
            totalSteps = totalSteps +1
            if direction == 'U':
                currentRow = currentRow-1
            elif direction == 'D':
                currentRow = currentRow+1
            elif direction == 'L':
                currentCol = currentCol-1
            elif direction == 'R':
                currentCol = currentCol+1

            if currentCol == endCol and currentRow == endRow:
                return int(totalSteps)

def searchClosestIntersection(panel, startRow, startCol, dimension, commands1, commands2):
    closest = 999999
    for row in range(dim):
        for col in range(dim):
            if panel[row][col] == -1:
                print("intersection found")
                print(row)
                print(col)
                print("moving wire 1")
                wire1 = calcStepsToPosition(panel, commands1, startRow, startCol, row, col)
                print("moving wire 2")
                wire2 = calcStepsToPosition(panel, commands2, startRow, startCol, row, col)
                tmpClosest = wire1 + wire2
                if(tmpClosest < closest):
                    closest = tmpClosest

    return closest


dim = 18000
start = int(dim/2)
panel = np.empty([dim, dim], dtype=int)

for i in range(dim):
    for j in range(dim):
        panel[i][j] = 0


#moveWire(1, panel, "R2,U3".split(","), start, start)
#moveWire(1, panel, "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(","), start, start)
#moveWire(2, panel, "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(","), start, start)
#print(panel)

# Test
#commands1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(",")
#commands2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(",")

# Input
script_dir = os.path.dirname(__file__)
inputFile = open(script_dir + "/input", "r")
line = inputFile.readline()
commands1 = line.split(",")
line = inputFile.readline()
commands2 = line.split(",")

print("moving wire 1")
moveWire(1, panel, commands1, start, start)
print("moving wire 2")
moveWire(2, panel, commands2, start, start)
print("starting calculation")

# Part 1
print(searchClosestCrossingDistance(panel, start, start, dim))

# Part 2
print(searchClosestIntersection(panel, start, start, dim, commands1, commands2))

