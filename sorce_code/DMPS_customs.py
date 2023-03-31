
#ライブラリの読み込み
import pandas as pd
import os
import datetime
import numpy as np
import tkinter as tk
# k-近傍法（k-NN）
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import pickle
import sys
sys.dont_write_bytecode = True
import warnings
warnings.simplefilter('ignore', UserWarning)
#オーバーサンプリング
from imblearn.over_sampling import SMOTE


def test():
    print("a")

def custom_knn(setting_detail):
    equation = setting_detail[19]
    calc_equationA = eval('equation')
    print(type(equation))
    print(calc_equationA)
