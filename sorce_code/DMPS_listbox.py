import tkinter as tk
import sys
sys.dont_write_bytecode = True

#リストボックスの生成
def create_listbox(area):
    background     = "black"
    fontcolor      = "green2"
    coodinate_listbox = tk.Listbox(area[2], bg=background, fg=fontcolor,width=16, height=15,  selectmode=tk.MULTIPLE)
    #coodinate_listbox.place(x=50, y=50)
    return coodinate_listbox


