import itertools

class IntcodeComputer:

    ADD = 1 # Add
    MUL = 2 # Multiplication
    IN = 3 # Read Input
    OUT = 4 # Write Output
    JNZ = 5 # Jump if not Zero
    JZ = 6 # Jump if Zero
    LES = 7 # Less
    EQU = 8 # Equals
    CRB = 9 # Change relative Base
    EXT = 99 # Exit

    def __init__(self, program, arguments, pauseOnOutput = False):
        self.program = {}
        for key, value in enumerate(program):
            self.program[key] = int(value)
        self.arguments = arguments
        self.output = []
        self.pointer = 0
        self.running = False
        self.waiting = False # Waiting for input
        self.terminated = False
        self.pauseOnOutput = pauseOnOutput
        self.relativeBase = 0

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

    def getNextArgs(self, values, modes):
        arg1 = self.getValue(values[0], modes[0])
        arg2 = self.getValue(values[1], modes[1])
        return (arg1, arg2)

    def getValue(self, value, mode):
        returnValue = value
        if (mode==0 or mode==2) and value is not None:
            address = value + (self.relativeBase if mode==2 else 0)
            if address not in self.program:
                self.program[address] = 0
            returnValue = self.program[address]
        return returnValue

    def writeValue(self, value, mode, address):
        address = address + (self.relativeBase if mode==2 else 0)
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
        modes = self.getNextModes()
        values = self.getNextValues()
        args = self.getNextArgs(values, modes)

        if op == self.ADD:
            self.writeValue(args[0]+args[1], modes[2], values[2])  
            self.pointer += 4      
        elif op == self.MUL:
            self.writeValue(args[0]*args[1], modes[2], values[2]) 
            self.pointer += 4
        elif op == self.IN:
            if len(self.arguments) > 0:
                self.waiting = False
                self.writeValue(self.arguments.pop(0),modes[0], values[0])
                self.pointer += 2
            else:
                self.running = False
                self.waiting = True
        elif op == self.OUT:
            self.pointer += 2
            self.running = False
            self.output.append(args[0])
        elif op == self.JNZ:
            if args[0] != 0:
                self.pointer = args[1]
            else:
                self.pointer += 3
        elif op == self.JZ:
            if args[0] == 0:
                self.pointer = args[1]
            else:
                self.pointer += 3
        elif op == self.LES:
            result = 0
            if args[0]<args[1]:
                result = 1
            self.writeValue(result, modes[2], values[2])
            self.pointer += 4
        elif op == self.EQU:
            result = 0
            if args[0]==args[1]:
                result = 1
            self.writeValue(result, modes[2], values[2])
            self.pointer += 4
        elif op == self.CRB:
            self.relativeBase+=args[0]
            self.pointer+=2
        elif op == self.EXT:
            self.running = False
            self.terminated = True
        
    def run(self):
        self.running = True
        self.waiting = False
        if self.pauseOnOutput:
            while self.running and not self.waiting:
                self.executeNextOperation()
        else:
            while not self.terminated and not self.waiting:
                self.executeNextOperation()
                self.running = True # in case an output operation set the status
