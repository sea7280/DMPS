from tkinter.scrolledtext import ScrolledText
import tkinter as tk

def create_textbox(area):
    frame = area[1]
    background = "black"
    fontcolor = "green2"
    textbox = ScrolledText(frame, font=("",10), height=19, width=53,
                            bg=background, fg=fontcolor)
    textbox.place(x=10, y=180)
    return textbox