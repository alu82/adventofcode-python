import os
import math
import sympy as sy


class Reaction:

    def __init__(self, input, output):
        self.input = input
        self.output = output

def expand(reactions, needed):  
    for chemical in needed.keys():
        if needed[chemical] > 0 and chemical != 'ORE':
            reaction = list(filter(lambda r:r.output[1]==chemical, reactions))[0]
            mult = int(math.ceil(needed[chemical]/reaction.output[0]))

            for input in reaction.input:
                tmpChemical = input[1]
                tmpAmount = input[0]
                newNeed = needed.get(tmpChemical, 0) + mult*tmpAmount
                needed[tmpChemical] = newNeed
            needed[chemical] = needed[chemical] - reaction.output[0]*mult
    
    stop = True
    for key, value in needed.items():
        if value > 0 and key != 'ORE':
            stop = False

    if stop:
        return needed['ORE']
    else:
        return expand(reactions, needed)


def part1(reactions):
    needed = {}
    for reaction in reactions:
        needed[reaction.output[1]] = 0
    needed['ORE'] = 0
    needed['FUEL'] = 1
    return expand(reactions, needed)

def part2(reactions):
    needed = {}
    for reaction in reactions:
        needed[reaction.output[1]] = 0
    needed['ORE'] = 0
    
    targetOre = 1000000000000

    fuel = 6320000
    while True:
        needed = {}
        for reaction in reactions:
            needed[reaction.output[1]] = 0
        needed['ORE'] = 0
        needed['FUEL'] = fuel

        ore = expand(reactions, needed)
        if ore > targetOre:
            fuel -= 1
            break
        else:
            fuel += 1
    return(fuel)
    
# Prepare
script_dir = os.path.dirname(__file__)
inputFile = open(script_dir + "/input", "r")
reactions = []
for line in inputFile:
    leftRight = line.split('=>')
    left = list(map(lambda p : p.strip().split(' '), leftRight[0].split(',')))
    right = leftRight[1].strip().split(' ')

    input = []
    for leftPart in left:
        input.append((int(leftPart[0]), leftPart[1]))
    output = (int(right[0]), right[1])

    reactions.append(Reaction(input, output))

print(part1(reactions))
print(part2(reactions))

    

