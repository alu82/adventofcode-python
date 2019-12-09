import os
import itertools
from base.ShipComputer import ShipComputer
import time

#Part 1
def part1(program):
    computer = ShipComputer(program, [1])
    computer.run()
    print(computer.output)

# Part 2
def part2(program):
    computer = ShipComputer(program, [2])
    computer.run()
    print(computer.output)

# Run methods
script_dir = os.path.dirname(__file__)
inputFile = open(script_dir + "/input", "r")

line = inputFile.readline()
input = line.split(",")

part1(input.copy())
t0 = time.time()
part2(input.copy())
t1 = time.time()
print(t1-t0)


