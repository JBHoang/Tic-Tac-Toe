import random

# initializing a blank board
game_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
# if condition_repeat is changed to 0, it means a user or player has already selected that spot
condition_repeat = [1, 1, 1, 1, 1, 1, 1, 1, 1]

# prints the current board
def print_current_board(board):
    print("")
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])

# user selects a number and it places X to the corresponding number
def place_move_on_board(board):
    print("")
    print("Enter a number from 1-9:")
    player_move = input()

    if int(player_move) == 1 and condition_repeat[0] == 1:
        board[0] = "X"
        condition_repeat[0] = 0

    elif int(player_move) == 2 and condition_repeat[1] == 1:
        board[1] = "X"
        condition_repeat[1] = 0

    elif int(player_move) == 3 and condition_repeat[2] == 1:
        board[2] = "X"
        condition_repeat[2] = 0

    elif int(player_move) == 4 and condition_repeat[3] == 1:
        board[3] = "X"
        condition_repeat[3] = 0

    elif int(player_move) == 5 and condition_repeat[4] == 1:
        board[4] = "X"
        condition_repeat[4] = 0

    elif int(player_move) == 6 and condition_repeat[5] == 1:
        board[5] = "X"
        condition_repeat[5] = 0

    elif int(player_move) == 7 and condition_repeat[6] == 1:
        board[6] = "X"
        condition_repeat[6] = 0

    elif int(player_move) == 8 and condition_repeat[7] == 1:
        board[7] = "X"
        condition_repeat[7] = 0

    elif int(player_move) == 9 and condition_repeat[8] == 1:
        board[8] = "X"
        condition_repeat[8] = 0
    else:
        print("invalid move , try again")
        print("")
        place_move_on_board(board)

    print_current_board(board)

# checks to see if the game is over win, draw, or loss: returns 0-win 1-loss 2-draw
def is_game_over(board):

    # check rows X
    if (board[0] == "X" and board[1] == "X" and board[2]) == "X":
        return 0
    if (board[3] == "X" and board[4] == "X" and board[5]) == "X":
        return 0
    if (board[6] == "X" and board[7] == "X" and board[8]) == "X":
        return 0

    # check columns X
    if (board[0] == "X" and board[3] == "X" and board[6]) == "X":
        return 0
    if (board[1] == "X" and board[4] == "X" and board[7]) == "X":
        return 0
    if (board[2] == "X" and board[5] == "X" and board[8]) == "X":
        return 0

    # check diagonal X
    if (board[0] == "X" and board[4] == "X" and board[8]) == "X":
        return 0
    if (board[2] == "X" and board[4] == "X" and board[6]) == "X":
        return 0

    # check rows O
    if (board[0] == "O" and board[1] == "O" and board[2]) == "O":
        return 1
    if (board[3] == "O" and board[4] == "O" and board[5]) == "O":
        return 1
    if (board[6] == "O" and board[7] == "O" and board[8]) == "O":
        return 1

    # check columns O
    if (board[0] == "O" and board[3] == "O" and board[6]) == "O":
        return 1
    if (board[1] == "O" and board[4] == "O" and board[7]) == "O":
        return 1
    if (board[2] == "O" and board[5] == "O" and board[8]) == "O":
        return 1

    # check diagonal O
    if (board[0] == "O" and board[4] == "O" and board[8]) == "O":
        return 1
    if (board[2] == "O" and board[4] == "O" and board[6]) == "O":
        return 1

    # if board is filled with X and O and no player won, then it returns 2 which is a draw
    if (board[0] != " " and board[1] != " " and board[2] != " " and board[3] != " " and board[4] != " " and board[5] != " " and board[6] != " " and board[7] != " " and board[8] != " "):
        return 2

    # game is not over, continue playing
    return 3

