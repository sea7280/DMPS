#フレーム生成ファイル

#ライブラリの読み込み
import tkinter as tk

#フレームの生成関数
def create_frame(master):
    mainFrame      = tk.Frame(master   , height=480, width=860, bg="black")
    customFrame    = tk.Frame(mainFrame, height=480, width=420, bg="black", relief=tk.GROOVE, bd=3)
    runFrame       = tk.Frame(mainFrame, height=480, width=420, bg="black", relief=tk.GROOVE, bd=3)
    setteingFrame  = tk.Frame(mainFrame, height=480, width=420, bg="black", relief=tk.GROOVE, bd=3)

    
    mainFrame.place(     x=0, y=25)
    customFrame.place(   x=5, y=0)
    runFrame.place(      x=435, y=0)
    setteingFrame.place( x=5, y=0)

    frame_list = [setteingFrame,    #0
                    runFrame,       #1
                    customFrame,    #2
                    mainFrame,      #3
                    ]
    
    return frame_list