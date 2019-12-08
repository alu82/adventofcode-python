import os

script_dir = os.path.dirname(__file__)
inputFile = open(script_dir + "/input", "r")

fuelNeeded = 0
for line in inputFile:
    fuelNeededForModule = int(line)//3 -2
    fuelNeeded +=  fuelNeededForModule
print(fuelNeeded)