from tkinter.scrolledtext import ScrolledText
import tkinter as tk

#テキストボックスの作成
def create_textbox(area):
    frame = area[1]
    background = "black"
    fontcolor = "green2"
    textbox = ScrolledText(frame, font=("",10), height=22, width=53,
                            bg=background, fg=fontcolor)
    textbox.place(x=10, y=180)
    return textbox

"""
def create_calcbox(area):
    frame = area[2]
    background = "black"
    fontcolor = "green2"
    calcboxA = ScrolledText(frame, font=("",13), height=5, width=42,
                            bg=background, fg=fontcolor)
    calcboxB = ScrolledText(frame, font=("",13), height=5, width=42,
                            bg=background, fg=fontcolor)
    calcboxA.place(x=10, y=220)
    calcboxB.place(x=10, y=330)
    calcbox = [calcboxA, calcboxB]
    print(calcbox)
    return calcbox

"""