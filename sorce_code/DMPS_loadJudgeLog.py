import sys
sys.dont_write_bytecode = True
import tkinter.filedialog
import os
import pickle

def loadJudgeLog():
    dir = os.getcwd() + '/pickle_log'
    data_file = tkinter.filedialog.askopenfilename(initialdir = dir)
    with open(data_file, mode='rb') as f:
        judegedata = pickle.load(f)
    return judegedata

