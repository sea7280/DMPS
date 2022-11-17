import matplotlib.pyplot as plt
from osgeo import gdal
import sys
sys.dont_write_bytecode = True

def luminance(filepath,entry_detail):
    bluepath  = filepath[0]
    greenpath = filepath[1]
    redpath   = filepath[2]
    nirpath   = filepath[3]
    range_max = entry_detail[3]
    title     = entry_detail[12]

    band_image1=gdal.Open(bluepath)
    band_image2=gdal.Open(greenpath)
    band_image3=gdal.Open(redpath)
    band_image4=gdal.Open(nirpath)

    Band_array1 = band_image1.ReadAsArray()
    Band_array2 = band_image2.ReadAsArray()
    Band_array3 = band_image3.ReadAsArray()
    Band_array4 = band_image4.ReadAsArray()


    plt.figure(figsize=(8,4))
    #先ほど配列に変換したデータの輝度値について、500本の柱で表示することにします
    plt.hist(Band_array1.flatten(),bins=500,range=(0, range_max), label="Blue", alpha=0.3, histtype='stepfilled', color="b") 
    plt.hist(Band_array2.flatten(),bins=500,range=(0, range_max), label="Green", alpha=0.3, histtype='stepfilled', color="g") 
    plt.hist(Band_array3.flatten(),bins=500,range=(0, range_max), label="Red", alpha=0.3, histtype='stepfilled', color="r") 
    plt.hist(Band_array4.flatten(),bins=500,range=(0, range_max), label="NIR", alpha=0.3, histtype='stepfilled', color="y") 

    plt.legend()
    plt.title(title)
    plt.show()


