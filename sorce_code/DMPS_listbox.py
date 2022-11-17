import tkinter as tk
import sys
sys.dont_write_bytecode = True

def create_listbox(master):
    coodinate_listbox = tk.Listbox(master,width=16, height=15, selectmode='single')
    coodinate_listbox.place(x=580, y=50)
    return coodinate_listbox

def delete(box):
    box.delete(box.curselection())
