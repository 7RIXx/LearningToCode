#!/bin/python3

'''
CURRENT ISSUES:

- f_sla, b_sla, x_sla not working in the check_win function

- Failed input from a player does not report an error message "Invalid selection"

- Responding yes to query_rematch function causes an exit

- Tie game is delayed reporting by two turns and fails to trigger query_rematch function
    - See also over_though function

- The main loops at the bottom feel tangled AF

- Whole program feels bulky AF

- Several uses of 'global' keyword inside functions to access outside variables

YET TO BE DESIGNED:
- The option for players to choose X or O

WOULD ALSO BE COOL:
- The option to let players choose any character other than the pre-destined question mark
    - This would require re-working the entire check_win function

        - I actually wonder if the check_win was enhanced if that would fix the problem with the diagonal wins?
'''

import string

#############################
######## SET GLOBALS ########
#############################

player_one_assigned = False
player_two_assigned = False

player_one_mark = "X"  # ADD SWAPABILITY IN
player_two_mark = "O"  # ADD SWAPABILITY IN
player_one_wins = False
player_two_wins = False

check_game_on = True
over_though = False
query_rematch = False

open_spaces = {"TL": 7, "TC": 8, "TR": 9, "L": 4, "C": 5, "R": 6, "BL": 1, "BC": 2, "BR": 3}
save_spaces = open_spaces

game_board = [

    ['//', '//', '//', '//', ' ', '=', '=', '=', ' ', '=', '=', '=', ' ', '=', '=', '=', ' ', '=', '=', '=', ' ', '=',
     '=', '=', ' ', r'\\', r'\\', r'\\', r'\\'],

    [' ||||', '|', '|', '|', ' ', ' ', ' ', ' ', ' ', '|', '|', '|', ' ', ' ', ' ', ' ', ' ', '|', '|', '|', ' ', ' ',
     ' ', ' ', ' ', '|', '|', '|', '||||'],

    [' ||||', '|', '|', '|', ' ', ' ', '?', ' ', ' ', '|', '|', '|', ' ', ' ', '?', ' ', ' ', '|', '|', '|', ' ', ' ',
     '?', ' ', ' ', '|', '|', '|', '||||'],

    [' ||||', '|', '|', '|', ' ', ' ', ' ', ' ', ' ', '|', '|', '|', ' ', ' ', ' ', ' ', ' ', '|', '|', '|', ' ', ' ',
     ' ', ' ', ' ', '|', '|', '|', '||||'],

    [' ||||', '|', '|', '|', ' ', '=', '=', '=', ' ', '+', '+', '+', ' ', '=', '=', '=', ' ', '+', '+', '+', ' ', '=',
     '=', '=', ' ', '|', '|', '|', '||||'],

    [' ||||', '|', '|', '|', ' ', ' ', ' ', ' ', ' ', '|', '|', '|', ' ', ' ', ' ', ' ', ' ', '|', '|', '|', ' ', ' ',
     ' ', ' ', ' ', '|', '|', '|', '||||'],

    [' ||||', '|', '|', '|', ' ', ' ', '?', ' ', ' ', '|', '|', '|', ' ', ' ', '?', ' ', ' ', '|', '|', '|', ' ', ' ',
     '?', ' ', ' ', '|', '|', '|', '||||'],

    [' ||||', '|', '|', '|', ' ', ' ', ' ', ' ', ' ', '|', '|', '|', ' ', ' ', ' ', ' ', ' ', '|', '|', '|', ' ', ' ',
     ' ', ' ', ' ', '|', '|', '|', '||||'],

    [' ||||', '|', '|', '|', ' ', '=', '=', '=', ' ', '+', '+', '+', ' ', '=', '=', '=', ' ', '+', '+', '+', ' ', '=',
     '=', '=', ' ', '|', '|', '|', '||||'],

    [' ||||', '|', '|', '|', ' ', ' ', ' ', ' ', ' ', '|', '|', '|', ' ', ' ', ' ', ' ', ' ', '|', '|', '|', ' ', ' ',
     ' ', ' ', ' ', '|', '|', '|', '||||'],

    [' ||||', '|', '|', '|', ' ', ' ', '?', ' ', ' ', '|', '|', '|', ' ', ' ', '?', ' ', ' ', '|', '|', '|', ' ', ' ',
     '?', ' ', ' ', '|', '|', '|', '||||'],

    [' ||||', '|', '|', '|', ' ', ' ', ' ', ' ', ' ', '|', '|', '|', ' ', ' ', ' ', ' ', ' ', '|', '|', '|', ' ', ' ',
     ' ', ' ', ' ', '|', '|', '|', '||||'],

    [r'\\', r'\\', r'\\', r'\\', ' ', '=', '=', '=', ' ', '=', '=', '=', ' ', '=', '=', '=', ' ', '=', '=', '=', ' ',
     '=', '=', '=', ' ', '//', '//', '//', '//'],

]

