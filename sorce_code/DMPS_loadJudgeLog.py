import sys
sys.dont_write_bytecode = True
import tkinter.filedialog
import os
import pickle
import tkinter as tk

def loadJudgeLog(setting_detail):
    log = setting_detail[17]

    dir = os.getcwd() + '/pickle_log'
    data_file = tkinter.filedialog.askopenfilename(initialdir = dir)

    log.insert(tk.END,"Load file : " + str(data_file) + "\n")
    log.see("end")

    with open(data_file, mode='rb') as f:
        judegedata = pickle.load(f)
    return judegedata

