board = []

turn_counter = 0


def play_game():
    reset()
    while True:
        display_board()
        global turn_counter
        winner = get_current_player(turn_counter - 1)
        if check_for_winner():
            print(f"{winner}'s won!")
            break
        if check_for_tie():
            print("It's a tie.")
            break
        take_turn()
        turn_counter += 1
    play_again()


def play_again():
    answer = input("\nPlay again? (Y/N): ").upper()
    if answer == "Y":
        play_game()
    elif answer != "N":
        print("Invalid input.")
        play_again()


def reset():
    global board
    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]
    global turn_counter
    turn_counter = 1


def display_board():
    print(f"\n {board[0]} | {board[1]} | {board[2]} "
          f"\n---+---+---"
          f"\n {board[3]} | {board[4]} | {board[5]} "
          f"\n---+---+---"
          f"\n {board[6]} | {board[7]} | {board[8]} ")


def take_turn():
    player = get_current_player(turn_counter)
    print(f"It's {player}'s turn.")
    position = int(input("Choose a position: ")) - 1
    if is_valid_position(position):
        board[position] = player
    else:
        print("That's not a valid position.")
        display_board()
        take_turn()


def get_current_player(turn):
    if turn % 2 == 1:
        return "X"
    else:
        return "O"


def is_valid_position(position):
    return 0 <= position <= 8 and board[position] != "X" and board[position] != "O"


def check_for_winner():
    return check_for_winner_horizontal() or check_for_winner_vertical() or check_for_winner_diagonal()


def check_for_winner_horizontal():
    return check_for_winner_at(0, 1, 2) or check_for_winner_at(3, 4, 5) or check_for_winner_at(6, 7, 8)


def check_for_winner_vertical():
    return check_for_winner_at(0, 3, 6) or check_for_winner_at(1, 4, 7) or check_for_winner_at(2, 5, 8)


def check_for_winner_diagonal():
    return check_for_winner_at(0, 4, 8) or check_for_winner_at(2, 4, 6)


def check_for_winner_at(pos1, pos2, pos3):
    return (board[pos1] == "X" or board[pos1] == "O") and board[pos1] == board[pos2] and board[pos1] == board[pos3]


def check_for_tie():
    return turn_counter >= 10


play_game()
