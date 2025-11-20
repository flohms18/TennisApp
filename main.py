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

def match():
    ScoreBoard = ["0","15","30","40","A"]
    P1Score = 0
    P2Score = 0
    GameP1 = 0
    GameP2 = 0
    Point = rd.randint(0,1)
    if Point == 0:
        P1Score += 1
    elif Point == 1:
        P2Score += 1
    if P1Score == 4 and P1Score - P2Score >= 2:
        print("Player 1 wins the game")
        GameP1 =+ 1
    elif P2Score == 4 and P2Score - P1Score >= 2:
        print("Player 2 wins the game")
        GameP2 =+ 1
    


