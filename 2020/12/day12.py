import os
import time
import copy
import math

def solve_1(input):
    facing = 90
    x = 0
    y = 0

    for instruction in input:
        action = instruction[0]
        value = int(instruction[1:])
        if action == "N":
            y += value
        elif action == "S":
            y -= value
        elif action == "E":
            x += value
        elif action == "W":
            x -= value
        elif action == "R":
            facing = (facing + value)%360
        elif action == "L":
            facing = (facing - value)%360
        elif action == "F":
            if facing == 0:
                y += value
            elif facing == 90:
                x += value
            elif facing == 180:
                y -= value
            elif facing == 270:
                x -= value
    print(abs(x) + abs(y))

def solve_2(input):
    x_s = 0
    y_s = 0
    x_w = 10
    y_w = 1

    for instruction in input:
        action = instruction[0]
        value = int(instruction[1:])
        if action == "N":
            y_w += value
        elif action == "S":
            y_w -= value
        elif action == "E":
            x_w += value
        elif action == "W":
            x_w -= value
        elif action == "R":
            x_w, y_w = rotate((x_s, y_s), (x_w, y_w), 360-value)
        elif action == "L":
            x_w, y_w = rotate((x_s, y_s), (x_w, y_w), value)
        elif action == "F":
            delta_x = x_w - x_s
            delta_y = y_w - y_s
            x_s += value*delta_x
            y_s += value*delta_y
            x_w += value*delta_x
            y_w += value*delta_y
    print(abs(x_s) + abs(y_s))

# rotates counterclockwise
def rotate(ship, waypoint, degrees):
    ox, oy = ship
    px, py = waypoint
    angle = math.radians(degrees)

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy

script_dir = os.path.dirname(__file__)
with open(script_dir + "/input", "r") as myInput:
    start_time = time.time()
    input = [line.strip() for line in myInput]
    solve_1(input)
    solve_2(input)
    print("--- Execution time %s s ---" % (time.time() - start_time))