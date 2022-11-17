import sys
sys.dont_write_bytecode = True

import DMPS_pathGet as pathGet
import DMPS_image as dataImage
import DMPS_truecolor as truecolor
import DMPS_ndvi as ndvi
import DMPS_fdi as fdi
import DMPS_writeExcel as writeExcel
import DMPS_saveSettings as saveSettings
import DMPS_knn as knn
import DMPS_knn_saveExcel as knnSave
import DMPS_knnRGB as knnRGB

def admin(entry,listbox, mode):

    filePath       = entry[0].get()         #0
    filePathAco    = entry[1].get()         #1
    luminance      = int(entry[2].get())    #2
    luminance_hist = int(entry[3].get())    #3
    minX           = int(entry[4].get())    #4
    minY           = int(entry[5].get())    #5
    delta          = int(entry[6].get())    #6
    ndvi_min       = float(entry[7].get())  #7
    ndvi_max       = float(entry[8].get())  #8
    fdi_min        = float(entry[9].get())  #9
    fdi_max        = float(entry[10].get()) #10
    saveFileName   = entry[11].get()        #11
    title          = entry[12].get()        #12

    entry_data = [filePath, filePathAco, luminance, luminance_hist
                  , minX, minY, delta, 
                  ndvi_min, ndvi_max, fdi_min, fdi_max, 
                  saveFileName, title]

    satellite_filepath = pathGet.pathGet(entry)

    if satellite_filepath[0] == None:
        pass
    else:
        if mode == "rgb":
            truecolor.truecolor(satellite_filepath, entry_data)
        elif mode == 'ndvi':
            ndvi_result = ndvi.calc_ndvi(satellite_filepath, entry_data)
            dataImage.image_create(ndvi_result, entry_data[7], entry_data[8], entry_data[12])
        elif mode == 'fdi':
            fdi_result = fdi.calc_fdi(satellite_filepath, entry_data)
            dataImage.image_create(fdi_result, entry_data[9], entry_data[10], entry_data[12])
        elif mode == 'ndvi&fdi':
            ndvi_result = ndvi.calc_ndvi(satellite_filepath, entry_data)
            fdi_result = fdi.calc_fdi(satellite_filepath, entry_data)
            dataImage.image_create_double(ndvi_result, fdi_result, entry_data[7], entry_data[8], entry_data[9], entry_data[10])
        elif mode == 'excel':
            ndvi_result = ndvi.calc_ndvi(satellite_filepath, entry_data)
            fdi_result = fdi.calc_fdi(satellite_filepath, entry_data)
            writeExcel.saveExcel(satellite_filepath, entry_data, ndvi_result, fdi_result)
        elif mode == 'saveSetting':
            saveSettings.saveSettings(entry_data)
        elif mode == 'judge':
            ndvi_result = ndvi.calc_ndvi(satellite_filepath, entry_data)
            fdi_result  = fdi.calc_fdi(satellite_filepath, entry_data)
            knn.knn_judge(ndvi_result, fdi_result)
            knnSave.knnSaveExcel(saveFileName)
            knnRGB.knnRGB(satellite_filepath, entry_data, listbox)