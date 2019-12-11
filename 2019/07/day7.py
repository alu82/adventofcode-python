import os
import itertools
from base.IntcodeComputer import IntcodeComputer

script_dir = os.path.dirname(__file__)
inputFile = open(script_dir + "/input", "r")

line = inputFile.readline()
input = line.split(",")

# Part 1
maxThrusterSignal=0
for phaseSettings in itertools.permutations([0,1,2,3,4]):
    inputSignal=0
    for i in range(5):
        phaseSetting=phaseSettings[i]
        computer = IntcodeComputer(input.copy(), [phaseSetting, inputSignal])
        computer.run()
        inputSignal = computer.getLastOutput()
    if inputSignal>maxThrusterSignal:
        maxThrusterSignal=inputSignal
print(maxThrusterSignal)

# Part 2
maxThrusterSignal=0
lastOutputE = 0
for phaseSettings in itertools.permutations([5,6,7,8,9]):
    computerA = IntcodeComputer(input.copy(), [phaseSettings[0]], True)
    computerB = IntcodeComputer(input.copy(), [phaseSettings[1]], True)
    computerC = IntcodeComputer(input.copy(), [phaseSettings[2]], True)
    computerD = IntcodeComputer(input.copy(), [phaseSettings[3]], True)
    computerE = IntcodeComputer(input.copy(), [phaseSettings[4]], True)
    computers = itertools.cycle([computerA, computerB, computerC, computerD, computerE])

    output = 0
    terminated = False
    while not terminated:
        currentComputer = next(computers)
        currentComputer.addArgument(output)
        currentComputer.run()
        output = currentComputer.getLastOutput()
        terminated = currentComputer.terminated

    maxThrusterSignal = computerE.getLastOutput() if computerE.getLastOutput()> maxThrusterSignal else maxThrusterSignal

print(maxThrusterSignal)