

import numpy as np
from osgeo import gdal


def calc_fdi(filepath,entry_detail):

    nirpath     = filepath[9]
    R_RE2path   = filepath[10]
    R_SWIR1path = filepath[11]
    senti_num   = filepath[12]
        #切り抜き範囲
    minX      = entry_detail[4]
    minY      = entry_detail[5]
    deltaX    = entry_detail[6]
    deltaY    = entry_detail[6]

    #gdal.Openで画像を読み込みます
    cut_NIR_img  =gdal.Open(nirpath    )
    cut_RE2_img  =gdal.Open(R_RE2path  )
    cut_SWIR1_img=gdal.Open(R_SWIR1path)

    #画像情報を配列に変換します
    NIR_Band_array      = cut_NIR_img.ReadAsArray()
    R_RE2_Band_array    = cut_RE2_img.ReadAsArray()
    R_SWIR1_Band_array  = cut_SWIR1_img.ReadAsArray()

    if deltaX == 0:
        pass

    else:

        raw = np.arange(minX)
        row = np.arange(minY)

        NIR_Band_array = np.delete(NIR_Band_array,row,axis=0)
        NIR_Band_array = np.delete(NIR_Band_array,raw,axis=1)

        R_RE2_Band_array = np.delete(R_RE2_Band_array,row,axis=0)
        R_RE2_Band_array = np.delete(R_RE2_Band_array,raw,axis=1)

        R_SWIR1_Band_array = np.delete(R_SWIR1_Band_array,row,axis=0)
        R_SWIR1_Band_array = np.delete(R_SWIR1_Band_array,raw,axis=1)

        raw_delta = np.arange(deltaX,len(NIR_Band_array[0]),1)
        row_delta = np.arange(deltaY,len(NIR_Band_array),1)

        NIR_Band_array = np.delete(NIR_Band_array,row_delta,axis=0)
        NIR_Band_array = np.delete(NIR_Band_array,raw_delta,axis=1)

        R_RE2_Band_array = np.delete(R_RE2_Band_array,row_delta,axis=0)
        R_RE2_Band_array = np.delete(R_RE2_Band_array,raw_delta,axis=1)

        R_SWIR1_Band_array  = np.delete(R_SWIR1_Band_array ,row_delta,axis=0)
        R_SWIR1_Band_array  = np.delete(R_SWIR1_Band_array ,raw_delta,axis=1)

        #-------------------------------calc-------------------------------------

    if senti_num == 1:  #S2A
        hNIR = 832.8
        hRed = 664.6
        hSWIR1 = 1613.7
    elif senti_num == 2: #S2B
        hNIR = 833.0
        hRed = 665.0
        hSWIR1 = 1610.4

    R_NIR = R_RE2_Band_array + ((R_SWIR1_Band_array - R_RE2_Band_array) * ((hNIR - hRed) / (hSWIR1 - hRed)) * 10)
    FDI = NIR_Band_array - R_NIR
    #FDI = NIR_Band_array - R_RE2_Band_array - (R_SWIR1_Band_array - R_RE2_Band_array) * 10*(833 - 655)/(1610 - 655)

    return FDI



