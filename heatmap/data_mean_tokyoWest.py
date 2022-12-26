#https://extralab.org/wp/python-files-select-filename-folderpath-get/


import os
from tkinter import filedialog  # tkinterのfiledialogをインポート
import tkinter as tk
from osgeo import gdal
import numpy as np
import pickle
import matplotlib.pyplot as plt
from PIL import Image
import math

# 複数ファイル選択
def files_select():
    root = tk.Tk()  # インスタンス生成
    root.withdraw()

    # ファイル選択ダイアログでのファイル検索種類を指定
    file_type = [('pickleファイル', '*.pickle')]
    filenames = filedialog.askopenfilenames(filetypes=file_type)

    return filenames  # 選択ファイルの絶対パスを返します。


# メイン処理関数
def hoge_logic(_path, _base_name):
    # 処理内容~~
    with open(_path, mode='rb') as f:
        judegedata = pickle.load(f)

    judegedata = np.array(judegedata)
    #figureならカウント付きヒートマップ　なしなら普通のヒートマップ
    #カウント付きは300ピクセル四方でカウント　なしは100ピクセル四方でカウント
    #ヒートマップの最大値はカウント付きは90000　なしは10000

    delta = 300
    max = 10000
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
            #割合算出
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

    return plasticPercent


# main
if __name__ == "__main__":
    # 複数ファイル選択処理の場合------
    filenames = files_select()
    
    bluepath  = "C:/Users/KamedaLab/Desktop/SatelliteData/S2A_tokyowan_20210924_west/GRANULE/L1C_T54SUE_A032675_20210924T012658/IMG_DATA/T54SUE_20210924T012701_B02.jp2"
    greenpath = "C:/Users/KamedaLab/Desktop/SatelliteData/S2A_tokyowan_20210924_west/GRANULE/L1C_T54SUE_A032675_20210924T012658/IMG_DATA/T54SUE_20210924T012701_B03.jp2"
    redpath   = "C:/Users/KamedaLab/Desktop/SatelliteData/S2A_tokyowan_20210924_west/GRANULE/L1C_T54SUE_A032675_20210924T012658/IMG_DATA/T54SUE_20210924T012701_B04.jp2"

    band2_8bit_path=os.path.dirname(__file__) + "/tif_file/Band2_8bit.tif"
    band3_8bit_path=os.path.dirname(__file__) + "/tif_file/Band3_8bit.tif"
    band4_8bit_path=os.path.dirname(__file__) + "/tif_file/Band4_8bit.tif"

    #切り出しの詳細
    minX          = 7400
    minY          = 5000
    deltaX        = 3490
    deltaY        = 5890
    max_luminance = 5000

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

    lenX = math.ceil(len(BlueBand_array[0]) / 300)
    lenY = math.ceil(len(BlueBand_array) / 300)
    
    sum_percent = np.zeros((lenY,lenX))

    # 複数ファイルを1ファイルずつ処理する
    for path in list(filenames):
        base_name = os.path.splitext(os.path.basename(path))[0]  # ファイル名を取得
        #dir_name = os.path.dirname(path)  # フォルダ名を取得

        # メイン処理関数呼び出し
        percent = hoge_logic(path, base_name)
#平均値算出
        sum_percent = sum_percent + percent
    mean_percent = np.round(sum_percent / len(filenames),3)

#描画
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(1, 1, 1)
#ヒートマップ作成
    im = plt.imshow(mean_percent, vmin=0, vmax=1,cmap='bwr', 
                    aspect='equal', interpolation='nearest')
    fig.colorbar(im, ax=ax)

#    #ヒートマップ上に数値を載せる
#    for i in range(len(mean_percent)):
#        for j in range(len(mean_percent[0])):
#            text = ax.text(j, i, mean_percent[i, j], fontsize=7,
#                       ha="center", va="center", color="w")

#画像描画
    image = Image.open(out_True_path)
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    ax.imshow(image, extent=[*xlim, *ylim], aspect='equal', alpha=0.7)


    plt.title("percent mean")
    plt.show()
    plt.close()
    # ----------------------

    print('処理終了')