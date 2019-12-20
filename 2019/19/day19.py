import os
from aoc.IntcodeComputer import IntcodeComputer
from aoc.Utils import drawMixPanel
from collections import deque

PULLED = 1

def part1(program):
    beamArea = {}

    for col in range(50):
        for row in range(50):
            droneSystem = IntcodeComputer(program.copy(), [col, row])
            droneSystem.run()
            beamArea[(col, row)] = droneSystem.getLastOutput()
    
    drawMixPanel(beamArea)
    beamerPoints = list(filter(lambda pos: beamArea[pos] == PULLED, beamArea))
    return len(beamerPoints)

def part2(program):

    move = deque(['XY', 'X', 'Y'])
    adjust = (0,0)
    off = 99
    start = (0, 2000) # works for my input, there should be a better solution to find a suitable startposition
    while not isPulled(program, start):
        start = (start[0] + 99, start[1])
    
    lastSuccess = []
    found = False
    while not found:
        found = True
        start = (start[0] + adjust[0], start[1] + adjust[1])
        rightEdge = (start[0] + off, start[1])
        bottomEdge = (start[0], start[1] + off)

        rightPulled = isPulled(program, rightEdge)
        bottomPulled = isPulled(program, bottomEdge)

        if rightPulled and bottomPulled:
            found = False
            lastSuccess.append(start)
            if move[0] == 'X':
                adjust = (-1,0)
            elif move[0] == 'XY':
                adjust = (-1, -1)
            else:
                adjust = (0,-1)
        elif not rightPulled or not bottomPulled: # if something goes wrong
            found = False
            adjust = (adjust[0]*-1, adjust[1]*-1) # revert last move
            move.rotate() # try another dimension

        if len(lastSuccess) > 3:
            if lastSuccess[-1] == lastSuccess[-2] == lastSuccess[-3] == lastSuccess[-4]:
                found = True
            lastSuccess = lastSuccess[-4:]

    return start[0]*10000 + start[1]


def isPulled(program, position):
    droneSystem = IntcodeComputer(program.copy(), [position[0], position[1]])
    droneSystem.run()
    return droneSystem.getLastOutput() == PULLED


# Open input files and get intcodeprogram
script_dir = os.path.dirname(__file__)
inputFile = open(script_dir + "/input", "r")
line = inputFile.readline()
program = line.split(",")

print(part1(program.copy()))
print(part2(program.copy()))