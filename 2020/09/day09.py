import os
import time

def solve(input):
    
    # Part 1
    pre = 25
    for n in range(pre, len(input)):
        summands = input[n-pre:n]
        sum_1 = input[n]

        found = False
        for i in range(len(summands)):
            rest = sum_1 - summands[i]
            if rest in summands[i+1:]:
                found = True
                break

        if not found:
            print(sum_1)
            invalid = sum_1

    # Part 2
    for l in range(2, len(input)):
        for n in range(len(input)-l):
            summands_2 =  input[n:n+l]
            if  sum(summands_2) == invalid:
                print(min(summands_2) + max(summands_2)) 
                return

script_dir = os.path.dirname(__file__)
with open(script_dir + "/input", "r") as myInput:
    start_time = time.time()
    input = [int(line.strip()) for line in myInput]
    solve(input)
    print("--- Execution time %s s ---" % (time.time() - start_time))