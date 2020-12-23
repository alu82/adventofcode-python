class Cup:    
    def __init__(self, label):     
        self.label = label
        self.ncup = None    
        self.pcup = None 

class CupGame:
    def __init__(self, start_cups, length):
        self.cups = dict()

        first_cup = None
        prev_cup = None
        for n in start_cups:
            current_cup = Cup(n)
            current_cup.pcup = prev_cup
            
            if first_cup is None:
                first_cup = current_cup
            if prev_cup is not None:
                prev_cup.ncup = current_cup 
            
            prev_cup = current_cup
            self.cups[n] = current_cup
        
        if len(start_cups) < length:
            for n in range(max(start_cups)+1, length+1):
                current_cup = Cup(n)
                current_cup.pcup = prev_cup
                prev_cup.ncup = current_cup
                prev_cup = current_cup
                self.cups[n] = current_cup
        
        first_cup.pcup = prev_cup
        prev_cup.ncup = first_cup
        self.max_label = max(len(start_cups), prev_cup.label)
        
    def get_next_destination(self, cup):
        pick_ups = [cup.ncup.label,cup.ncup.ncup.label,cup.ncup.ncup.ncup.label]
        next_possible_label = cup.label - 1
        while next_possible_label not in self.cups or next_possible_label in pick_ups:
            next_possible_label = next_possible_label - 1 if next_possible_label > 0 else self.max_label
        return self.cups[next_possible_label]
    
    def move_pickups(self, source_cup, destination_cup):
        pick_up_cup_1 = source_cup.ncup
        pick_up_cup_3 = source_cup.ncup.ncup.ncup
        next_cup = pick_up_cup_3.ncup

        source_cup.ncup = next_cup
        next_cup.pcup = source_cup

        after_dest_cup = destination_cup.ncup
        destination_cup.ncup = pick_up_cup_1
        pick_up_cup_1.pcup = destination_cup
        pick_up_cup_3.ncup = after_dest_cup
        after_dest_cup.pcup = pick_up_cup_3

def solve_2():
    input = "198753462"
    cups = [int(n) for n in input]
    
    cup_game = CupGame(cups, 1_000_000)
    
    moves = 10_000_000
    start = cups[0]

    current_cup = cup_game.cups[start]
    for n in range(moves):       
        dest_cup = cup_game.get_next_destination(current_cup)
        cup_game.move_pickups(current_cup, dest_cup)
        current_cup = current_cup.ncup
        
    cup_1 = cup_game.cups[1].ncup.label
    cup_2 = cup_game.cups[1].ncup.ncup.label
    print(cup_1, cup_2, cup_1*cup_2)

def get_destination(current, cups):
    destination = current - 1
    while destination not in cups:
        destination = destination - 1 if destination > 1 else max(cups)
    return destination

def solve_1():
    input = "198753462"
    cups = [int(n) for n in input]
    moves = 100
    c_pos = 0
    for _ in range(moves):
        c_cup = cups[c_pos]
        pick_ups = [cups[(c_pos+i)%len(cups)] for i in range(1,4)]
        
        for pick_up in pick_ups:
            cups.remove(pick_up)
        
        dest = get_destination(c_cup, cups)
        dest_index = cups.index(dest) + 1
        for pick_up in pick_ups[::-1]:
            cups.insert(dest_index, pick_up)
        c_pos = (cups.index(c_cup) + 1)%len(cups)

    solution = "".join([str(cups[(cups.index(1)+i)%len(cups)]) for i in range(1,len(cups))])
    print("part 1", solution)

solve_1()
solve_2()



