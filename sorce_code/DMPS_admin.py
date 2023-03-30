import sys
sys.dont_write_bytecode = True
import tkinter as tk

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
import DMPS_hist as hist
import DMPS_reloadJudgeRGB as reloadJudge
import DMPS_loadJudgeLog as JudgeLog
import DMPS_resulutMapping as resulutMapping



def admin(entry, listbox, chk, textbox, mode):

#entryの入力値を配列に格納
    filePath       = entry[0].get()         #0
    filePathAco    = entry[1].get()         #1
    luminance      = int(entry[2].get())    #2
    luminance_hist = int(entry[3].get())    #3
    minX           = int(entry[4].get())    #4
    minY           = int(entry[5].get())    #5
    deltaX         = int(entry[6].get())    #6
    deltaY         = int(entry[7].get())    #7
    ndvi_min       = float(entry[8].get())  #8
    ndvi_max       = float(entry[9].get())  #9
    fdi_min        = float(entry[10].get())  #10
    fdi_max        = float(entry[11].get()) #11
    saveFileName   = entry[12].get()        #12
    title          = entry[13].get()        #13
    load_px        = int(entry[14].get())   #14
    load_py        = int(entry[15].get())   #15
    check          = chk                    #16
    #textbox                                #17
    teacher        = entry[16].get()        #18

#変数：setting_detail
    setting_detail = [filePath, filePathAco, luminance, luminance_hist
                  , minX, minY, deltaX, deltaY,
                  ndvi_min, ndvi_max, fdi_min, fdi_max, 
                  saveFileName, title, load_px,load_py, check, textbox, teacher]

#衛星データのパスを配列に格納
    satellite_filepath = pathGet.pathGet(entry)

#ボタンによって処理が変わる
    if satellite_filepath[0] == None:
        textbox.insert(tk.END,"No Satellite Data\n")
        textbox.see("end")
    else:
        if mode == "rgb":
            truecolor.truecolor(satellite_filepath, setting_detail)
        elif mode == 'ndvi':
            ndvi_result = ndvi.calc_ndvi(satellite_filepath, setting_detail)
            dataImage.image_create(ndvi_result, setting_detail[8], setting_detail[9], setting_detail[13])
        elif mode == 'fdi':
            fdi_result = fdi.calc_fdi(satellite_filepath, setting_detail)
            dataImage.image_create(fdi_result, setting_detail[10], setting_detail[11], setting_detail[13])
        elif mode == 'ndvi&fdi':
            textbox.insert(tk.END,"Start calculation NDVI & FDI.\n")
            textbox.see("end")
            ndvi_result = ndvi.calc_ndvi(satellite_filepath, setting_detail)
            fdi_result = fdi.calc_fdi(satellite_filepath, setting_detail)
            dataImage.image_create_double(ndvi_result, fdi_result, setting_detail[8], setting_detail[9], setting_detail[10], setting_detail[11])
        elif mode == 'excel':
            ndvi_result = ndvi.calc_ndvi(satellite_filepath, setting_detail)
            fdi_result = fdi.calc_fdi(satellite_filepath, setting_detail)
            writeExcel.saveExcel(satellite_filepath, setting_detail, ndvi_result, fdi_result)
        elif mode == 'saveSetting':
            saveSettings.saveSettings(setting_detail)
        elif mode == 'judge':
            ndvi_result = ndvi.calc_ndvi(satellite_filepath, setting_detail)
            fdi_result  = fdi.calc_fdi(satellite_filepath, setting_detail)
            knn.knn_judge(ndvi_result, fdi_result, setting_detail)
            knnSave.knnSaveExcel(saveFileName)
            textbox.insert(tk.END,"Complete save excel file.\n")
            textbox.see("end")
            knnRGB.knnRGB(satellite_filepath, setting_detail, listbox, load=None)
        elif mode == 'loadJudge':
            log = JudgeLog.loadJudgeLog(setting_detail)
            knnRGB.knnRGB(satellite_filepath, setting_detail, listbox, load=log)
        elif mode == "heatmap":
            log = JudgeLog.loadJudgeLog(setting_detail)
            resulutMapping.resultMapping(satellite_filepath, setting_detail, load=log, figure=False)
        elif mode == "heatfigure":
            log = JudgeLog.loadJudgeLog(setting_detail)
            resulutMapping.resultMapping(satellite_filepath, setting_detail, load=log, figure=True)
        elif mode == 'hist':
            hist.luminance(satellite_filepath, setting_detail)
        elif mode == "reload":
            reloadJudge.reloadJudgeRGB(satellite_filepath, setting_detail, listbox, mode="list")
        elif mode == "pointload":
            reloadJudge.reloadJudgeRGB(satellite_filepath, setting_detail, listbox, mode="point")