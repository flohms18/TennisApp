import random as rd
# Si tu veux la touche espace, installe 'keyboard' et décommente :
# import keyboard

def play_point():
    """Simule un point et retourne le gagnant (0 = P1, 1 = P2)."""
    return rd.randint(0, 1)

def play_game():
    """Simule un jeu complet et retourne le gagnant (0 = P1, 1 = P2)."""
    ScoreBoard = ["0", "15", "30", "40", "A"]
    P1Score, P2Score = 0, 0

    while True:
        # Interaction : appuie sur Entrée
        input("Appuie sur Entrée pour jouer un point...")

        # Si tu veux la touche espace :
        # print("Appuie sur ESPACE pour jouer un point...")
        # keyboard.wait("space")

        point = play_point()
        if point == 0:
            P1Score += 1
            print("➡️ Point Player 1")
        else:
            P2Score += 1
            print("➡️ Point Player 2")

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
            print("🏆 Player 1 wins the game")
            return 0
        elif P2Score >= 4 and P2Score - P1Score >= 2:
            print("🏆 Player 2 wins the game")
            return 1

def play_set():
    """Simule un set complet et retourne le gagnant (0 = P1, 1 = P2)."""
    GameP1, GameP2 = 0, 0

    while True:
        winner = play_game()
        if winner == 0:
            GameP1 += 1
        else:
            GameP2 += 1

        print(f"Games: Player 1 = {GameP1}, Player 2 = {GameP2}")

        # Conditions de victoire du set
        if GameP1 >= 6 and GameP1 - GameP2 >= 2:
            print("🎉 Player 1 wins the set")
            return 0
        elif GameP2 >= 6 and GameP2 - GameP1 >= 2:
            print("🎉 Player 2 wins the set")
            return 1

def match():
    """Simule un match en 3 sets gagnants."""
    SetP1, SetP2 = 0, 0

    while SetP1 < 3 and SetP2 < 3:
        winner = play_set()
        if winner == 0:
            SetP1 += 1
        else:
            SetP2 += 1

        print(f"Sets: Player 1 = {SetP1}, Player 2 = {SetP2}")

    # Victoire du match
    if SetP1 == 3:
        print("🏆🏆🏆 Player 1 wins the match!")
    else:
        print("🏆🏆🏆 Player 2 wins the match!")

# Lancer la simulation
match()