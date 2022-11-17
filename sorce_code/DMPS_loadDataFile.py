import tkinter.filedialog
import tkinter as tk
import sys
sys.dont_write_bytecode = True

def load_dataFile(ent):
        ent.delete(0, tk.END)
        data_file = tkinter.filedialog.askdirectory()
        ent.insert(tk.END,data_file)