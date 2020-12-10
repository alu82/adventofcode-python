import os
import time
import math

def solve(input):
    #Part 1
    input.extend([0, max(input)+3])
    sorted_list = sorted(input)
    print(sorted_list)
    diff_list = [sorted_list[i+1] - sorted_list[i] for i in range(len(sorted_list)-1)]
    print(diff_list.count(1)*diff_list.count(3))

    # Part 2
    comb = 1
    c = 0
    for n in diff_list:
        if n == 1:
            c+=1
        elif n == 3:
            if c == 1:
                comb *= 1
            elif c == 2:
                comb *= 2
            elif c == 3:
                comb *= 4
            elif c == 4:
                comb *= 7
            elif c == 5:
                comb *= 13
            c = 0
    
    print(comb)
        

script_dir = os.path.dirname(__file__)
with open(script_dir + "/input", "r") as myInput:
    start_time = time.time()
    input = [int(line.strip()) for line in myInput]
    solve(input)
    print("--- Execution time %s s ---" % (time.time() - start_time))