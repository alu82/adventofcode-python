import os
import itertools

def auslesenInstractionAndMode (intmode):
    op=intmode%100
    restmodezahl=intmode//100
    if op==3 or op==4:
        return (op, restmodezahl)
    mode1=restmodezahl% 10
    restmodezahl=restmodezahl//10
    mode2=restmodezahl% 10
    mode3=restmodezahl//10
    return (op, mode1, mode2, mode3)

def gibWert(mode, zahl, inputArray):
    if mode==0:
        return int(inputArray[zahl])
    if mode==1:
        return zahl


def newintcomputer(phaseSetting, inputSignal, input, startPointer, nextInputType):
    pointer=startPointer
    if nextInputType:
        nextInput=phaseSetting
    else:
        nextInput=inputSignal
    while pointer<=len(input):
        anweisung=auslesenInstractionAndMode(int(input[pointer]))
        op=anweisung[0]
        if(op == 99):
            return (None, pointer)
        if(op==1):
            para1=gibWert(anweisung[1], int(input[pointer+1]), input)
            para2=gibWert(anweisung[2], int(input[pointer+2]), input)
            result=para1+para2
            input[int(input[pointer+3])] = result
            pointer=pointer+4
        if(op==2):
            para1=gibWert(anweisung[1], int(input[pointer+1]), input)
            para2=gibWert(anweisung[2], int(input[pointer+2]), input)
            result=para1*para2
            input[int(input[pointer+3])] = result
            pointer=pointer+4
        if(op==3):
            input[int(input[pointer+1])] = nextInput
            nextInput=inputSignal
            pointer=pointer+2
        if(op==4):
            return ((gibWert(anweisung[1], int(input[pointer+1]), input)), pointer+2)
        if(op==5):
            if gibWert(anweisung[1], int(input[pointer+1]), input) != 0:
                pointer = gibWert(anweisung[2], int(input[pointer+2]), input)
            else:
                pointer=pointer+3
        if(op==6):
            if gibWert(anweisung[1], int(input[pointer+1]), input) == 0:
                pointer = gibWert(anweisung[2], int(input[pointer+2]), input)
            else:
                pointer=pointer+3
        if(op==7):
            para1=gibWert(anweisung[1], int(input[pointer+1]), input)
            para2=gibWert(anweisung[2], int(input[pointer+2]), input)
            result = 0
            if(para1<para2):
                result = 1
            input[int(input[pointer+3])] = result
            pointer=pointer+4
        if(op==8):
            para1=gibWert(anweisung[1], int(input[pointer+1]), input)
            para2=gibWert(anweisung[2], int(input[pointer+2]), input)
            result = 0
            if(para1==para2):
                result = 1
            input[int(input[pointer+3])] = result
            pointer=pointer+4
            

script_dir = os.path.dirname(__file__)
inputFile = open(script_dir + "/input", "r")

line = inputFile.readline()
input = line.split(",")

# Part 1
#maxThrusterSignal=0
#for phaseSettings in itertools.permutations([0,1,2,3,4]):
#    inputSignal=0
#    for i in range(5):
#        phaseSetting=phaseSettings[i]
#        inputSignal=newintcomputer(phaseSetting, inputSignal, input.copy(), 0, True)[0]
#    if inputSignal>maxThrusterSignal:
#        maxThrusterSignal=inputSignal
#print(maxThrusterSignal)

# Part 2
maxThrusterSignal=0
currentOutputE = 0
for phaseSettings in itertools.permutations([5,6,7,8,9]):
    currentPointers = [0,0,0,0,0]
    inputs = [input.copy(), input.copy(), input.copy(), input.copy(), input.copy()]
    inputSignal=0
    i = 0
    while inputSignal is not None:
        nextInputType = i<5
        phaseSetting=phaseSettings[i%5]
        currentPointer = currentPointers[i%5]
        computerStatus=newintcomputer(phaseSetting, inputSignal, inputs[i%5], currentPointer, nextInputType)
        inputSignal = computerStatus[0]
        currentPointers[i%5] = computerStatus[1]
        if i%5 == 4 and inputSignal is not None:
            currentOutputE = inputSignal
        i += 1
    if currentOutputE>maxThrusterSignal:
        maxThrusterSignal=currentOutputE

print(maxThrusterSignal)
print(currentOutputE)