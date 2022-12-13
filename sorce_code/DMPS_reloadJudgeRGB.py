import matplotlib.pyplot as plt
from osgeo import gdal
import matplotlib.image as mpimg
import os
import tkinter as tk
import pickle
import numpy as np
import sys
sys.dont_write_bytecode = True
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

def reloadJudgeRGB(filepath,setting_detail, point_list,mode):
    log = setting_detail[17]

#サイズの取得
    minX          = setting_detail[4]
    minY          = setting_detail[5]
    deltaX        = setting_detail[6]
    deltaY        = setting_detail[7]
    path = filepath[0]
    getSize_path=os.path.dirname(__file__) + "/tif_file/getSize_8bit.tif"
    gdal.Translate(getSize_path,path,outputType=gdal.GDT_Byte, srcWin=[minX,minY,deltaX,deltaY])
    band_image=gdal.Open(getSize_path)
    Band_array = band_image.ReadAsArray()

    maxSizeX = len(Band_array[0])
    maxSizeY = len(Band_array)
    band_image = None
    Band_array = None

#座標の取得
#リストからの選択
    if mode == "list":
        index = point_list.curselection()
    
        if not index:
            log.insert(tk.END,"Please select a point.\n")
            log.see("end")
        elif len(index) > 1:
            log.insert(tk.END,"Please select only one.\n")
            log.see("end")
        else:
            point = point_list.get(index)
            delete = ["Point: ", " ", "[", "]"]
            for i in delete:
                point = point.replace(i, "")
            point = point.split(",")
            centerX, centerY = int(point[0]), int(point[1])
    elif mode == "point":
        centerX, centerY = setting_detail[14], setting_detail[15]
#拡大範囲の決定
#0以下になったら0になるように設定
        expansionRange = 50
        if expansionRange > maxSizeY:
            expansionRange = round(maxSizeY * 0.5)
        expansionRange_half = round(expansionRange *0.5 - 1)
        deltaMinX, deltaMinY = centerX - expansionRange_half, centerY - expansionRange_half
        if deltaMinX < 0:
            deltaMinX = 0
        if deltaMinY < 0:
            deltaMinY = 0
#画像サイズを超える場合収まるように設定

        if deltaMinX + expansionRange > maxSizeX-1:
            deltaX = maxSizeX - deltaMinX
        else:
            deltaX = expansionRange

        if deltaMinY + expansionRange > maxSizeY-1:
            deltaY = maxSizeY - deltaMinY
        else:
            deltaY = expansionRange

        minX          = deltaMinX + setting_detail[4]
        minY          = deltaMinY + setting_detail[5]
        max_luminance = setting_detail[2]

        bluepath  = filepath[0]
        greenpath = filepath[1]
        redpath   = filepath[2]
    
        with open(os.path.dirname(__file__) + "/pickle/judge.pickle", mode='rb') as f:
            judegedata = pickle.load(f)

        raw = np.arange(deltaMinX)
        row = np.arange(deltaMinY)
        judegedata = np.delete(judegedata,row,axis=0)
        judegedata = np.delete(judegedata,raw,axis=1)

        raw_delta = np.arange(deltaX,len(judegedata[0]),1)
        row_delta = np.arange(deltaY,len(judegedata),1)
        judegedata = np.delete(judegedata,row_delta,axis=0)
        judegedata = np.delete(judegedata,raw_delta,axis=1)

        band2_8bit_path=os.path.dirname(__file__) + "/tif_file/Band2_8bit.tif"
        band3_8bit_path=os.path.dirname(__file__) + "/tif_file/Band3_8bit.tif"
        band4_8bit_path=os.path.dirname(__file__) + "/tif_file/Band4_8bit.tif"

        gdal.Translate(band2_8bit_path,bluepath,  scaleParams=[[0,max_luminance]],outputType=gdal.GDT_Byte, srcWin=[minX,minY,deltaX,deltaY])
        gdal.Translate(band3_8bit_path,greenpath, scaleParams=[[0,max_luminance]],outputType=gdal.GDT_Byte, srcWin=[minX,minY,deltaX,deltaY])
        gdal.Translate(band4_8bit_path,redpath,   scaleParams=[[0,max_luminance]],outputType=gdal.GDT_Byte, srcWin=[minX,minY,deltaX,deltaY])

        b2_image=gdal.Open(band2_8bit_path)
        b3_image=gdal.Open(band3_8bit_path)
        b4_image=gdal.Open(band4_8bit_path)

        BlueBand_array  = b2_image.ReadAsArray()
        GreenBand_array = b3_image.ReadAsArray()
        RedBand_array   = b4_image.ReadAsArray()

        size_y = deltaY
        size_x = deltaX
        for y in range(size_y):
            y = y
            for x in range(size_x):
                x = x
                if judegedata[y][x] == "plastic":
                    RedBand_array[y][x] = 255
                    GreenBand_array[y][x] = 0
                    BlueBand_array[y][x] = 0
                elif judegedata[y][x] == "ship":
                    RedBand_array[y][x] = 0
                    GreenBand_array[y][x] = 0
                    BlueBand_array[y][x] = 255
                elif judegedata[y][x] == "water":
                    pass
                elif judegedata[y][x] == "wood":
                    pass
                elif judegedata[y][x] == "pumice":
                    pass

        Xsize=b2_image.RasterXSize #band2の画像のX方向ピクセル数
        Ysize=b2_image.RasterYSize #band2の画像のY方向ピクセル数
        dtype=gdal.GDT_Byte
        band=3

        out_True_path =os.path.dirname(__file__) + "/tif_file/truecolor.tif"
        out1= gdal.GetDriverByName('GTiff').Create(out_True_path, Xsize, Ysize, band, dtype)
        out1.SetProjection(b2_image.GetProjection())
        out1.SetGeoTransform(b2_image.GetGeoTransform())

        out1.GetRasterBand(1).WriteArray(RedBand_array)   #赤の配列を赤バンドに書き込む
        out1.GetRasterBand(2).WriteArray(GreenBand_array) #緑の配列を緑バンドに書き込む
        out1.GetRasterBand(3).WriteArray(BlueBand_array)  #青の配列を青バンドに書き込む
        out1.FlushCache()

#---------------------------------------- 出力 -----------------------------------------

        plt.figure(figsize=(7,5))

        image1 = mpimg.imread(out_True_path)
        plt.imshow(image1)
        plt.title(setting_detail[13])


        plt.show()
        plt.close()


