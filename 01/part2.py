import os

def calculateFuelForMass(mass):
    fuelNeeded = mass//3 -2
    if fuelNeeded > 0:
        return fuelNeeded + calculateFuelForMass(fuelNeeded)
    else:
        return 0

script_dir = os.path.dirname(__file__)
inputFile = open(script_dir + "/input", "r")

fuelNeeded = 0
for line in inputFile:
   fuelNeededForModule = calculateFuelForMass(int(line))
   fuelNeeded +=  fuelNeededForModule
print(fuelNeeded)