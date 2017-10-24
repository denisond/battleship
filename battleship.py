# battleships. battleships? i ain't playing games bitch. gat'll click, gravel pit, that'll be ya grave bitch.
from random import randint

board_player1 = []
board_player2 = []

for x in range(5):#create 2D list for each player, each with 5 sublists of 5 "O"'s
    board_player1.append(["O"] * 5)
    board_player2.append(["O"] * 5)


def print_board(board):#fcn to create battleship board
    for row in board:
        print(" ".join(row))


def random_row(board):#fcn to create the starting row for each player's battleship
    return randint(0, len(board) - 1)

ship_row_player1 = random_row(board_player1)
ship_row_player2 = random_row(board_player2)


def random_col(board):#fcn to create the starting column for each player's battleship
    return randint(0, len(board[0]) - 1)

ship_col_player1 = random_col(board_player1)
ship_col_player2 = random_col(board_player2)

#fcn below assigns orientation for battleship. if 0, battleship extends rightward from point determined by fcn's above; if 1, battleship extends downward.
def random_orientation(board):
    return randint(0,1)

ship_orient_player1 = random_orientation(board_player1)
ship_orient_player2 = random_orientation(board_player2)

#fcn to assign length to battleship such that whole battleship is on the board.
def random_length(ship_orient, ship_row, ship_col):
    if ship_orient == 0:
        return randint(1, (5  - ship_col))
    else:
        return randint(1, (5 - ship_row))

ship_len_player1 = random_length(ship_orient_player1, ship_row_player1, ship_col_player1)
ship_len_player2 = random_length(ship_orient_player2, ship_row_player2, ship_col_player2)

#large block comments below added so information on battleship location isn't displayed to each player.

print("Player 1's Board")
print_board(board_player1)
print("Player 1 Row:", ship_row_player1)
print("Player 1 Col:", ship_col_player1)
print("Player 1 Orient:", ship_orient_player1)
print("Player 1 Length:", ship_len_player1)
print("\n")

print("Player 2's Board")
print_board(board_player2)
print("Player 2 Row:", ship_row_player2)
print("Player 2 Col:", ship_col_player2)
print("Player 2 Orient:", ship_orient_player2)
print("Player 2 Length:", ship_len_player2)
print("\n")


