import os



def intcomputer(inputArray):
    for i in range(0, len(inputArray), 4):
        op = int(inputArray[i])

        if(op == 99):
            break

        a = int(inputArray[int(inputArray[i+1])])
        b = int(inputArray[int(inputArray[i+2])])
        target = int(inputArray[i+3])

        result = 0
        if(op == 1):
            result = a+b
        elif(op == 2):
            result = a*b
     
        inputArray[target] = result

    return inputArray

script_dir = os.path.dirname(__file__)
inputFile = open(script_dir + "/input", "r")

line = inputFile.readline()
inputArray = line.split(",")

# Part 1
# print(intcomputer(inputArray))

# Part 2
for i in range(99):
    found = False
    if(found):
        break
    for j in range(99):
        inputArray = line.split(",")
        inputArray[1] = i
        inputArray[2] = j
        tmpResult = intcomputer(inputArray)
        if(tmpResult[0] == 19690720):
            print(100*i + j)
            found = True
            break
