import os
import time
import copy

U = (-1,0)  #UP
R = (0,1)   #RIGHT
D = (1,0)   #DOWN
L = (0,-1)  #LEFT
U_L = tuple(map(lambda a,b:a+b, U, L))
U_R = tuple(map(lambda a,b:a+b, U, R))
D_R = tuple(map(lambda a,b:a+b, D, R))
D_L = tuple(map(lambda a,b:a+b, D, L))
DIR = [U_L, U, U_R, R, D_R, D, D_L, L]

def solve(input):
    seat_Layout_1 = simulate(input, False, 4)
    print(sum([l.count("#") for l in seat_Layout_1]))

    seat_Layout_2 = simulate(input, True, 5)
    print(sum([l.count("#") for l in seat_Layout_2]))

def simulate(seat_layout, view_further, threshold):
    curr_seats = copy.deepcopy(seat_layout)
    changed = True
    while changed:
        changed = False
        new_seats = copy.deepcopy(curr_seats)
        for row in range(len(curr_seats)):
            for col in range(len(curr_seats[row])):
                occ = get_occupied_seats(curr_seats, row, col, view_further)
                if curr_seats[row][col] == "L" and occ == 0:
                    new_seats[row][col] = "#"
                    changed = True
                if curr_seats[row][col] == "#" and occ >= threshold:
                    new_seats[row][col] = "L"
                    changed = True
        curr_seats = new_seats
    return new_seats

def get_occupied_seats(seat_layout, row, col, view_further=False):
    row_l = len(seat_layout)
    col_l = len(seat_layout[0])

    steps = 1
    if view_further:
        steps = max(row_l, col_l)

    c = 0
    for pos in DIR:
        for s in range(1, steps+1):
            row_ = row + s*pos[0]
            col_ = col + s*pos[1]

            if 0 <= row_ < row_l and 0 <= col_ < col_l:
                seat = seat_layout[row_][col_]
                if seat == '#':
                    c += 1
                    break
                elif seat == 'L':
                    break
            else:
                break
    return c

script_dir = os.path.dirname(__file__)
with open(script_dir + "/input", "r") as myInput:
    start_time = time.time()
    input = [list(line.strip()) for line in myInput]
    solve(input)
    print("--- Execution time %s s ---" % (time.time() - start_time))