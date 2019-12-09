import itertools

class ShipComputer:

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
        self.program = []
        for value in program:
            self.program.append(int(value))
        self.arguments = arguments
        self.output = []
        self.pointer = 0
        self.running = False
        self.terminated = False

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

    def getLastOutput(self):
        if(len(self.output)>0):
            return self.output[-1]
        else:
            return None

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
            self.output.append(args[0])
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
            self.terminated = True

    def run(self):
        self.running = True
        while self.running and self.pointer<len(self.program):
            self.executeNextOperation()
