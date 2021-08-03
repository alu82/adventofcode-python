import os
import time

subject_number = 7
modulo = 20201227
card_public_key = 8184785
door_public_key = 5293040

def solve_1():
    card_loop_size = find_loop_size(card_public_key)
    door_loop_size = find_loop_size(door_public_key)

    print(generate_encryption_key(card_public_key, door_loop_size))
    print(generate_encryption_key(door_public_key, card_loop_size))

def solve_2(input):
    pass

def find_loop_size(public_key):
    value = 1
    loop_size = 0
    while value != public_key:
        value = (value * subject_number)%modulo
        loop_size += 1
    return loop_size

def generate_encryption_key(public_key, loop_size):
    return pow(public_key, loop_size, modulo)

solve_1()