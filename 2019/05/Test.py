import os

def auslesenInstractionAndMode (intmode):
    op=intmode%100
    restmodezahl=intmode//100
    if op==3 or op==4:
        return (op, restmodezahl)
    mode1=restmodezahl% 10
    restmodezahl=restmodezahl//10
    mode2=restmodezahl% 10
    mode3=restmodezahl//10
    return (op, mode1, mode2, mode3)


print(auslesenInstractionAndMode(1101))

