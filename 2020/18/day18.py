import os
import time

operators = ["+", "*"]

def solve_1(input):
    return sum([calculate(exp, precendece="none") for exp in input])
    
def solve_2(input):
    # add precedence for + here
    return sum([calculate(exp, precendece="add") for exp in input])


def calculate(exp, precendece):
    while not exp.isdigit():
        term = find_term(exp)
        value = eval_term(term, precendece)
        exp = exp.replace(term, str(value))
    else:
        return int(exp)

def find_term(exp):
    term = exp
    open = False
    for i, c in enumerate(exp):
        if c == "(":
            open = True
            lo = i
        elif c == ")":
            if open:
                up = i
                break
    if open:
        term = exp[lo:up+1]
    return term

def eval_term(term, precedence):
    clean_term = term
    if "(" in clean_term:
        clean_term = clean_term.replace("(","")
        clean_term = clean_term.replace(")","")
    if precedence == "none":
        return eval_term_from_behind(clean_term.split(" ")[::-1])
    elif precedence == "add":
        return eval_term_precedence_add(clean_term.split(" "))
    
def eval_term_from_behind(term):
    if len(term) == 1:
        return int(term[0])
    else:
        curr = int(term.pop(0))
        op = term.pop(0)
        if op == "+":
            return curr + eval_term_from_behind(term)
        elif op == "*":
            return curr * eval_term_from_behind(term)

def eval_term_precedence_add(term):
    if len(term) == 1:
        return int(term[0])
    else:
        if "*" in term:
            idx_mult = term.index("*")
            return eval_term_precedence_add(term[:idx_mult]) * eval_term_precedence_add(term[idx_mult+1:])
        else:
            return eval_term_from_behind(term)
        
with open(os.path.dirname(__file__) + "/input", "r") as myInput:
    start_time = time.time()
    input = [line.strip() for line in myInput]
    print(solve_1(input))
    print(solve_2(input))
    print("--- Execution time %s s ---" % (time.time() - start_time))