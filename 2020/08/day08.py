import os
import time

def solve(program):
    print(execute_program(program))

    for i in range(len(program)):
        
        fixed_program = program.copy()
        op, arg = parse_instruction(fixed_program[i])
        if op in ["nop", "jmp"]:
            if op == "nop":
                fixed_instruction = "jmp" + " " + str(arg)
            elif op == "jmp":
                fixed_instruction = "nop" + " " + str(arg)
            
            fixed_program[i] = fixed_instruction
            status, accumulator = execute_program(fixed_program)

            if status == 0:
                print(accumulator)
                break

def execute_program(program):
    accumulator = 0
    ex_lines = set()
    next_line = 0

    while True:
        if next_line in ex_lines:
            status = 1
            break
        elif next_line == len(program):
            status = 0
            break
        else:
            ex_lines.add(next_line)

        op, arg = parse_instruction(program[next_line])

        if op == "acc":
            accumulator += arg
            next_line += 1
        elif op == "jmp":
            next_line += arg
        elif op == "nop":
            next_line += 1
    
    return status, accumulator

def parse_instruction(instruction):
    return instruction[:3], int(instruction[4:])

script_dir = os.path.dirname(__file__)
with open(script_dir + "/input", "r") as myInput:
    start_time = time.time()
    input = [line.strip() for line in myInput]
    solve(input)
    print("--- %s seconds ---" % (time.time() - start_time))