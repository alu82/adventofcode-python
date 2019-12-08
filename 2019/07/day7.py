import os
import itertools
from base.ShipComputer import ShipComputer

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
        computer = ShipComputer("A", input.copy(), [phaseSetting, inputSignal])
        inputSignal = computer.run()
    if inputSignal>maxThrusterSignal:
        maxThrusterSignal=inputSignal
print(maxThrusterSignal)

# Part 2
maxThrusterSignal=0
lastOutputE = 0
for phaseSettings in itertools.permutations([5,6,7,8,9]):
    computerA = ShipComputer("A", input.copy(), [phaseSettings[0]])
    computerB = ShipComputer("B", input.copy(), [phaseSettings[1]])
    computerC = ShipComputer("C", input.copy(), [phaseSettings[2]])
    computerD = ShipComputer("D", input.copy(), [phaseSettings[3]])
    computerE = ShipComputer("E", input.copy(), [phaseSettings[4]])
    computers = itertools.cycle([computerA, computerB, computerC, computerD, computerE])
    
    output = 0
    while output is not None:
        currentComputer = next(computers)
        currentComputer.addArgument(output)
        output = currentComputer.run()

        if currentComputer.name == "E" and output is not None:
            lastOutputE = output

    if lastOutputE>maxThrusterSignal:
        maxThrusterSignal=lastOutputE

print(maxThrusterSignal)