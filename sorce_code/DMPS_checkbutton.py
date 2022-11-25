import tkinter as tk


def create_checkbutton(master):
# チェックONにする
    bln = tk.BooleanVar()
    bln.set(True)

    # チェックボタン作成
    chk = tk.Checkbutton(master, variable=bln, text='Standardization')
    chk.place(x=580, y=335)
    return chk