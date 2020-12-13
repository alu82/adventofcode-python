import os
import time

def solve_1(input):
    timestamp = int(input[0])
    bus_ids = [int(b) for b in input[1].split(",") if b != "x"]
    result=min([(b, b-timestamp%b) for b in bus_ids], key=lambda p: p[1])
    print(result[1]*result[0])

def solve_2(input):
    bus_ids = [b for b in input[1].split(",")]
    
    for idx, bus_id in enumerate(bus_ids):
        if bus_id == "x":
            continue
        if idx == 0:
            solution = 0
            steps = int(bus_id)
        else:
            bus = int(bus_id)
            while True:
                if (solution+idx)%bus == 0:
                    steps *= bus
                    break
                else:
                    solution += steps             
    print(solution)


def find(ref, bus, idx):
    mult = 1
    while True:
        if (ref*mult+idx)%bus == 0:
            return mult
        mult += 1


script_dir = os.path.dirname(__file__)
with open(script_dir + "/input", "r") as myInput:
    start_time = time.time()
    input = [line.strip() for line in myInput]
    # solve_1(input)
    solve_2(input)
    print("--- Execution time %s s ---" % (time.time() - start_time))