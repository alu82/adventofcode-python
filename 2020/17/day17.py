import os
import time
from collections import defaultdict
from collections import namedtuple
from copy import deepcopy
from itertools import product

Coordinate = namedtuple("Coordinate", ["x", "y", "z", "w"])

def solve_1(input):
    grid = simulate(get_grid(input),cycles=6,dimensions=3)
    print(len([v for v in grid.values() if v == "#"]))
    
def solve_2(input):
    grid = simulate(get_grid(input),cycles=6,dimensions=4)
    print(len([v for v in grid.values() if v == "#"]))

def simulate(grid, cycles, dimensions):
    for _ in range(cycles):
        ext_up = max([max(c.x,c.y,c.z,c.w) for c in grid.keys()]) # since we have a default dict we calculate the maximum extension into one dimension
        ext_lo = min([min(c.x,c.y,c.z,c.w) for c in grid.keys()])
        extension = range(ext_lo-1, ext_up+2)
        w_extension = extension
        if dimensions == 3:
            w_extension = range(1)
        new_grid = deepcopy(grid)
        for x in extension:
            for y in extension:
                for z in extension:
                    for w in w_extension:
                        c_coord = Coordinate(x,y,z,w)
                        c_value = grid[(x,y,z,w)]
                        active = no_active_neighbors(grid, c_coord)
                        if c_value == "#"  and active not in (2,3):
                            new_grid[c_coord] = "."
                        elif c_value == "." and active == 3:
                            new_grid[c_coord] = "#"  
        grid = new_grid  
    return new_grid

def no_active_neighbors(grid, coord):
    active = 0
    for c in product([-1, 0, 1], repeat=4):
        if not c == (0,0,0,0) and grid[(coord.x+c[0],coord.y+c[1],coord.z+c[2],coord.w+c[3])] == "#":
            active += 1
    return active

def get_grid(input):
    grid = defaultdict(lambda: ".")
    for x, line in enumerate(input):
        for y, value in enumerate(line):
            grid[Coordinate(x,y,0,0)] = value
    return grid

def print_grid(grid):
    ext_up = max([max(c.x,c.y,c.z,c.w) for c in grid.keys()]) 
    ext_lo = min([min(c.x,c.y,c.z,c.w) for c in grid.keys()])
    extension = range(ext_lo-1, ext_up+2)
    for z in extension:
        print("z=",z)
        for x in extension:
            line = ""
            for y in extension:
                line += grid[(x,y,z)]
            print(line)


script_dir = os.path.dirname(__file__)
with open(script_dir + "/input", "r") as myInput:
    start_time = time.time()
    input = [line.strip() for line in myInput]
    solve_1(input)
    solve_2(input)
    print("--- Execution time %s s ---" % (time.time() - start_time))