save_board = game_board


#############################
###### WRITE FUNCTIONS ######
#############################

def show_board():

    print("".join(game_board[0]))
    print("".join(game_board[1]))
    print("".join(game_board[2]))
    print("".join(game_board[3]))
    print("".join(game_board[4]))
    print("".join(game_board[5]))
    print("".join(game_board[6]))
    print("".join(game_board[7]))
    print("".join(game_board[8]))
    print("".join(game_board[9]))
    print("".join(game_board[10]))
    print("".join(game_board[11]))
    print("".join(game_board[12]))


def player_one_plays():

    one_choi = ""

    while not one_choi.isnumeric():
        one_choi = input("\r\n" + "Player One" + "\r\n" + "\r\n" + "Use NumPad to Choose Your Position: ")

    one_choice = int(one_choi)

    # Verify Choice
    if one_choice == 7 and "TL" in open_spaces:
        game_board[2][6] = player_one_mark
        open_spaces.pop("TL")

    elif one_choice == 8 and "TC" in open_spaces:
        game_board[2][14] = player_one_mark
        open_spaces.pop("TC")

    elif one_choice == 9 and "TR" in open_spaces:
        game_board[2][22] = player_one_mark
        open_spaces.pop("TR")

    elif one_choice == 4 and "L" in open_spaces:
        game_board[6][6] = player_one_mark
        open_spaces.pop("L")

    elif one_choice == 5 and "C" in open_spaces:
        game_board[6][14] = player_one_mark
        open_spaces.pop("C")

    elif one_choice == 6 and "R" in open_spaces:
        game_board[6][22] = player_one_mark
        open_spaces.pop("R")

    elif one_choice == 1 and "BL" in open_spaces:
        game_board[10][6] = player_one_mark
        open_spaces.pop("BL")

    elif one_choice == 2 and "BC" in open_spaces:
        game_board[10][14] = player_one_mark
        open_spaces.pop("BC")

    elif one_choice == 3 and "BR" in open_spaces:
        game_board[10][22] = player_one_mark
        open_spaces.pop("BR")

    else:
        print("\r\n")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Invalid Choice, Please Try Again..")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("\r\n")


def player_two_plays():

    two_choi = ""

    while not two_choi.isnumeric():
        two_choi = input("\r\n" + "Player Two" + "\r\n" + "\r\n" + "Use NumPad to Choose Your Position: ")

    two_choice = int(two_choi)

    # Verify Choice
    if two_choice == 7 and "TL" in open_spaces:
        game_board[2][6] = player_two_mark
        open_spaces.pop("TL")

    elif two_choice == 8 and "TC" in open_spaces:
        game_board[2][14] = player_two_mark
        open_spaces.pop("TC")

    elif two_choice == 9 and "TR" in open_spaces:
        game_board[2][22] = player_two_mark
        open_spaces.pop("TR")

    elif two_choice == 4 and "L" in open_spaces:
        game_board[6][6] = player_two_mark
        open_spaces.pop("L")

    elif two_choice == 5 and "C" in open_spaces:
        game_board[6][14] = player_two_mark
        open_spaces.pop("C")

    elif two_choice == 6 and "R" in open_spaces:
        game_board[6][22] = player_two_mark
        open_spaces.pop("R")

    elif two_choice == 1 and "BL" in open_spaces:
        game_board[10][6] = player_two_mark
        open_spaces.pop("BL")

    elif two_choice == 2 and "BC" in open_spaces:
        game_board[10][14] = player_two_mark
        open_spaces.pop("BC")

    elif two_choice == 3 and "BR" in open_spaces:
        game_board[10][22] = player_two_mark
        open_spaces.pop("BR")

    else:
        print("\r\n")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Invalid Choice, Please Try Again..")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("\r\n")


