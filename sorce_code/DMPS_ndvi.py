
from osgeo import gdal
from tkinter import messagebox
import os
import sys
sys.dont_write_bytecode = True

def calc_ndvi(filepath,setting_detail):
#--------------------------------------------- path ---------------------------------------------------------

    redpath = filepath[2]
    nirpath = filepath[3]

#--------------------------------------------- range ---------------------------------------------------------

    minX      = setting_detail[4]
    minY      = setting_detail[5]
    deltaX    = setting_detail[6]
    deltaY    = setting_detail[6]

#--------------------------------------------- tif ---------------------------------------------------------

    band4_8bit_path =os.path.dirname(__file__) + "/tif_file/Band4_8bit.tif"
    band8_8bit_path =os.path.dirname(__file__) + "/tif_file/Band8_8bit.tif"

#---------------------------------------------- 配列変換 -----------------------------------------------------
    gdal.Translate(band4_8bit_path ,redpath ,srcWin=[minX,minY,deltaX,deltaY])
    gdal.Translate(band8_8bit_path ,nirpath ,srcWin=[minX,minY,deltaX,deltaY])

    b4_image =gdal.Open(band4_8bit_path)
    b8_image =gdal.Open(band8_8bit_path)

    RedBand_array       = b4_image.ReadAsArray()
    NIR_Band_array      = b8_image.ReadAsArray()

    RedBand_array      = RedBand_array      / 10000
    NIR_Band_array     = NIR_Band_array     / 10000

    ndvi = (NIR_Band_array - RedBand_array)/(NIR_Band_array + RedBand_array)


    return ndvi