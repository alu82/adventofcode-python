import os
from base.IntcodeComputer import IntcodeComputer
from collections import deque
import colorama

class Robo:
    
    UP=(0,-1)
    RIGHT=(1,0)
    DOWN=(0,1)
    LEFT=(-1,0)

    BLACK=0
    WHITE=1
    
    TURN_LEFT=0
    TURN_RIGHT=1

    def __init__(self, program, startColor):
        self.brain=IntcodeComputer(program,[], True)
        self.panel=(0,0)
        self.facing=deque([self.UP, self.RIGHT, self.DOWN, self.LEFT])
        self.path=[self.panel]
        self.panelGrid={}
        self.panelGrid[self.panel] = startColor

    def getColorForPanel(self):
        return self.panelGrid.get(self.panel, self.BLACK)
    
    def move(self):
        self.panel=(self.panel[0]+self.facing[0][0], self.panel[1]+self.facing[0][1])
        self.path.append(self.panel)

    def rotate(self, direction):
        if direction==self.TURN_LEFT:
            self.facing.rotate(1)
        elif direction==self.TURN_RIGHT:
            self.facing.rotate(-1)

    def paint(self, color):
        if color==self.BLACK:
            self.panelGrid[self.panel]=self.BLACK
        elif color==self.WHITE:
            self.panelGrid[self.panel]=self.WHITE
    
    def work(self):
        while not self.brain.terminated:
            self.brain.addArgument(self.getColorForPanel())
            self.brain.run()
            nextColor=self.brain.getLastOutput()
            self.brain.run()
            nextRotation=self.brain.getLastOutput()
            self.paint(nextColor)
            self.rotate(nextRotation)
            self.move()

# panel of type dictionary with keys as 2-tupel (col, row) and values as colors
def drawPanel(panel):
    block = u'\u2588'
    colors = {
        Robo.BLACK: colorama.Fore.BLACK,
        Robo.WHITE: colorama.Fore.WHITE,
    }
    
    minRow = min(panel.keys(), key=lambda panel:panel[1])[1]
    maxRow = max(panel.keys(), key=lambda panel:panel[1])[1]
    minCol = min(panel.keys(), key=lambda panel:panel[0])[0]
    maxCol = max(panel.keys(), key=lambda panel:panel[0])[0]

    drawing = ""
    for row in range(minRow, maxRow+1):
        for col in range(minCol, maxCol+1):
            color = colors[panel.get((col, row), 0)]
            drawing += color + block
        drawing += "\n"
    print(drawing)
            
# Run methods
script_dir = os.path.dirname(__file__)
inputFile = open(script_dir + "/input", "r")
line = inputFile.readline()
program = line.split(",")

# Part 1
robo1=Robo(program.copy(), Robo.BLACK)
robo1.work()
print(len(set(robo1.path)))

# Part 2 
robo2=Robo(program.copy(), Robo.WHITE)
robo2.work()
drawPanel(robo2.panelGrid)
