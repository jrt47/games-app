from tkinter import *

WIDTH = 234
HEIGHT = 259

BUTTON_HEIGHT = 2
BUTTON_WIDTH = 4

X_PADDING = 60
Y_PADDING = 10

TITLE = "Tic Tac Toe"

board = []

turn_counter = 0


def reset():
    global board
    board = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]
    global turn_counter
    turn_counter = 1
    label_text.set("It's X's turn.")
    update_button_text()
    enable_buttons()


def button_click(position):
    global turn_counter
    player = get_current_player()
    if is_valid_position(position):
        board[position] = player
        update_button_text()
        if check_for_winner():
            label_text.set(f"{player}'s won!")
            return
        if check_for_tie():
            label_text.set("It's a tie.")
            return
        turn_counter += 1
        player = get_current_player()
        label_text.set(f"It's {player}'s turn.")


def enable_buttons():
    for i in range(9):
        buttons[i]["state"] = "normal"


def update_button_text():
    for i in range(9):
        button_texts[i].set(board[i])


def get_current_player():
    if turn_counter % 2 == 1:
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
    return turn_counter >= 9


def place_window():
    w = WIDTH
    h = HEIGHT
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = ws/2 - w/2
    y = hs/2 - h/2
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))


def keep_groove(event):
    if event.widget in buttons:
        event.widget.config(relief=GROOVE)


root = Tk()
root.title(TITLE)

title = Label(root, text=TITLE, font=("TkDefaultFont",15))
title.grid(row=0, column=0, columnspan=3, pady=(Y_PADDING, 0))

button_text_0 = StringVar()
button_text_1 = StringVar()
button_text_2 = StringVar()
button_text_3 = StringVar()
button_text_4 = StringVar()
button_text_5 = StringVar()
button_text_6 = StringVar()
button_text_7 = StringVar()
button_text_8 = StringVar()

button_texts = [button_text_0, button_text_1, button_text_2,
                button_text_3, button_text_4, button_text_5,
                button_text_6, button_text_7, button_text_8]

button_0 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, relief=GROOVE,
                  textvariable=button_text_0, command=lambda:button_click(0))
button_1 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, relief=GROOVE,
                  textvariable=button_text_1, command=lambda:button_click(1))
button_2 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, relief=GROOVE,
                  textvariable=button_text_2, command=lambda:button_click(2))
button_3 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, relief=GROOVE,
                  textvariable=button_text_3, command=lambda:button_click(3))
button_4 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, relief=GROOVE,
                  textvariable=button_text_4, command=lambda:button_click(4))
button_5 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, relief=GROOVE,
                  textvariable=button_text_5, command=lambda:button_click(5))
button_6 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, relief=GROOVE,
                  textvariable=button_text_6, command=lambda:button_click(6))
button_7 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, relief=GROOVE,
                  textvariable=button_text_7, command=lambda:button_click(7))
button_8 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, relief=GROOVE,
                  textvariable=button_text_8, command=lambda:button_click(8))

buttons = [button_0, button_1, button_2,
           button_3, button_4, button_5,
           button_6, button_7, button_8]

button_0.grid(row=1, column=0, padx=(X_PADDING, 0), pady=(Y_PADDING, 0))
button_1.grid(row=1, column=1, pady=(Y_PADDING,0))
button_2.grid(row=1, column=2, padx=(0, X_PADDING), pady=(Y_PADDING, 0))
button_3.grid(row=2, column=0, padx=(X_PADDING, 0))
button_4.grid(row=2, column=1)
button_5.grid(row=2, column=2, padx=(0, X_PADDING))
button_6.grid(row=3, column=0, padx=(X_PADDING, 0), pady=(0, Y_PADDING))
button_7.grid(row=3, column=1, pady=(0,Y_PADDING))
button_8.grid(row=3, column=2, padx=(0, X_PADDING), pady=(0, Y_PADDING))

label_text = StringVar()
label = Label(root, textvariable=label_text)
label.grid(row=4, column=0, columnspan=3)

reset_button = Button(root, text="Reset", command=reset)
reset_button.grid(row=5, column=0, columnspan=3, pady=Y_PADDING)

root.bind('<Button-1>', keep_groove)


def start():
    reset()
    place_window()
    root.mainloop()


start()
