import os
import time
import itertools as it

def solve_1(input):
    memory, mask = dict(), ""
    for command in input:
        if command.startswith("mask ="):
            mask = command[7:]
        elif command.startswith("mem["):
            address, value = parse_write_command(command)
            memory[address] = mask_value(mask, value)
    print(sum(memory.values()))

def solve_2(input):
    memory, mask = dict(), ""
    for command in input:
        if command.startswith("mask ="):
            mask = command[7:]
        elif command.startswith("mem["):
            address, value = parse_write_command(command)
            for addr in mask_address(mask, address):
                memory[addr] = value      
    print(sum(memory.values()))

def parse_write_command(command):
    address = int(command[command.index("[")+1:command.index("]")])
    value = int(command[command.index("=")+2:])
    return address, value

def mask_value(mask, value):
    bins = list(format(value, "0" + str(len(mask)) + "b"))
    for idx, val in enumerate(mask):
        if val in ("0", "1"):
            bins[idx] = val
    return int("".join(bins),2)

def mask_address(mask, address):
    bins = list(format(address, "0" + str(len(mask)) + "b"))
    x_pos = list()
    for idx, val in enumerate(mask):
        if val == "1":
            bins[idx] = val
        elif val == "X":
            x_pos.append(idx)

    addresses = set()
    for p in list(it.product(['0', '1'], repeat=len(x_pos))):
        masked_address = bins.copy()
        for idx, pos in enumerate(x_pos):
            masked_address[pos] = p[idx]
        addresses.add(int("".join(masked_address),2))
    return addresses


script_dir = os.path.dirname(__file__)
with open(script_dir + "/input", "r") as myInput:
    start_time = time.time()
    input = [line.strip() for line in myInput]
    solve_1(input)
    solve_2(input)
    print("--- Execution time %s s ---" % (time.time() - start_time))