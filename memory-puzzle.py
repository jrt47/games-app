from tkinter import *
from random import sample
from sched import scheduler
from time import time
from time import sleep


BUTTON_HEIGHT = 2
BUTTON_WIDTH = 4

X_PADDING = 40
Y_PADDING = 15

TITLE = "Memory Puzzle"

ALL_CARDS = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E',
             'V', 'V', 'W', 'W', 'X', 'X', 'Y', 'Y', 'Z', 'Z']

cards = []
revealed = []

first = -1

timer = scheduler(time, sleep)

def shuffle_cards():
    global cards
    cards = sample(ALL_CARDS, len(ALL_CARDS))


def button_click(n):
    if is_blank_card(n):
        reveal_card(n)
        global first
        if first == -1:
            first = n
        elif cards[first] == cards[n]:
            first = -1
        else:
            flip_wrong_cards_delay(n)
            first = -1


def flip_wrong_cards_delay(n):
    timer.enter(2, 1, flip_wrong_cards, argument=(n,))
    timer.run()


def flip_wrong_cards(n):
    revealed[first] = ''
    revealed[n] = ''
    update_button_text()


def reveal_card(n):
    revealed[n] = cards[n]
    update_button_text()


def is_blank_card(n):
    return revealed[n] == ''


def update_button_text():
    for i in range(20):
        button_texts[i].set(revealed[i])


def reset():
    global first
    first = -1
    shuffle_cards()
    clear_revealed()

def clear_revealed():
    global revealed
    revealed = ['', '', '', '', '',
                '', '', '', '', '',
                '', '', '', '', '',
                '', '', '', '', '',
                '', '', '', '', '']
    update_button_text()


root = Tk()
root.title(TITLE)

title = Label(root, text=TITLE, font=("TkDefaultFont", 15))
title.grid(row=0, column=0, columnspan=5, pady=Y_PADDING)

bt0 = StringVar()
bt1 = StringVar()
bt2 = StringVar()
bt3 = StringVar()
bt4 = StringVar()
bt5 = StringVar()
bt6 = StringVar()
bt7 = StringVar()
bt8 = StringVar()
bt9 = StringVar()
bt10 = StringVar()
bt11 = StringVar()
bt12 = StringVar()
bt13 = StringVar()
bt14 = StringVar()
bt15 = StringVar()
bt16 = StringVar()
bt17 = StringVar()
bt18 = StringVar()
bt19 = StringVar()

button_texts = [bt0, bt1, bt2, bt3, bt4,
                bt5, bt6, bt7, bt8, bt9,
                bt10, bt11, bt12, bt13, bt14,
                bt15, bt16, bt17, bt18, bt19]

b0 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
            textvariable=bt0, command=lambda: button_click(0))
b1 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
            textvariable=bt1, command=lambda: button_click(1))
b2 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
            textvariable=bt2, command=lambda: button_click(2))
b3 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
            textvariable=bt3, command=lambda: button_click(3))
b4 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
            textvariable=bt4, command=lambda: button_click(4))
b5 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
            textvariable=bt5, command=lambda: button_click(5))
b6 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
            textvariable=bt6, command=lambda: button_click(6))
b7 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
            textvariable=bt7, command=lambda: button_click(7))
b8 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
            textvariable=bt8, command=lambda: button_click(8))
b9 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
            textvariable=bt9, command=lambda: button_click(9))
b10 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
             textvariable=bt10, command=lambda: button_click(10))
b11 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
             textvariable=bt11, command=lambda: button_click(11))
b12 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
             textvariable=bt12, command=lambda: button_click(12))
b13 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
             textvariable=bt13, command=lambda: button_click(13))
b14 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
             textvariable=bt14, command=lambda: button_click(14))
b15 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
             textvariable=bt15, command=lambda: button_click(15))
b16 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
             textvariable=bt16, command=lambda: button_click(16))
b17 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
             textvariable=bt17, command=lambda: button_click(17))
b18 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
             textvariable=bt18, command=lambda: button_click(18))
b19 = Button(root, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
             textvariable=bt19, command=lambda: button_click(19))

buttons = [b0, b1, b2, b3, b4,
           b5, b6, b7, b8, b9,
           b10, b11, b12, b13, b14,
           b15, b16, b17, b18, b19]

b0.grid(row=1, column=0, padx=(X_PADDING, 0))
b1.grid(row=1, column=1)
b2.grid(row=1, column=2)
b3.grid(row=1, column=3)
b4.grid(row=1, column=4, padx=(0, X_PADDING))
b5.grid(row=2, column=0, padx=(X_PADDING, 0))
b6.grid(row=2, column=1)
b7.grid(row=2, column=2)
b8.grid(row=2, column=3)
b9.grid(row=2, column=4, padx=(0, X_PADDING))
b10.grid(row=3, column=0, padx=(X_PADDING, 0))
b11.grid(row=3, column=1)
b12.grid(row=3, column=2)
b13.grid(row=3, column=3)
b14.grid(row=3, column=4, padx=(0, X_PADDING))
b15.grid(row=4, column=0, padx=(X_PADDING, 0))
b16.grid(row=4, column=1)
b17.grid(row=4, column=2)
b18.grid(row=4, column=3)
b19.grid(row=4, column=4, padx=(0, X_PADDING))

reset_button = Button(root, text="Reset", command=reset)
reset_button.grid(row=5, column=0, columnspan=5, pady=Y_PADDING)


def start():
    reset()
    root.mainloop()


start()
