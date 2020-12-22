import os
import time

def solve_1(input):
    deck_1 = [int(p) for p in input[0] if not p.startswith("Player")]
    deck_2 = [int(p) for p in input[1] if not p.startswith("Player")]

    while len(deck_1) > 0 and len(deck_2) > 0:
        card_1 = deck_1.pop(0)
        card_2 = deck_2.pop(0)

        if card_1 > card_2:
            deck_1.append(card_1)
            deck_1.append(card_2)
        else:
            deck_2.append(card_2)
            deck_2.append(card_1)

    winner = deck_1 if len(deck_1) > 0 else deck_2
    return winning_score(winner)

def solve_2(input):
    deck_1 = [int(p) for p in input[0] if not p.startswith("Player")]
    deck_2 = [int(p) for p in input[1] if not p.startswith("Player")]
    return max([winning_score(deck) for deck in combat(deck_1, deck_2)])

def winning_score(deck):
    solution = 0
    for idx, value in enumerate(deck[::-1]):
        solution += (value * (idx+1))
    return solution

def combat(deck_1, deck_2):
    rounds = list()
    while len(deck_1) > 0 and len(deck_2) > 0:
        round = (deck_1.copy(), deck_2.copy())
        if round in rounds:
            return deck_1, deck_2
        else:
            rounds.append(round)

        card_1 = deck_1.pop(0)
        card_2 = deck_2.pop(0)
        if len(deck_1) < card_1 or len(deck_2) < card_2:
            if card_1 > card_2:
                deck_1.append(card_1)
                deck_1.append(card_2)
            else:
                deck_2.append(card_2)
                deck_2.append(card_1)
            
            if len(deck_1) == 0 or len(deck_2) == 0:
                return deck_1, deck_2
        else:
            sub_deck_1, sub_deck_2 = combat(deck_1[:card_1], deck_2[:card_2])
            if len(sub_deck_1) > 0 or (len(sub_deck_1) > 0 and len(sub_deck_2) > 0):
                deck_1.append(card_1)
                deck_1.append(card_2)
            else:
                deck_2.append(card_2)
                deck_2.append(card_1)

with open(os.path.dirname(__file__) + "/input", "r") as myInput:
    start_time = time.time()
    input = [block.splitlines() for block in myInput.read().split("\n\n")]
    print(solve_1(input))
    print(solve_2(input))
    print("--- Execution time %s s ---" % (time.time() - start_time))