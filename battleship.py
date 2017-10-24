# codecademy battleship game variation
from random import randint

board_player1 = []
board_player2 = []

for x in range(5):
    board_player1.append(["O"] * 5)
    board_player2.append(["O"] * 5)


def print_board(board):
    for row in board:
        print(" ".join(row))





def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row_player1 = random_row(board_player1)
ship_col_player1 = random_col(board_player1)

ship_row_player2 = random_row(board_player2)
ship_col_player2 = random_row(board_player2)

print_board(board_player1)
print("Player 1 Row:", ship_row_player1)
print("Player 1 Col:", ship_col_player1)
print("\n")

print_board(board_player2)
print("Player 2 Row:", ship_row_player2)
print("Player 2 Col:", ship_col_player2)
print("\n")

# Everything from here on should be in your for loop
# don't forget to properly indent!

for turn in range(8):
    if turn % 2 == 0:
        print("Round", turn // 2 + 1, "\n")
        print("Player 1: Turn", turn // 2 + 1)
        guess_row_p1 = int(input("Guess Row: "))
        guess_col_p1 = int(input("Guess Col: "))

        if guess_row_p1 == ship_row_player2 and guess_col_p1 == ship_col_player2:
            print("Congratulations, Player 1! You sank my battleship!")
            board_player2[guess_row_p1][guess_col_p1] = "$"
            # print_board(board)
            break
        else:
            if guess_row_p1 not in range(5) or \
                            guess_col_p1 not in range(5):
                print("Oops, that's not even in the ocean.")
            elif board_player2[guess_row_p1][guess_col_p1]== "X":
                print("You guessed that one already.")
            else:
                print("You missed my battleship, Player 1!")
                board_player2[guess_row_p1][guess_col_p1] = "X"
            print("Player 2's Board")
            print_board(board_player2)
            print("\n")
            if turn == 6:
                print("Player 1, you are out of turns.", "\n")

    else:
        print("Player 2: Turn", turn // 2 + 1)
        guess_row_p2 = int(input("Guess Row: "))
        guess_col_p2 = int(input("Guess Col: "))

        if guess_row_p2 == ship_row_player1 and guess_col_p2 == ship_col_player1:
            print("Congratulations, Player 2! You sank my battleship!")
            board_player1[guess_row_p2][guess_col_p2] = "$"
            # print_board(board)
            break
        else:
            if guess_row_p2 not in range(5) or \
                            guess_col_p2 not in range(5):
                print("Oops, that's not even in the ocean, Player 2.")
            elif board_player1[guess_row_p2][guess_col_p2] == "X":
                print("You guessed that one already, Player 2.")
            else:
                print("You missed my battleship, Player 2!")
                board_player1[guess_row_p2][guess_col_p2] = "X"
            print("Player 1's Board")
            print_board(board_player1)
            print("\n")
            if turn == 7:
                print("Player 2, you are out of turns.", "\n")
                print("The game was a draw!")
