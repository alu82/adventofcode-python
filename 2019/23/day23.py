import os
from aoc.IntcodeComputer import IntcodeComputer
from threading import Thread
from threading import RLock
import time

class Packet:
    def __init__(self, target, x, y):
        self.target = target
        self.x = x
        self.y = y

    def print(self):
        print(self.target, self.x, self.y)

class Network:

    def __init__(self):
        self.computers = {}
        self.lock = RLock()
        self.nat = None

    def addComputer(self, computer):
        self.computers[computer.address] = computer
    
    def addNat(self, nat):
        self.nat = nat

    def startNetwork(self):
        for computer in self.computers.values():
            computer.run()
        self.nat.run()

    def stopNetwork(self):
        self.nat.shutdown()
        for computer in self.computers.values():
            computer.shutdown()

    def dispatchPacket(self, packet):
        packet.print()
        if packet.target in self.computers:
            self.lock.acquire()
            self.computers[packet.target].receivePacket(packet)
            self.lock.release()
        
        if packet.target == self.nat.address:
            self.nat.receivePacket(packet)

class Nat:

    def __init__(self, network, stopOnFirst):
        self.address = 255
        self.network = network
        self.stopOnFirst = stopOnFirst
        self.lastPacket = None
        self.lastSendPacket = None
        self.running = False
    
    def receivePacket(self, packet):
        self.lastPacket = packet

        if self.stopOnFirst:
            self.network.stopNetwork()
            self.lastPacket.print()

    def monitor(self):
        while self.running:
            idle = True
            for computer in self.network.computers.values():
                if len(computer.inQueue) > 0:
                    idle = False
                    break
            
            if idle and self.lastPacket is not None:
                time.sleep(5)
                halt = False
                if self.lastSendPacket is not None:
                    halt = self.lastSendPacket.y == self.lastPacket.y

                self.lastSendPacket = Packet(0, self.lastPacket.x, self.lastPacket.y)
                print("waking up network" + str(self.lastPacket.y))
                self.network.dispatchPacket(self.lastSendPacket)
                if halt:
                    self.network.stopNetwork()
            time.sleep(5)

    
    def run(self):
        monitorThread = Thread(target=self.monitor)
        self.running = True
        monitorThread.start()

    def shutdown(self):
        self.running = False

class NetworkComputer:

    def __init__(self, address, program, network):
        self.address = address
        self.nic = IntcodeComputer(program, [address])
        self.network = network
        self.inQueue = []
        self.lock = RLock()
        self.running = False

    def receivePacket(self, packet):
        self.inQueue.append(packet)

    def processPacket(self):
        while self.running:
            self.lock.acquire()
            if len(self.inQueue) == 0:
                self.nic.addArgument(-1) 
            else:
                nextPacket = self.inQueue.pop(0)
                self.nic.addArgument(nextPacket.x)
                self.nic.addArgument(nextPacket.y)
            if self.nic.waiting:
                self.nic.run()
            self.lock.release()

    def sendPacket(self):
        while self.running:
            self.lock.acquire()
            if len(self.nic.output) > 2:
                target = self.nic.output.pop(0)
                x = self.nic.output.pop(0)
                y = self.nic.output.pop(0)
                packet = Packet(target, x, y)
                self.network.dispatchPacket(packet)
            self.lock.release()

    def run(self):
        inThread = Thread(target=self.processPacket)
        outThread = Thread(target=self.sendPacket)
        self.running = True
        self.nic.run()
        inThread.start()
        outThread.start()

    def shutdown(self):
        self.running = False

def part1(program):
    numberOfComputers = 50
    network = Network()
    for address in range(numberOfComputers):
        network.addComputer(NetworkComputer(address, program.copy(), network))
    network.addNat(Nat(network, True))
    network.startNetwork()

def part2(program):
    numberOfComputers = 50
    network = Network()
    for address in range(numberOfComputers):
        network.addComputer(NetworkComputer(address, program.copy(), network))
    network.addNat(Nat(network, False))
    network.startNetwork()


# Open input files and get intcodeprogram
script_dir = os.path.dirname(__file__)
inputFile = open(script_dir + "/input", "r")
line = inputFile.readline()
program = line.split(",")


# part1(program.copy())
part2(program.copy())