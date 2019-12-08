import itertools

class ShipComputer:

    program = []
    arguments = []
    pointer = 0
    running = False

    ADD = 1
    MUL = 2
    IN = 3
    OUT = 4
    JNZ = 5
    JZ = 6
    LES = 7
    EQU = 8
    EXT = 99

    def __init__(self, program, arguments):
        for value in program:
            self.program.append(int(value))
        self.arguments = arguments

    def getNextOperation(self):
        return self.program[self.pointer]%100
    
    def getNextModes(self):
        modes = self.program[self.pointer]//100
        mode1=modes%10
        modes=modes//10
        mode2=modes%10
        mode3=modes//10
        return (mode1, mode2, mode3)

    def getNextValues(self):
        val1 = self.getValue(self.pointer + 1, 0)
        val2 = self.getValue(self.pointer + 2, 0)
        val3 = self.getValue(self.pointer + 3, 0)
        return (val1, val2, val3)

    def getNextArgs(self, values):
        modes = self.getNextModes()
        arg1 = self.getValue(values[0], modes[0])
        arg2 = self.getValue(values[1], modes[1])
        return (arg1, arg2)

    def getValue(self, value, mode):
        returnValue = value
        if mode==0 and value is not None: #indirect mode
            if value < len(self.program):
                 returnValue = self.program[value]
        return returnValue

    def writeValue(self, value, address):
        self.program[address] = value

    def addArgument(self, argument):
        self.arguments.append(argument)

    def executeNextOperation(self):
        op = self.getNextOperation()
        values = self.getNextValues()
        args = self.getNextArgs(values)

        if op == self.ADD:
            self.writeValue(args[0]+args[1], values[2])  
            self.pointer += 4      
        if op == self.MUL:
            self.writeValue(args[0]*args[1], values[2]) 
            self.pointer += 4
        if op == self.IN:
            self.writeValue(self.arguments.pop(0),values[0])
            self.pointer += 2
        if op == self.OUT:
            self.pointer += 2
            self.running = False
            return args[0]
        if op == self.JNZ:
            if args[0] != 0:
                self.pointer = args[1]
            else:
                self.pointer += 3
        if op == self.JZ:
            if args[0] == 0:
                self.pointer = args[1]
            else:
                self.pointer += 3
        if op == self.LES:
            result = 0
            if args[0]<args[1]:
                result = 1
            self.writeValue(result, values[2])
            self.pointer += 4
        if op == self.EQU:
            result = 0
            if args[0]==args[1]:
                result = 1
            self.writeValue(result, values[2])
            self.pointer += 4
        if op == self.EXT:
            self.running = False
            return None

    def run(self):
        self.running = True
        result = None
        while self.running and self.pointer<len(self.program):
            result = self.executeNextOperation()
        return result


program = [3,8,1001,8,10,8,105,1,0,0,21,38,47,72,97,122,203,284,365,446,99999,3,9,1001,9,3,9,1002,9,5,9,1001,9,4,9,4,9,99,3,9,102,3,9,9,4,9,99,3,9,1001,9,2,9,102,5,9,9,101,3,9,9,1002,9,5,9,101,4,9,9,4,9,99,3,9,101,5,9,9,1002,9,3,9,101,2,9,9,102,3,9,9,1001,9,2,9,4,9,99,3,9,101,3,9,9,102,2,9,9,1001,9,4,9,1002,9,2,9,101,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99]
# Part 1
#maxThrusterSignal=0
#for phaseSettings in itertools.permutations([0,1,2,3,4]):
#    inputSignal=0
#    for i in range(5):
#        phaseSetting=phaseSettings[i]
#        computer = ShipComputer(program.copy(), [phaseSetting, inputSignal])
#        inputSignal = computer.run()
#    if inputSignal>maxThrusterSignal:
#        maxThrusterSignal=inputSignal
#print(maxThrusterSignal)

# Part 2
maxThrusterSignal=0
currentOutputE = 0
for phaseSettings in itertools.permutations([5,6,7,8,9]):
    computerA = ShipComputer(program.copy(), [phaseSettings[0]])
    computerB = ShipComputer(program.copy(), [phaseSettings[1]])
    computerC = ShipComputer(program.copy(), [phaseSettings[2]])
    computerD = ShipComputer(program.copy(), [phaseSettings[3]])
    computerE = ShipComputer(program.copy(), [phaseSettings[4]])
    computers = [computerA, computerB, computerC, computerD, computerE]
    
    i = 0
    output = 0
    while output is not None:
        currentComputer = computers[i%5]
        currentComputer.addArgument(output)
        output = currentComputer.run()

        if i%5 == 4 and output is not None:
            currentOutputE = output
        i += 1
    if currentOutputE>maxThrusterSignal:
        maxThrusterSignal=currentOutputE

print(maxThrusterSignal)
print(currentOutputE)