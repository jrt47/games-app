from tkinter import *
from turtle import TurtleScreen, RawTurtle

WIDTH = 0
HEIGHT = 0

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 450

X_PADDING = 40
Y_PADDING = 10

TITLE = "Pong"


root = Tk()
root.title(TITLE)

title = Label(root, text=TITLE, font=("TkDefaultFont",15))
title.grid(row=0, column=0, pady=(Y_PADDING, Y_PADDING))

frame = Frame(root, bd=2, relief=GROOVE)
frame.grid(row=1, column=0, padx=X_PADDING)

canvas = Canvas(frame, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
canvas.pack()
screen = TurtleScreen(canvas)


left_paddle = RawTurtle(canvas)
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("black")
left_paddle.shapesize(stretch_wid=6, stretch_len=1.5)
left_paddle.penup()
left_paddle.goto(-300, 0)

right_paddle = RawTurtle(canvas)
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("black")
right_paddle.shapesize(stretch_wid=6, stretch_len=1.5)
right_paddle.penup()
right_paddle.goto(300, 0)


def start():
    root.mainloop()


if __name__ == '__main__':
    start()