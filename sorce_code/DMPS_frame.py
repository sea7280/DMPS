#フレーム生成ファイル

#ライブラリの読み込み
import tkinter as tk

#フレームの生成関数
def create_frame(master):
<<<<<<< HEAD
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
=======
    #フレームの生成
    detectionFrame = tk.Frame(master, height=440, width=420, bg="black", relief=tk.GROOVE, bd=3)
    runFrame       = tk.Frame(master, height=440, width=420, bg="black", relief=tk.GROOVE, bd=3)
    setteingFrame  = tk.Frame(master, height=440, width=420, bg="black", relief=tk.GROOVE, bd=3)
    #フレームの設置
    detectionFrame.place(   x=5, y=25)
    runFrame.place(     x=5, y=25)
    setteingFrame.place(x=5, y=25)
    #生成したフレームを配列で管理
    frame_list = [setteingFrame,        #0
                    runFrame,       #1
                    detectionFrame]     #2
    #frame_listを返す
>>>>>>> 31f046cb4c7057d00b1283210064bef6d4a36d72
    return frame_list