import tkinter as tk


def create_checkbutton(area):
    background = "black"
    fontcolor = "green2"
    settingsArea = area[0]
# チェックONにする
    bln = tk.BooleanVar()
    bln.set(True)

    # チェックボタン作成
    chk = tk.Checkbutton(settingsArea, variable=bln, bg=background, fg=fontcolor)
    chk.place(x=210, y=409)
    return bln