def check_win():


    h_top = [game_board[2][6], game_board[2][14], game_board[2][22]]
    h_mid = [game_board[6][6], game_board[6][14], game_board[6][22]]
    h_low = [game_board[10][6], game_board[10][14], game_board[10][22]]
    v_lef = [game_board[2][6], game_board[6][6], game_board[10][6]]
    v_mid = [game_board[2][14], game_board[6][14], game_board[10][14]]
    v_rig = [game_board[2][22], game_board[6][22], game_board[10][22]]
    x_sla = [game_board[10][6], game_board[6][10], game_board[2][22], game_board[10][22], game_board[2][6]]
    f_sla = [game_board[10][6], game_board[6][10], game_board[2][22]]
    b_sla = [game_board[10][22], game_board[6][10], game_board[2][6]]

    if ("TL" and "TC" and "TR") not in open_spaces:

        if h_top == ['X', 'X', 'X']:
            one_wins = True
            player_one_wins = one_wins

        elif h_top == ['O', 'O', 'O']:
            two_wins = True
            player_two_wins = two_wins

    if "L" and "C" and "R" not in open_spaces:

        if h_mid == ['X', 'X', 'X']:
            one_wins = True
            player_one_wins = one_wins

        elif h_mid == ['O', 'O', 'O']:
            two_wins = True
            player_two_wins = two_wins

    if "BL" and "BC" and "BR" not in open_spaces:

        if h_low == ['X', 'X', 'X']:
            one_wins = True
            player_one_wins = one_wins

        elif h_low == ['O', 'O', 'O']:
            two_wins = True
            player_two_wins = two_wins

    if "TL" and "L" and "BL" not in open_spaces:

        if v_lef == ['X', 'X', 'X']:
            one_wins = True
            player_one_wins = one_wins

        elif v_lef == ['O', 'O', 'O']:
            two_wins = True
            player_two_wins = two_wins

    if "TC" and "C" and "BC" not in open_spaces:

        if v_mid == ['X', 'X', 'X']:
            one_wins = True
            player_one_wins = one_wins

        elif v_mid == ['O', 'O', 'O']:
            two_wins = True
            player_two_wins = two_wins

    if "TR" and "R" and "BR" not in open_spaces:

        if v_rig == ['X', 'X', 'X']:
            one_wins = True
            player_one_wins = one_wins

        elif v_rig == ['O', 'O', 'O']:
            two_wins = True
            player_two_wins = two_wins

    if "BL" and "C" and "TR" not in open_spaces:

        if f_sla == ['X', 'X', 'X']:
            one_wins = True
            player_one_wins = one_wins

        elif f_sla == ['O', 'O', 'O']:
            two_wins = True
            player_two_wins = two_wins

    if "TL" and "C" and "BR" not in open_spaces:

        if b_sla == ['X', 'X', 'X']:
            one_wins = True
            player_one_wins = one_wins

        elif b_sla == ['O', 'O', 'O']:
            two_wins = True
            player_two_wins = two_wins

    if "TL" and "C" and "TR" and "BL" and "BR" not in open_spaces:

        if x_sla == ['X', 'X', 'X']:
            one_wins = True
            player_one_wins = one_wins

        elif x_sla == ['O', 'O', 'O']:
            two_wins = True
            player_two_wins = two_wins


def is_over():

    global over_though

    if game_over == 0 and not player_one_wins and not player_two_wins:
        check_game_on = False
        print("You must be employees, because NOBODY WON HERE!")
        over_though = False
        return over_though

while check_game_on:

    game_over = len(open_spaces)
    print(game_over)

    if player_one_wins:
        check_game_on = False
        print("PLAYER ONE WINS!")
        break

    elif player_two_wins:
        check_game_on = False
        print("PLAYER TWO WINS!")
        break

    else:
        print("\r\n" * 100)
        show_board()
        player_one_plays()
        print("\r\n" * 100)
        show_board()
        check_win()
        is_over()

        if player_one_wins:
            print("PLAYER ONE WINS!")
            break

        elif over_though:
            print("Nobody Wins")
            break

        else:
            player_two_plays()
            print("\r\n" * 100)
            show_board()
            check_win()
            is_over()

        if player_two_wins:
            print("PLAYER TWO WINS!")
            break

        elif over_though:
            print("Nobody Wins")
            break

        else:
            continue

while not query_rematch:

    rematch = str(input("Would you like to play again (Y/N) ? "))
    yes = ["Y", "y"]
    no = ["N", "n"]

    if rematch in yes:
        query_rematch = True

    elif rematch in no:
        break

    else:
        print("Invalid Selection...")

if query_rematch == True:
    player_one_assigned = False
    player_two_assigned = False
    player_one_wins = False
    player_two_wins = False
    player_one_mark = "X"  # ADD SWAPABILITY IN
    player_two_mark = "O"  # ADD SWAPABILITY IN
    check_game_on = True
    query_rematch = False
    game_board = save_board
    open_spaces = save_spaces

else:
    check_game_on = False
    print("\r\n" * 5)
    print("Goodbye")
    exit()
