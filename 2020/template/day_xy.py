import os
import time

def solve_1(input):
    pass

def solve_2(input):
    pass

with open(os.path.dirname(__file__) + "/input", "r") as myInput:
    start_time = time.time()
    input = [line.strip() for line in myInput]
    print(solve_1(input))
    print(solve_2(input))
    print("--- Execution time %s s ---" % (time.time() - start_time))