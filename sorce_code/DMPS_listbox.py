import tkinter as tk
import sys
sys.dont_write_bytecode = True


def create_listbox(area):
    coodinate_listbox = tk.Listbox(area[2],width=16, height=15,  selectmode=tk.MULTIPLE)
    coodinate_listbox.place(x=580, y=50)
    return coodinate_listbox


