import tkinter as tk

def create_frame(master):
    detectionFrame = tk.Frame(master, height=440, width=420, bg="black", relief=tk.GROOVE, bd=3)
    runFrame       = tk.Frame(master, height=440, width=420, bg="black", relief=tk.GROOVE, bd=3)
    setteingFrame  = tk.Frame(master, height=440, width=420, bg="black", relief=tk.GROOVE, bd=3)

    detectionFrame.place(   x=5, y=25)
    runFrame.place(     x=5, y=25)
    setteingFrame.place(x=5, y=25)

    frame_list = [setteingFrame,        #0
                    runFrame,       #1
                    detectionFrame]     #2
    return frame_list