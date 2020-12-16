import os
import time

def solve_1(input):
    ranges = extract_ranges(input)
    print(sum([calc_ticket_error(t, ranges.values())[1] for t in get_nearby_tickets(input)]))

def solve_2(input):
    ranges = extract_ranges(input)
    valid_tickets = [t for t in get_nearby_tickets(input) if not calc_ticket_error(t, ranges.values())[0]]
    my_ticket = get_my_ticket(input)
    
    field_indexes = dict()
    changed = True
    while changed:
        changed = False
        for field, field_ranges in ranges.items():
            if field not in field_indexes.keys():
                possible_indexes = calc_index_for_ranges(field_ranges, valid_tickets, set(field_indexes.values()))
                if len(possible_indexes) == 1:
                    field_indexes[field] = possible_indexes.pop()
                    changed = True

    solution = 1
    for field, field_index in field_indexes.items():
        if field.startswith("departure"):
            solution *= my_ticket[field_index]
    print(solution)

def extract_ranges(input):
    valid_ranges = dict()
    for line in input:
        if line == "":
            break

        field, ranges = line.split(":")
        field_ranges = set()
        for r in [r.strip() for r in ranges.split(" or ")]:
            l, u = r.split("-")
            field_ranges.add(range(int(l),int(u)+1))
        valid_ranges[field] = field_ranges

    return valid_ranges

def get_nearby_tickets(input):
    tickets = []
    for t in input[input.index("nearby tickets:")+1:]:
        tickets.append([int(v) for v in t.split(",")])
    return tickets

def get_my_ticket(input):
    return [int(v) for v in input[input.index("your ticket:")+1].split(",")]

def calc_index_for_ranges(ranges, tickets, occ_indexes):
    possible_indexes = {i for i in range(len(tickets[0]))} - occ_indexes

    for ticket in tickets:
        for idx, value in enumerate(ticket):
            valid = False
            for field_range in ranges:
                if value in field_range:
                    valid = True
            if not valid and idx in possible_indexes:
                possible_indexes.remove(idx)
    
    return possible_indexes

def calc_ticket_error(ticket, ranges):
    error_sum = 0
    error = False
    for value in ticket:
        is_valid = False
        for field_ranges in ranges:
            for field_range in field_ranges:
                if value in field_range:
                    is_valid = True
                    break
        if not is_valid:
            error = True
            error_sum += value
    return error, error_sum


script_dir = os.path.dirname(__file__)
with open(script_dir + "/input", "r") as myInput:
    start_time = time.time()
    input = [line.strip() for line in myInput]
    solve_1(input)
    solve_2(input)
    print("--- Execution time %s s ---" % (time.time() - start_time))