for turn in range(10):
    if turn % 2 == 0:
        print("Round", turn // 2 + 1, "\n")
        print("Player 1: Turn", turn // 2 + 1)
        guess_row_p1 = int(input("Guess Row: "))
        guess_col_p1 = int(input("Guess Col: "))
        print("\n")
        if ship_orient_player2 == 0:
            if guess_row_p1 == ship_row_player2 and guess_col_p1 in range(ship_col_player2, ship_col_player2 + ship_len_player2):
                if board_player2[guess_row_p1][guess_col_p1] != "$":
                    print("You hit my battleship, Player 1!")
                    board_player2[guess_row_p1][guess_col_p1] = "$"
                    if str(board_player2).count("$") == ship_len_player2:
                        print("Player 2's Board")
                        print_board(board_player2)
                        print("You sank my battleship, Player 1!", "\n")
                        print("Player 1 Wins!!!")
                        break
                elif board_player2[guess_row_p1][guess_col_p1] == "$":
                    print("You guessed that one correctly already.")
                print("Player 2's Board")
                print_board(board_player2)
            else:
                if guess_row_p1 not in range(5) or \
                                guess_col_p1 not in range(5):
                    print("Oops, that's not even in the ocean, Player 1.")

                elif board_player2[guess_row_p1][guess_col_p1] == "X":
                    print("You guessed that one incorrectly already, Player 1.")
                else:
                    print("You missed my battleship, Player 1!")
                    board_player2[guess_row_p1][guess_col_p1] = "X"
                print("Player 2's Board")
                print_board(board_player2)
                print("\n")
                if turn == 8:
                    print("Player 1, you are out of turns.", "\n")
        elif ship_orient_player2 == 1:
            if guess_col_p1 == ship_col_player2 and guess_row_p1 in range(ship_row_player2, ship_row_player2 + ship_len_player2):
                if board_player2[guess_row_p1][guess_col_p1] != "$":
                    print("You hit my battleship, Player 1!")
                    board_player2[guess_row_p1][guess_col_p1] = "$"
                    if str(board_player2).count("$") == ship_len_player2:
                        print("Player 2's Board")
                        print_board(board_player2)
                        print("You sank my battleship, Player 1!", "\n")
                        print("Player 1 Wins!!!")
                        break
                elif board_player2[guess_row_p1][guess_col_p1] == "$":
                    print("You guessed that one correctly already.")
                print("Player 2's Board")
                print_board(board_player2)
            else:
                if guess_row_p1 not in range(5) or \
                                guess_col_p1 not in range(5):
                    print("Oops, that's not even in the ocean.")

                elif board_player2[guess_row_p1][guess_col_p1] == "X":
                    print("You guessed that one incorrectly already.")
                else:
                    print("You missed my battleship, Player 1!")
                    board_player2[guess_row_p1][guess_col_p1] = "X"
                print("Player 2's Board")
                print_board(board_player2)
                print("\n")
                if turn == 8:
                    print("Player 1, you are out of turns.", "\n")


    elif turn % 2 != 0:
        print("Player 2: Turn", turn // 2 + 1)
        guess_row_p2 = int(input("Guess Row: "))
        guess_col_p2 = int(input("Guess Col: "))
        print("\n")
        if ship_orient_player1 == 0:
            if guess_row_p2 == ship_row_player1 and guess_col_p2 in range(ship_col_player1, ship_col_player1 + ship_len_player1):
                if board_player1[guess_row_p2][guess_col_p2] != "$":
                    print("You hit my battleship, Player 2!")
                    board_player1[guess_row_p2][guess_col_p2] = "$"
                    if str(board_player1).count("$") == ship_len_player1:
                        print("Player 1's Board")
                        print_board(board_player1)
                        print("You sank my battleship, Player 2!", "\n")
                        print("Player 2 Wins!!!")
                        break
                elif board_player1[guess_row_p2][guess_col_p2] == "$":
                    print("You guessed that one correctly already.")
                print("Player 1's Board")
                print_board(board_player1)
            else:
                if guess_row_p2 not in range(5) or \
                                guess_col_p2 not in range(5):
                    print("Oops, that's not even in the ocean, Player 2.")
                elif board_player1[guess_row_p2][guess_col_p2] == "X":
                    print("You guessed that one incorrectly already, Player 2.")
                else:
                    print("You missed my battleship, Player 2!")
                    board_player1[guess_row_p2][guess_col_p2] = "X"
                print("Player 1's Board")
                print_board(board_player1)
                print("\n")
                if turn == 9:
                    print("Player 2, you are out of turns.", "\n")
                    print("The game was a draw!")
        elif ship_orient_player1 == 1:
            if guess_col_p2 == ship_col_player1 and guess_row_p2 in range(ship_row_player1, ship_row_player1 + ship_len_player1):
                if board_player1[guess_row_p2][guess_col_p2] != "$":
                    print("You hit my battleship, Player 2!")
                    board_player1[guess_row_p2][guess_col_p2] = "$"
                    if str(board_player1).count("$") == ship_len_player1:
                        print("Player 1's Board")
                        print_board(board_player1)
                        print("You sank my battleship, Player 2!", "\n")
                        print("Player 2 Wins!!!")
                        break
                elif board_player1[guess_row_p2][guess_col_p2] == "$":
                    print("You guessed that one correctly already.")
                print("Player 1's Board")
                print_board(board_player1)
            else:
                if guess_row_p2 not in range(5) or \
                                guess_col_p2 not in range(5):
                    print("Oops, that's not even in the ocean.")

                elif board_player1[guess_row_p2][guess_col_p2] == "X":
                    print("You guessed that one incorrectly already.")
                else:
                    print("You missed my battleship, Player 1!")
                    board_player1[guess_row_p2][guess_col_p2] = "X"
                print("Player 1's Board")
                print_board(board_player1)
                print("\n")
                if turn == 9:
                    print("Player 2, you are out of turns.", "\n")

