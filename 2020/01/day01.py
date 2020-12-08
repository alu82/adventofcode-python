import os

def part_1(myInput):
    for i in range(len(myInput)-1):
        for j in range(i+1,len(myInput)):
            sum = myInput[i] + myInput[j]
            if sum == 2020:
                prod = myInput[i] * myInput[j]
                print(prod)
                return

def part_2(myInput):
    for i in range(len(myInput)-2):
        for j in range(i+1,len(myInput)-1):
            for k in range(j+1, len(myInput)):
                sum = myInput[i] + myInput[j] + myInput[k]
                if sum == 2020:
                    prod = myInput[i] * myInput[j] * myInput[k]
                    print(prod)
                    return
    

script_dir = os.path.dirname(__file__)
with open(script_dir + "/input", "r") as myInput:
    input = [int(line.replace("\n", "")) for line in myInput.readlines()]
    part_1(input)
    part_2(input)