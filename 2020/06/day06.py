import os
import time

def solve_1(input):
    questions = set()
    sum_1 = 0
    for line in input:
        if line:
            for q in line:
                questions.add(q)
        else:
            sum_1 += len(questions)
            questions = set()
    print(sum_1)

def solve_2(input):
    questions = set()
    sum = 0
    first_line = True
    for line in input:
        if line:
            questions_2 = set()
            for q in line:
                questions_2.add(q)
            if first_line:
                questions = questions_2
                first_line = False
            else:
                questions = questions.intersection(questions_2)
        else:
            sum += len(questions)
            questions = set()
            first_line = True
    print(sum)


script_dir = os.path.dirname(__file__)
with open(script_dir + "/input", "r") as myInput:
    input = [line.strip() for line in myInput]
    input.append("")
    solve_1(input)
    solve_2(input)
    