# checks all legal moves
def legal_moves(board):
    legal_move_list = [] # creates an empty list

    i = 0
    for empty in board:
        if empty == "X" or empty == "O":
            i = i + 1
        else:
            # when the spot on the board does not have X or O then it appends the legal spot in a list
            legal_move_list.append(i)
            i = i + 1

    # returns a list of legal moves
    return legal_move_list

# random play outs
def random_play_out():
    # creates a dictionary from 0 to 8
    dict_stimulation_results = {s:0 for s in range(9)}

    # playouts_num is the number of playout the which will be simulated before the computer decides on a move
    playouts_num = 0
    while playouts_num < 5000:
        playouts_num = playouts_num + 1

        simulation_board = game_board[:]
        cond = True
        XO_selector = True

        while(cond):
            legal_move_list = legal_moves(simulation_board)

            random_index = random.randint(0, len(legal_move_list)-1)

            # saves the first move the computer made in the simulated playout
            saved_first_spot = legal_move_list[random_index]

            # alternates between placing a random O or X in the stimulated playout
            if XO_selector:
                simulation_board[legal_move_list[random_index]] = "O"
                XO_selector = False
            else:
                simulation_board[legal_move_list[random_index]] = "X"
                XO_selector = True

            # checks to see if the simulated playout is over and returns an integer to simulated_game_result
            simulated_game_result = is_game_over(simulation_board)

            # if simulated_game_result == 3 this if statement is ignored (3 means continue)
            if simulated_game_result != 3:
                cond = False # breaks while loop

                if simulated_game_result == 0: # O - Computer lost simulation playout
                    temp = dict_stimulation_results.get(saved_first_spot) + 100
                    dict_stimulation_results.update({saved_first_spot: temp})
                if simulated_game_result == 1:  # O - Computer won simulation playout
                    temp = dict_stimulation_results.get(saved_first_spot) + 100
                    dict_stimulation_results.update({saved_first_spot: temp})
                if simulated_game_result == 2:  # there was a draw
                    temp = dict_stimulation_results.get(saved_first_spot) + 1
                    dict_stimulation_results.update({saved_first_spot: temp})

            legal_move_list.clear()

    # print(dict_stimulation_results)
    # print( max(dict_stimulation_results, key=dict_stimulation_results.get) )

    return max(dict_stimulation_results, key=dict_stimulation_results.get)

# decides who goes first
def who_goes_first():
    print("")
    print("Select who goes first, press 'p' for player, press 'c' for computer:")
    first = input()

    if first == "p":
        print("Player Goes First")
    elif first == "c":
        print("Computer Goes First")
        computer_move = random_play_out()
        condition_repeat[computer_move] = 0
        game_board[computer_move] = "O"
        print_current_board(game_board)
    else:
        print("invalid entry, try again")
        who_goes_first()

def play_a_new_game():
    print("")
    print("Player - X")
    print("Computer - O")
    print("")
    print("Board Reference")
    print("")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")

    who_goes_first()

    cond1 = True
    while cond1:

        print("")
        print("############################################################################################")

        print("")
        print("Player's Turn")
        place_move_on_board(game_board) # places your move on the board

        if is_game_over(game_board) != 3:
            print("")
            print("GAME OVER")
            if is_game_over(game_board) == 1:
                print("YOU LOSE")
            elif is_game_over(game_board) == 2:
                print("DRAW")
            else:
                print("YOU WIN")
            print("")

            exit(0)

        print("")
        print("############################################################################################")

        print("")
        print("Computer's Turn")
        computer_move = random_play_out()
        condition_repeat[computer_move] = 0
        game_board[computer_move] = "O"

        if is_game_over(game_board) != 3:
            print_current_board(game_board)
            print("")
            print("GAME OVER")
            if is_game_over(game_board) == 1:
                print("YOU LOSE")
            elif is_game_over(game_board) == 2:
                print("DRAW")
            else:
                print("YOU WIN")
            print("")

            exit(0)

        print_current_board(game_board)

if __name__ == "__main__":
    play_a_new_game()