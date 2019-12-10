import os
from math import atan
from math import degrees
import itertools

def degreeTriangle(a, b):
    if b == 0:
        return 90
    else:
        return degrees(atan(a/b))

def getDegrees(position):
    # Top Right
    if position[0] >= 0 and position[1] <= 0:
        a = abs(position[0])
        b = abs(position[1])
        addDeg = 0
    # Bottom Right
    elif position[0] >= 0 and position[1] >= 0:
        a = abs(position[1])
        b = abs(position[0])
        addDeg = 90
    # Bottom Left
    elif position[0] <= 0 and position[1] >= 0:
        a = abs(position[0])
        b = abs(position[1])
        addDeg = 180
    # Top Left
    elif position[0] <= 0 and position[1] <= 0:
        a = abs(position[1])
        b = abs(position[0])
        addDeg = 270

    return degreeTriangle(a, b) + addDeg

#Part 1
def part1(asteroids):
    maxSeenAsteroids = (None, 0)
    for baseAsteroid in asteroids:
        offsets = set([])
        for remoteAsteroid in asteroids:
            if not baseAsteroid == remoteAsteroid:
                offset = (remoteAsteroid[0] - baseAsteroid[0], remoteAsteroid[1] - baseAsteroid[1])
                offsets.add(getDegrees(offset))
        seenAsteroids = (baseAsteroid, len(offsets))
        maxSeenAsteroids = seenAsteroids if seenAsteroids[1] > maxSeenAsteroids[1] else maxSeenAsteroids
    return maxSeenAsteroids

#Part 2
def part2(asteroids, laserPosition):
    otherAsteroids = {}
    for asteroid in asteroids:
        if not laserPosition == asteroid:
            offset = (asteroid[0] - laserPosition[0], asteroid[1] - laserPosition[1])
            degrees = getDegrees(offset)
            distance = abs(offset[0]) + abs(offset[1])
            newAsteroid = (asteroid[0], asteroid[1], distance)

            if degrees not in otherAsteroids:
                otherAsteroids[degrees] = []
            otherAsteroids[degrees].append(newAsteroid)
            otherAsteroids[degrees] = sorted(otherAsteroids[degrees], key=lambda asteroid: asteroid[2]) # sort by distance
    
    vaporized = []
    for key in itertools.cycle(sorted(otherAsteroids.keys())):
        if len(otherAsteroids[key]) > 0:
            vaporized.append(otherAsteroids[key].pop(0))
        if len(vaporized) == len(asteroids) - 1:
            break

    return vaporized
# Run methods
script_dir = os.path.dirname(__file__)
inputFile = open(script_dir + "/input", "r")

asteroids = []
for y, line in enumerate(inputFile):
    for x, character in enumerate(line):
        if character == '#':
            asteroids.append((x, y))

maxSeenAsteroids = part1(asteroids)
print(maxSeenAsteroids)
print(part2(asteroids, maxSeenAsteroids[0])[199])