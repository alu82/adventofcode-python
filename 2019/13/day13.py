import os
import itertools
from aoc.IntcodeComputer import IntcodeComputer
from aoc.Utils import drawPanel
import colorama

EMPTY = 0
WALL = 1
BLOCK = 2
HPADDLE = 3
BALL = 4

STICK_NEUTRAL = 0
STICK_LEFT = -1
STICK_RIGHT = 1

def drawGameBoard(gameBoard):
    colors = {
        EMPTY: colorama.Fore.BLACK,
        WALL: colorama.Fore.BLUE,
        BLOCK: colorama.Fore.YELLOW,
        HPADDLE: colorama.Fore.GREEN,
        BALL: colorama.Fore.RED
    }

    gamePanel = {}
    for idx in range(2, len(gameBoard), 3):
        gameElement = gameBoard[idx]
        if(gameElement in colors):
            pos = (gameBoard[idx-2], gameBoard[idx-1])
            gamePanel[pos] = gameElement
    if len(gamePanel.keys()) > 0:
        drawPanel(gamePanel, colors)

def getBallPosition(gameBoard):
    for idx in range(2, len(gameBoard), 3):
        if gameBoard[idx] == BALL:
            ballPos = (gameBoard[idx-2], gameBoard[idx-1])
    return ballPos

def getPaddlePosition(gameBoard):
    for idx in range(2, len(gameBoard), 3):
        if gameBoard[idx] == HPADDLE:
            paddlePos = (gameBoard[idx-2], gameBoard[idx-1])
    return paddlePos

def getNextJoyStickMovement(paddlePosition, ballPosition):
    xDiff = paddlePosition[0] - ballPosition[0]
    if xDiff == 0:
        return STICK_NEUTRAL
    elif xDiff < 0:
        return STICK_RIGHT
    elif xDiff > 0:
        return STICK_LEFT

def getGameScore(gameBoard):
    gameScore = 0
    for idx in range(1, len(gameBoard), 2):
        if gameBoard[idx-1] == -1 and gameBoard[idx] == 0:
            gameScore = gameBoard[idx+1]
    return gameScore

def part1(program):
    game=IntcodeComputer(program, [])
    game.run()
    blocks = list(filter(lambda item: item == BLOCK, game.output[2::3]))
    return len(blocks)

def part2(program):
    program[0] = 2
    game=IntcodeComputer(program, [])
    while game.terminated != True:
        game.run()
        drawGameBoard(game.output)
        paddlePosition = getPaddlePosition(game.output)
        ballPosition = getBallPosition(game.output)
        game.addArgument(getNextJoyStickMovement(paddlePosition, ballPosition))
    
    return getGameScore(game.output)
        

# Open input files and get intcodeprogram 
script_dir = os.path.dirname(__file__)
inputFile = open(script_dir + "/input", "r")
line = inputFile.readline()
program = line.split(",")

# Part 1
blocks = part1(program.copy())
print(blocks)

# Part 2
gameScore = part2(program.copy())
print(gameScore)

