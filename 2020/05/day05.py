import os

def solve(input):
    seats = [get_seat_id(boarding_pass) for boarding_pass in input]
    print(max(seats))

    my_seat_id = 0
    for i in range(max(seats)):
        p, c, n = i-1, i, i+1
        if p in seats and n in seats and c not in seats:
            my_seat_id =c
    print(my_seat_id)


def get_seat_id(boarding_pass):
    bin = boarding_pass.replace("L", "0")
    bin = bin.replace("F", "0")
    bin = bin.replace("R", "1")
    bin = bin.replace("B", "1")
    return int(bin, 2)

script_dir = os.path.dirname(__file__)
with open(script_dir + "/input", "r") as myInput:
    input = [line.strip() for line in myInput]
    solve(input)