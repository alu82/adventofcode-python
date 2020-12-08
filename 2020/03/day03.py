import os

def slope(r, d, terrain):
    mod = len(terrain[0])
    x = y = 0
    trees = 0

    while not y >= len(terrain) - d:
        x = (x+r) % mod
        y += d
        if terrain[y][x] == '#':
            trees += 1
    
    return trees

def solve(myInput):
    terrain = [line.strip() for line in myInput]
    part1 = slope(3, 1, terrain)
    part2 = slope(1, 1, terrain) * slope(3, 1, terrain) * slope(5, 1, terrain) * slope(7, 1, terrain) * slope(1, 2, terrain)
    print(part1)
    print(part2)
    


script_dir = os.path.dirname(__file__)
with open(script_dir + "/input", "r") as myInput:
    solve(myInput)