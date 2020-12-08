import os
import time

def solve_1(myInput):
    rules = get_rules(myInput)
    
    bags = set()
    bags.add("shiny gold")
    found_new = True
    
    while found_new:
        found_new = False
        for key, value in rules.items():
            if key not in bags:
                for q, b in value:
                    if b in bags:
                        bags.add(key)
                        found_new = True

    bags.remove("shiny gold")
    print(len(bags))

def solve_2(myInput):
    rules = get_rules(myInput)
    print(rules)
    
    bags = dict()
    bags["shiny gold"] = 1
    n_bags = 0

    tmp_bags = dict()
    found_new = True

    while found_new:
        found_new = False
        for key, value in bags.items():
            rule = rules[key]
            for q,b in rule:
                found_new = True
                tmp_bags[b] = q * value + tmp_bags.get(b, 0)

        if found_new:
            bags = tmp_bags.copy()
            tmp_bags.clear()
            n_bags += sum(bags.values())

    print(n_bags)


def get_rules(myInput):
    rules = dict()
    for line in myInput:
        line = line.replace(".", "")
        line = line.replace(" bags", "")
        line = line.replace(" bag", "")
        outer, inner = line.split("contain")
        inner_p = [p.strip() for p in inner.split(", ")]
        inner_q_b = []
        for p in inner_p:
            if not p == "no other":
                q, b = p.split(" ", 1)
                inner_q_b.append((int(q), b))
        rules[outer.strip()] = inner_q_b
    return rules

script_dir = os.path.dirname(__file__)
with open(script_dir + "/input", "r") as myInput:
    start_time = time.time()
    input = [line.strip() for line in myInput]
    solve_1(input)
    solve_2(input)
    print("--- %s seconds ---" % (time.time() - start_time))