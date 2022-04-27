def rps():
    possibilites = ['scissors', 'paper', 'rock']

    score1 = 0
    score2 = 0

    while score1 < 2 and score2 < 2:
        player1 = input("Ingrese opcion J1: ")
        player2 = input("Ingrese opcion J2: ")

        if (player1 == possibilites[0] and player2 == possibilites[1] or
                player1 == possibilites[1] and player2 == possibilites[2] or
                player1 == possibilites[2] and player2 == possibilites[0]):
            score1 += 1
        elif player1 == player2:
            continue
        else:
            score2 += 1

    if score1 > score2:
        return "Player1 wins"
    else:
        return "Player2 wins"


def main():
    winner = rps()
    print(winner)


if __name__ == '__main__':
    main()
