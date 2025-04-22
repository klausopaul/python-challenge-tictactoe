from random import randrange
import os


def cls():
    os.system("cls" if os.name == "nt" else "clear")


# -------------------------------------------------------------------------
def top_line_board():

    for i in range(1, 4):
        print("+", end="")
        print("-" * 7, end="")
    print("+")

    for i in range(1, 4):
        print("|", end="")
        print(" " * 7, end="")
    print("|")


def bottom_line_board():

    for i in range(1, 4):
        print("|", end="")
        print(" " * 7, end="")
    print("|")


def final_line_board():

    for i in range(1, 4):
        print("+", end="")
        print("-" * 7, end="")
    print("+")


# -------------------------------------------------------------------------
def print_number_in_row(board, row):

    # print first number of the first column of the passed row
    print("|", " " * 1, board[row][0], " " * 1, "|", end="")

    # print the other numbers from columns 2 and 3 of the passed row
    for j in range(1, 3):
        print(" " * 2, board[row][j], " " * 1, "|", end="")
        # on the last column, print a new line
        if j == 2:
            print()


# -------------------------------------------------------------------------
def display_board(board):

    # print()
    # print("Current board status")
    top_line_board()
    print_number_in_row(board, 0)
    bottom_line_board()

    top_line_board()
    print_number_in_row(board, 1)
    bottom_line_board()

    top_line_board()
    print_number_in_row(board, 2)
    bottom_line_board()

    final_line_board()


# -------------------------------------------------------------------------
def print_invalid_input_msg():

    print("Oops..Valid values are from 1 to 9.")
    print()


def print_occupied_msg():

    print("Position is taken")
    print()


# -------------------------------------------------------------------------
def is_input_between_range(play_input_to_int):

    if play_input_to_int > 0 and play_input_to_int < 10:
        return True
    else:
        return False


# -------------------------------------------------------------------------
def change_board_value(board, play_input_to, map_play_input_to_board, player):

    board_coordinates = map_play_input_to_board[play_input_to]
    row = board_coordinates[0]
    column = board_coordinates[1]
    if player == "user":
        board[row][column] = "O"
    else:
        board[row][column] = "X"  # computer is playing


# -------------------------------------------------------------------------
def is_position_free(play_input_to, map_play_input_to_board, free_positions):

    board_coordinates = map_play_input_to_board[play_input_to]
    if board_coordinates in free_positions:
        return board_coordinates
    else:
        return -1


# -------------------------------------------------------------------------
def remove_free_position(free_positions, val):

    free_positions.remove(val)


# -------------------------------------------------------------------------
def calculate_result_of_play(
    board, play_input_to_int, map_play_input_to_board, free_positions, user
):

    # position is free
    coord = is_position_free(play_input_to_int, map_play_input_to_board, free_positions)

    # coord == -1 means the position played is not free
    if coord != -1:
        # change value of board
        change_board_value(board, play_input_to_int, map_play_input_to_board, user)
        # remove the position from the free positions
        remove_free_position(free_positions, coord)
        # tell the play was good
        return 0
    else:
        # position is occupied
        return -1


# -------------------------------------------------------------------------
def enter_move(board, map_play_input_to_board, free_positions):

    play_input = input("Pick the position of your move: ")
    try:
        play_input_to_int = int(play_input)
    except ValueError:
        if play_input.upper() == "Q":
            print("Exiting game...")
            return -3
        else:
            print_invalid_input_msg()
    else:
        if is_input_between_range(play_input_to_int):
            result = calculate_result_of_play(
                board,
                play_input_to_int,
                map_play_input_to_board,
                free_positions,
                "user",
            )
            if result == -1:
                print_occupied_msg()
                return -1  # give user another change, not letting computer play
            else:
                return 0  # let computer play
        else:
            print_invalid_input_msg()
            return -1  # give user another change, not letting computer play


# -------------------------------------------------------------------------
def computer_enter_move(board, map_play_input_to_board, free_positions):

    choosing = True
    while choosing:
        play_input = randrange(1, 10)

        result = calculate_result_of_play(
            board, play_input, map_play_input_to_board, free_positions, "computer"
        )

        if result == -1:
            # print ('Computer played a occupied position')
            choosing = True
        else:
            print("Computer has played")
            choosing = False


# -------------------------------------------------------------------------
def return_game_status(game_board):
    results = []

    # Rows
    sr1 = set()
    sr2 = set()
    sr3 = set()

    # Columns
    sc1 = set()
    sc2 = set()
    sc3 = set()

    # Diagonals
    sd1 = set()
    sd2 = set()

    # Check Rows
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if i == 0:
                sr1.add(game_board[i][j])
            elif i == 1:
                sr2.add(game_board[i][j])
            elif i == 2:
                sr3.add(game_board[i][j])

    results.append((sr1, len(sr1)))
    results.append((sr2, len(sr2)))
    results.append((sr3, len(sr3)))

    # Check Columns
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if i == 0:
                sc1.add(game_board[j][i])
            elif i == 1:
                sc2.add(game_board[j][i])
            elif i == 2:
                sc3.add(game_board[j][i])

    results.append((sc1, len(sc1)))
    results.append((sc2, len(sc2)))
    results.append((sc3, len(sc3)))

    # Check diagonal #1
    for i in range(len(game_board)):
        sd1.add(game_board[i][i])

    results.append((sd1, len(sd1)))

    # Check diagonal #2
    c = 2
    for i in range(len(game_board)):
        sd2.add(game_board[i][c])
        c -= 1

    results.append((sd2, len(sd2)))

    wh = 0
    wc = 0
    tie = 0
    for t in results:
        if t[1] == 1:
            if "O" in t[0]:
                wh = 1
            elif "X" in t[0]:
                wc = 1
        if t[1] == 2:
            tie += 1

    # print ('wh ', wh)
    # print ('wc ', wc)
    # print ('tie ', tie)

    if wh == 1:
        return "H"  # ('Human wins!')
    elif wc == 1:
        return "C"  # ('Computer wins')
    elif tie == 8:
        return "T"  # ('The game was a tie')
    else:
        return "P"  # ('Game in progress...')


def print_results(game_status):
    if game_status != "P":
        if game_status == "H":
            print("Human wins!")
        elif game_status == "C":
            print("Computer wins")
        elif game_status == "T":
            print("The game was a tie")
        return True


# -----------------------------------------------------------------------------------------------
# Main routine
# -----------------------------------------------------------------------------------------------
# Initial board state at the beginning of every game
game_board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

# maps input to coordinates in the board
map_play_input_to_board_coord = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
}

# Initial free positions, except position 5, coordinates (1,1)
free_positions = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]

# Initial state of the game
end_of_game = False

# Now, to clear the screen
cls()
print()
print("Welcome to Tic-Tac-Toe.")
print("You can exit the game at any time by entering q or Q.")
print('The computer is playing "X" and it has already started.')

display_board(game_board)

# Start the gamea
while not (end_of_game):
    # Enter user's move
    results = enter_move(game_board, map_play_input_to_board_coord, free_positions)

    game_status = return_game_status(game_board)

    end_of_game = print_results(game_status)

    # If user move was ok (results == 0) then let computer play
    if results == 0 and game_status == "P":
        # Computer's move
        computer_enter_move(game_board, map_play_input_to_board_coord, free_positions)

        game_status = return_game_status(game_board)

        end_of_game = print_results(game_status)

    elif results == -3:  # user quit the game in progress
        end_of_game = True

    # Display board state
    display_board(game_board)

    # cosmetic separator between plays
    print(" " * 40)
