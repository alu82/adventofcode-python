import time

def memory_game(input, turns):
    starting_numbers = [int(n) for n in input.split(",")]
    number_indexes = {}
    for t in range(turns):
        if t < len(starting_numbers):
            number_indexes[starting_numbers[t]] = [None, t]
            last_number = starting_numbers[t]
        else:
            # calculate new number
            ll_idx, l_idx = number_indexes.get(last_number, [None, t])
            new_number = 0
            if ll_idx is not None:
                new_number = l_idx - ll_idx
            last_number = new_number

            # calculate indexes of new number
            new_index = [None, t]
            if new_number in number_indexes:
                _ , n_idx = number_indexes[new_number]
                new_index = [n_idx, t]
            number_indexes[new_number] = new_index 
               
    return new_number

start_time = time.time()
input = "14,3,1,0,9,5"
print(memory_game(input, 2020))
print(memory_game(input, 30000000))
print("--- Execution time %s s ---" % (time.time() - start_time))