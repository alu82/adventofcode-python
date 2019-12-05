import os

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


def newintcomputer(input, inputArray):
    pointer=0
    while pointer<=len(inputArray):
        anweisung=auslesenInstractionAndMode(int(inputArray[pointer]))
        op=anweisung[0]
        if(op == 99):
            break
        if(op==1):
            para1=gibWert(anweisung[1], int(inputArray[pointer+1]), inputArray)
            para2=gibWert(anweisung[2], int(inputArray[pointer+2]), inputArray)
            result=para1+para2
            inputArray[int(inputArray[pointer+3])] = result
            pointer=pointer+4
        if(op==2):
            para1=gibWert(anweisung[1], int(inputArray[pointer+1]), inputArray)
            para2=gibWert(anweisung[2], int(inputArray[pointer+2]), inputArray)
            result=para1*para2
            inputArray[int(inputArray[pointer+3])] = result
            pointer=pointer+4
        if(op==3):
            inputArray[int(inputArray[pointer+1])] =input
            pointer=pointer+2
        if(op==4):
            print(gibWert(anweisung[1], int(inputArray[pointer+1]), inputArray))
            pointer=pointer+2
        if(op==5):
            if gibWert(anweisung[1], int(inputArray[pointer+1]), inputArray) != 0:
                pointer = gibWert(anweisung[2], int(inputArray[pointer+2]), inputArray)
            else:
                pointer=pointer+3
        if(op==6):
            if gibWert(anweisung[1], int(inputArray[pointer+1]), inputArray) == 0:
                pointer = gibWert(anweisung[2], int(inputArray[pointer+2]), inputArray)
            else:
                pointer=pointer+3
        if(op==7):
            para1=gibWert(anweisung[1], int(inputArray[pointer+1]), inputArray)
            para2=gibWert(anweisung[2], int(inputArray[pointer+2]), inputArray)
            result = 0
            if(para1<para2):
                result = 1
            inputArray[int(inputArray[pointer+3])] = result
            pointer=pointer+4
        if(op==8):
            para1=gibWert(anweisung[1], int(inputArray[pointer+1]), inputArray)
            para2=gibWert(anweisung[2], int(inputArray[pointer+2]), inputArray)
            result = 0
            if(para1==para2):
                result = 1
            inputArray[int(inputArray[pointer+3])] = result
            pointer=pointer+4
            

script_dir = os.path.dirname(__file__)
inputFile = open(script_dir + "/input", "r")

line = inputFile.readline()
inputArray = line.split(",")

# Part 1
#newintcomputer(1, inputArray)

# Part 2
newintcomputer(5, inputArray)