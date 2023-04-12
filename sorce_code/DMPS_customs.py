
#ライブラリの読み込み
import pandas as pd
import os
from osgeo import gdal
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

import DMPS_fdi as fdi_calc
import DMPS_ndvi as ndvi_calc

def custom_knn(filepath, setting_detail):

#式の取得
    equationA = setting_detail[19][0].get()
    equationB = setting_detail[19][1].get()

    #切り出しの詳細
    minX          = setting_detail[4]
    minY          = setting_detail[5]
    deltaX        = setting_detail[6]
    deltaY        = setting_detail[7]
    #空変数の用意
    BlueBand_array       = None
    GreenBand_array      = None
    RedBand_array        = None
    NIR_Band_array       = None
    aco_BlueBand_array   = None
    aco_GreenBand_array  = None
    aco_RedBand_array    = None
    aco_NIR_Band_array   = None
    aco_RE2_Band_array   = None
    aco_SWIR1_Band_array = None
    ndvi_result          = None
    fdi_result           = None

    """文字列に衛星データ変数が含まれるか判定
       必要な変数のみデータを保持することでメモリへの負担を軽減"""
    #判定、保持の処理を関数化
    #データを保持する変数を引数としている

    def haveData(pathNum):
        path = filepath[pathNum]
        band_8bit_path =os.path.dirname(__file__) + "/tif_file/Band_8bit.tif"
        gdal.Translate(band_8bit_path,path  ,srcWin=[minX,minY,deltaX,deltaY])
        b8_image=gdal.Open(band_8bit_path)
        band_array  = b8_image.ReadAsArray()
        band_array  = band_array  / 10000
        return band_array

    #acoliteデータ用
    def haveAcoData(pathNum):
        path = filepath[pathNum]
        cut_img = gdal.Open(path)
        band_array  = cut_img.ReadAsArray()
        if deltaX == 0 and deltaY == 0:
            pass
        #切り抜き範囲に合わせて配列の抜き出し
        #ここのコード醜いからいつか修正したい
        else:
            band_array = band_array[minY:minY+deltaY, minX:minX+deltaX]
        return band_array

    if 'a' in equationA or 'a' in equationB:
        BlueBand_array = haveData(0)
    if 'b' in equationA or 'b' in equationB:
        GreenBand_array = haveData(1)
    if 'c' in equationA or 'c' in equationB:
        RedBand_array = haveData(2)
    if 'd' in equationA or 'd' in equationB:
        NIR_Band_array = haveData(3)
    if 'e' in equationA or 'e' in equationB:
        aco_BlueBand_array = haveAcoData(6)
    if 'f' in equationA or 'f' in equationB:
        aco_GreenBand_array = haveAcoData(7)
    if 'g' in equationA or 'g' in equationB:
        aco_RedBand_array = haveAcoData(8)
    if 'h' in equationA or 'h' in equationB:
        aco_NIR_Band_array = haveAcoData(9)
    if 'i' in equationA or 'i' in equationB:
        aco_RE2_Band_array = haveAcoData(10)
    if 'j' in equationA or 'j' in equationB:
        aco_SWIR1_Band_array = haveAcoData(11)
    if 'ndvi' in equationA or 'ndvi' in equationB:
        ndvi_result = ndvi_calc.calc_ndvi(filepath, setting_detail)
    if 'fdi' in equationA or 'fdi' in equationB:
        fdi_result = fdi_calc.calc_fdi(filepath, setting_detail)

##################################################################################################
    #変数へ割り当て
    a = BlueBand_array       
    b = GreenBand_array      
    c = RedBand_array        
    d = NIR_Band_array       
    e = aco_BlueBand_array   
    f = aco_GreenBand_array  
    g = aco_RedBand_array    
    h = aco_NIR_Band_array   
    i = aco_RE2_Band_array   
    j = aco_SWIR1_Band_array 
    ndvi = ndvi_result
    fdi  = fdi_result

#入力した計算式の実行

    calc_equationA = eval(equationA)
    calc_equationB = eval(equationB)
    print(calc_equationA)
    print(calc_equationB)
#################################### 機械学習実行 #####################################









