import tkinter as tk

def create_frame(master):
    detectionFrame = tk.Frame(master   , height=440, width=850, bg="black", relief=tk.GROOVE, bd=3)
    mainFrame      = tk.Frame(master   , height=440, width=860, bg="black")
    runFrame       = tk.Frame(mainFrame, height=440, width=420, bg="black", relief=tk.GROOVE, bd=3)
    setteingFrame  = tk.Frame(mainFrame, height=440, width=420, bg="black", relief=tk.GROOVE, bd=3)

    detectionFrame.place(x=5, y=25)
    mainFrame.place(     x=0, y=25)
    runFrame.place(      x=435, y=0)
    setteingFrame.place( x=5, y=0)

    frame_list = [setteingFrame,        #0
                    runFrame,       #1
                    detectionFrame,#2
                    mainFrame]     #3
    return frame_list