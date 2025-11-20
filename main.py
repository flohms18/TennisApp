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

import random as rd

def match():
    ScoreBoard = ["0", "15", "30", "40", "A"]
    P1Score = 0
    P2Score = 0
    GameP1 = 0
    GameP2 = 0

    while GameP1 < 6 and GameP2 < 6:
        P1Score, P2Score = 0, 0  # reset scores for each game

        while True:
            Point = rd.randint(0, 1)
            if Point == 0:
                P1Score += 1
            else:
                P2Score += 1

            # Affichage du score
            if P1Score >= 3 and P2Score >= 3:
                if P1Score == P2Score:
                    print("Score: Deuce")
                elif P1Score == P2Score + 1:
                    print("Score: Advantage Player 1")
                elif P2Score == P1Score + 1:
                    print("Score: Advantage Player 2")
            else:
                print(f"Score: {ScoreBoard[min(P1Score, 4)]} - {ScoreBoard[min(P2Score, 4)]}")

            # Conditions de victoire du jeu
            if P1Score >= 4 and P1Score - P2Score >= 2:
                print("Player 1 wins the game")
                GameP1 += 1
                break
            elif P2Score >= 4 and P2Score - P1Score >= 2:
                print("Player 2 wins the game")
                GameP2 += 1
                break

        print(f"Games: Player 1 = {GameP1}, Player 2 = {GameP2}")

    # Victoire du set
    if GameP1 >= 6 and GameP1 - GameP2 >= 2:
        print("Player 1 wins the set")
    elif GameP2 >= 6 and GameP2 - GameP1 >= 2:
        print("Player 2 wins the set")
    
    


