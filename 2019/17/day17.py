import os
import itertools
from aoc.IntcodeComputer import IntcodeComputer
from aoc.Utils import drawPanel
import colorama
from operator import add

SCAFFOLD = 35
OPENSPACE = 46
NEWLINE = 10

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

COLORS =  {
    SCAFFOLD : colorama.Fore.BLUE,
    OPENSPACE: colorama.Fore.BLACK,
    0 : colorama.Fore.GREEN
}

def getCurrentViewGrid(view):
    panel = {}
    col = 0
    row = 0
    for field in view:
        if field == NEWLINE:
            row += 1
            col = 0
        else:
            panel[(col, row)] = field
            col += 1
    return panel

def getAdjacentPositions(position):
    adjacents = []
    for direction in DIRECTIONS:
        adjacents.append(tuple(map(add, position, direction)))
    return adjacents

def getInterSections(view):
    intersections = []
    scaffolds = list(filter(lambda v: view[v] == SCAFFOLD, view))
    for scaffold in scaffolds:
        adjacents = getAdjacentPositions(scaffold)
        if all(adjacent in scaffolds for adjacent in adjacents):
            intersections.append(scaffold)
    return intersections

def part1(program):
    vacuumRobot = IntcodeComputer(program, [])
    vacuumRobot.run()
    currentView = vacuumRobot.output
    view = getCurrentViewGrid(currentView)
    drawPanel(view, COLORS)
    intersections = getInterSections(view)
    return sum(list(map(lambda i: i[0] * i[1], intersections)))

def part2(program):
    mainroutine = 'A,A,B,C,C,A,B,C,A,B'
    funA = 'L,12,L,12,R,12'
    funB = 'L,8,L,8,R,12,L,8,L,8'
    funC = 'L,10,R,8,R,12'
    video = 'n'

    vacuumRobot = IntcodeComputer(program, [])
    vacuumRobot.addAsciiArguments(mainroutine)
    vacuumRobot.addAsciiArguments(funA)
    vacuumRobot.addAsciiArguments(funB)
    vacuumRobot.addAsciiArguments(funC)
    vacuumRobot.addAsciiArguments(video)

    while not vacuumRobot.terminated:
        vacuumRobot.run()
    
    return vacuumRobot.getLastOutput()


# Open input files and get intcodeprogram
script_dir = os.path.dirname(__file__)
inputFile = open(script_dir + "/input", "r")
line = inputFile.readline()
program = line.split(",")

alignementParameter = part1(program.copy())
print(alignementParameter)

program2 = program.copy()
program2[0] = 2
spaceDust = part2(program2)
print(spaceDust)
