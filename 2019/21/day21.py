import os
import itertools
from aoc.IntcodeComputer import IntcodeComputer
from aoc.Utils import drawAsciiPanel
import colorama

HULL = ord('#')
OPENSPACE = ord('.')
SPRINGDROID = ord('@')
NEWLINE = 10

COLORS =  {
    str(HULL) : colorama.Fore.GREEN,
    str(SPRINGDROID): colorama.Fore.YELLOW,
    str(OPENSPACE): colorama.Fore.BLACK,
    ' ' : colorama.Fore.GREEN
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

def part1(program):
    instructions = []

    # Jump over 3 tile wide hole
    instructions.append('NOT A J')
    instructions.append('NOT B T')
    instructions.append('AND T J')
    instructions.append('NOT C T')
    instructions.append('AND T J')
    instructions.append('AND D J')

    instructions.append('NOT C T')
    instructions.append('AND D T')
    instructions.append('OR T J')
    instructions.append('NOT A T')
    instructions.append('AND D T')
    instructions.append('OR T J')
    
    instructions.append('WALK')

    computer = IntcodeComputer(program, [])
    for instruction in instructions:
        if instruction != '':
            computer.addAsciiArguments(instruction)
    computer.run()

    lastMoments = getCurrentViewGrid(computer.output)
    drawAsciiPanel(lastMoments)

def part2(program):
    instructions = []

    # Jump if one of the next 3 tiles is empty
    instructions.append('NOT A J')
    instructions.append('NOT B T')
    instructions.append('OR T J')
    instructions.append('NOT C T')
    instructions.append('OR T J')
    # but not too early we need a valid jump afterwards
    instructions.append('NOT E T')
    instructions.append('NOT T T')
    instructions.append('OR H T')
    instructions.append('AND T J')
    # land save
    instructions.append('AND D J')
    # run
    instructions.append('RUN')
    
    computer = IntcodeComputer(program, [])
    for instruction in instructions:
        if instruction != '':
            computer.addAsciiArguments(instruction)
    computer.run()

    lastMoments = getCurrentViewGrid(computer.output)
    drawAsciiPanel(lastMoments)

# Open input files and get intcodeprogram
script_dir = os.path.dirname(__file__)
inputFile = open(script_dir + "/input", "r")
line = inputFile.readline()
program = line.split(",")

part1(program.copy())
part2(program.copy())