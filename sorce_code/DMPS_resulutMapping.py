import tkinter as tk
from osgeo import gdal
import numpy as np
import os
import pickle
import matplotlib.pyplot as plt
from PIL import Image

#ヒートマップの作成
def resultMapping(filepath,setting_detail, load, figure):
    log = setting_detail[17]
    log.insert(tk.END,"Start Start creating a heatmap.\n")
    log.see("end")

    bluepath  = filepath[0]
    greenpath = filepath[1]
    redpath   = filepath[2]

    if load == None:
        with open(os.path.dirname(__file__) + "/pickle/judge.pickle", mode='rb') as f:
            judegedata = pickle.load(f)
    else:
        judegedata = load
    judegedata = np.array(judegedata)
    band2_8bit_path=os.path.dirname(__file__) + "/tif_file/Band2_8bit.tif"
    band3_8bit_path=os.path.dirname(__file__) + "/tif_file/Band3_8bit.tif"
    band4_8bit_path=os.path.dirname(__file__) + "/tif_file/Band4_8bit.tif"

    #切り出しの詳細
    minX          = setting_detail[4]
    minY          = setting_detail[5]
    deltaX        = setting_detail[6]
    deltaY        = setting_detail[7]
    max_luminance = setting_detail[2]

    #各バンドのファイルを、それぞれ、関心領域のみ切り出す。出力は8bitのgeotifとする
    #gdal.Translate({出力画像名}, {入力画像名}, outputType={データ形式設定} , scaleParams=[[min,max]], srcWin=[minX,minY,deltaX,deltaY])
    gdal.Translate(band2_8bit_path,bluepath,  scaleParams=[[0,max_luminance]],outputType=gdal.GDT_Byte, srcWin=[minX,minY,deltaX,deltaY])
    gdal.Translate(band3_8bit_path,greenpath, scaleParams=[[0,max_luminance]],outputType=gdal.GDT_Byte, srcWin=[minX,minY,deltaX,deltaY])
    gdal.Translate(band4_8bit_path,redpath,   scaleParams=[[0,max_luminance]],outputType=gdal.GDT_Byte, srcWin=[minX,minY,deltaX,deltaY])

    #作成した8bitの切り出し画像を読み込む
    b2_image=gdal.Open(band2_8bit_path)
    b3_image=gdal.Open(band3_8bit_path)
    b4_image=gdal.Open(band4_8bit_path)

    #読み込んだ画像を配列に変換する
    BlueBand_array  = b2_image.ReadAsArray()
    GreenBand_array = b3_image.ReadAsArray()
    RedBand_array   = b4_image.ReadAsArray()

    #出力ファイルの設定のために、入力ファイルのX方向のピクセル数、Y方向のピクセル数を読み出す
    Xsize=b2_image.RasterXSize #band2の画像のX方向ピクセル数
    Ysize=b2_image.RasterYSize #band2の画像のY方向ピクセル数
    dtype=gdal.GDT_Byte
    band=3

    out_True_path =os.path.dirname(__file__) + "/tif_file/truecolor.tif"    #出力ファイル名
    out1= gdal.GetDriverByName('GTiff').Create(out_True_path, Xsize, Ysize, band, dtype)#({出力ファイル名}, {X方向のピクセル数},{Y方向のピクセル数},{バンド数},{データ形式})
    out1.SetProjection(b2_image.GetProjection())      #{出力変数}.SetProjection(座標系情報)
    out1.SetGeoTransform(b2_image.GetGeoTransform())  #{出力変数}.SetGeoTransform(座標に関する６つの数字)
    out1.GetRasterBand(1).WriteArray(RedBand_array)   #赤の配列を赤バンドに書き込む
    out1.GetRasterBand(2).WriteArray(GreenBand_array) #緑の配列を緑バンドに書き込む
    out1.GetRasterBand(3).WriteArray(BlueBand_array)  #青の配列を青バンドに書き込む
    out1.FlushCache()
<<<<<<< HEAD
    #figureならカウント付きヒートマップ　なしなら普通のヒートマップ
    #カウント付きは300ピクセル四方でカウント　なしは100ピクセル四方でカウント
    #ヒートマップの最大値はカウント付きは90000　なしは10000
=======

#最大値の設定
>>>>>>> 31f046cb4c7057d00b1283210064bef6d4a36d72
    if figure == True:
        delta = 100
        max = 90000
    elif figure == False:
        delta = 50
        max = 0.2
#プラスチックカウント
    plasticCount = []
    plasticPercent = []
    for y in range(0,len(judegedata),delta):
        countX = []
        percentX = []
        for x in range(0,len(judegedata[0]),delta):
            data = judegedata[y:y+delta,x:x+delta]
            #プラスチックの数をカウント
            count = np.count_nonzero(data == "plastic")
            percent = round((count * 10 / (delta*10)**2) * 100,3)
            #X方向のカウント結果
            countX.append(count)
            percentX.append(percent)
        #x方向のカウント結果をまとめて配列に
        plasticCount.append(countX)
        plasticPercent.append(percentX)
    #numpy化
    plasticCount = np.array(plasticCount)
    plasticPercent = np.array(plasticPercent)
    #ログの出力
    log.insert(tk.END,"Complete.\n")
    log.see("end")
#描画
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(1, 1, 1)
#ヒートマップ作成
    #im = plt.imshow(plasticCount, vmin=0, vmax=600,cmap='gist_stern', interpolation='nearest')
#    im = plt.imshow(plasticPercent, vmin=0, vmax=max,cmap='bwr', 
#                    aspect='equal', interpolation='nearest')
    #im = plt.imshow(plasticPercent, vmin=0, vmax=max,cmap='gist_ncar', 
    im = plt.imshow(plasticPercent, vmin=0, vmax=max,cmap='bwr',
                    aspect='equal', interpolation='nearest')
    fig.colorbar(im, ax=ax)
    
    if figure == True:
    #ヒートマップ上に数値を載せる
        for i in range(len(plasticCount)):
            for j in range(len(plasticCount[0])):
                text = ax.text(j, i, plasticPercent[i, j], size ='small',
                       ha="center", va="center", color="w")
    elif figure == False:
        pass
        
#画像描画
    image = Image.open(out_True_path)
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    ax.imshow(image, extent=[*xlim, *ylim], aspect='equal', alpha=0.7)


    plt.title(setting_detail[12])
    plt.show()
    plt.close()
