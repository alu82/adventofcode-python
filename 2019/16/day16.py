import os
import itertools
from aoc.IntcodeComputer import IntcodeComputer
from aoc.Utils import drawPanel
from collections import deque
import colorama
from random import randrange

pattern = deque([0, 1, 0, -1])

def phase(signal, pattern):
    results = {}
    for i in range(1, len(signal)+1):
        results[i] = (-1*int(signal[i-1]), int(signal[i-1]))

    for i in range(1, len(signal)+1):
        usedPattern = pattern.copy()
        pass

    newSignal = ""
    for pos in range(1, len(signal)+1):
        usedPattern = pattern.copy()
        newValue = 0
        for idx, char in enumerate(signal):
            if (idx+1)%pos == 0:
                usedPattern.rotate(-1)
            #print(int(char), usedPattern[0])
            if usedPattern[0] != 0:
                newValue +=  int(char) * usedPattern[0]
        newSignal += str(newValue)[-1]
    return newSignal

def part1(signal):
    for _ in range(100):
        signal = phase(signal, pattern)
    print(signal[:8])

# This solution will not work for every input (see offset/length ratio).
# - To determine the value of an index i, all values prior to that index can be ignored (first entry in the pattern is zero)
# - The offset must be greater than signalLength/2 in order to be able to ignore the patterns the last two entries of the pattern. 
# - In that case we can ignore the pattern, because for the relevant part of the signal only the second entry of the pattern applies (1)
def part2(signal):
    newSignal = 10000*signal
    offset = int(signal[:7])
    relevantSignal = list(map(int, newSignal[offset:]))
    for _ in range(100):
        lastValue = 0
        for i in range(len(relevantSignal)-1, -1, -1):
            lastValue += relevantSignal[i]
            relevantSignal[i] = lastValue%10  

    newSignal = ''.join(str(value) for value in relevantSignal[:8]) 
    print(newSignal) 

# Open input files and get intcodeprogram 
script_dir = os.path.dirname(__file__)
inputFile = open(script_dir + "/input", "r")
signal = inputFile.readline()

part1(signal)
part2(signal)