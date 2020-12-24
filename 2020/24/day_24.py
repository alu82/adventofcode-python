import os
import time
from collections import defaultdict 

directions = {
    "e" : (2,0),
    "se" : (1,1),
    "sw" : (-1,1),
    "w" : (-2,0),
    "nw" : (-1,-1),
    "ne" : (1,-1)
    }

def solve(input):
    black_tiles = set()
    for instructions in input:
        tile_x, tile_y = 0, 0
        instruction = ""
        for d in instructions:
            instruction += d
            if instruction in directions.keys():
                tile_x += directions[instruction][0]
                tile_y += directions[instruction][1]
                flipped_tile = (tile_x, tile_y)
                instruction = ""
        if flipped_tile in black_tiles:
            black_tiles.remove(flipped_tile)
        else:
            black_tiles.add(flipped_tile)
    print(len(black_tiles))

    for _ in range(100):
        black_neighbors_black = defaultdict(lambda : 0)
        black_neighbors_white = defaultdict(lambda : 0)

        for black_tile in black_tiles:
            black_neighbors_black[black_tile] = 0

        for black_tile in black_tiles:
            for neighbor_tile in [(black_tile[0]+d[0], black_tile[1]+d[1]) for d in directions.values()]:
                if neighbor_tile in black_tiles:
                    black_neighbors_black[neighbor_tile] += 1
                else:
                    black_neighbors_white[neighbor_tile] += 1
        
        for b, nb in black_neighbors_black.items():
            if nb == 0 or nb > 2:
                black_tiles.remove(b)
        
        for w, nb in black_neighbors_white.items():
            if nb == 2:
                black_tiles.add(w)
    print(len(black_tiles))

with open(os.path.dirname(__file__) + "/input", "r") as myInput:
    start_time = time.time()
    input = [line.strip() for line in myInput]
    solve(input)
    print("--- Execution time %s s ---" % (time.time() - start_time))