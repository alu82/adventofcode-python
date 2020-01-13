import os

DEAL_INTO_NEW_STACK = "deal into new stack"
DEAL_WITH_INCREMENT = "deal with increment "
CUT = "cut "

class CardShuffle:

    def __init__(self, numberOfCards, card):
        self.numberOfCards = numberOfCards
        self.card = card

    def dealIntoNewStack(self):
        self.card = (self.numberOfCards - self.card - 1)%self.numberOfCards
        
    def cutCards(self, n):
        self.card = (self.card + self.numberOfCards - n)%self.numberOfCards

    def dealWithIncrement(self, increment):
        self.card = (self.card*increment)%self.numberOfCards

def part1(cmds):
    cards = CardShuffle(10007, 2019)
    for cmd in cmds:
        if cmd.startswith(DEAL_INTO_NEW_STACK):
            cards.dealIntoNewStack()
        elif cmd.startswith(DEAL_WITH_INCREMENT):
            increment = int(cmd[len(DEAL_WITH_INCREMENT):])
            cards.dealWithIncrement(increment)
        elif cmd.startswith(CUT):
            n = int(cmd[len(CUT):])
            cards.cutCards(n)

    return cards.card
    
def part2(cmds):
    cards = CardShuffle(119315717514047, 2020)
    #cmds = 101741582076661*cmds
    for _ in range(4):
        print(cards.card)
        for cmd in cmds:
            if cmd.startswith(DEAL_INTO_NEW_STACK):
                cards.dealIntoNewStack()
            elif cmd.startswith(DEAL_WITH_INCREMENT):
                increment = int(cmd[len(DEAL_WITH_INCREMENT):])
                cards.dealWithIncrement(increment)
            elif cmd.startswith(CUT):
                n = int(cmd[len(CUT):])
                cards.cutCards(n)
            
    return cards.card


# Open input files and get intcodeprogram
script_dir = os.path.dirname(__file__)
with open(script_dir + "/input", "r") as myInput:
    cmds = myInput.readlines()

    print(part1(cmds)) # 2496
    #print(part2(cmds))