import random as rd

def tossing():
    print("Welcome players")
    TH = rd.randint(0,1)
    if TH == 0:
        print("It's Head!")
        print("P1! You serve! P2 You receive")
    else:
        print("It's Tail")
        print("P2! You serve! P1 You receive")
