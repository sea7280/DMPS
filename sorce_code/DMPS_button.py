import tkinter as tk
import sys
sys.dont_write_bytecode = True
import threading

import DMPS_exit as exit
import DMPS_admin as admin
import DMPS_loadDataFile as loadDataFile
import DMPS_loadSetting as loadSetting
import DMPS_listDelete as listDelete
import DMPS_tkraise as tkraise

def create_button(master, area, entry, listbox, chk, textbox):
        entry_list     = entry
        settingsArea   = area[0]
        runArea        = area[1]
        detectionArea  = area[2]
        background     = "black"
        fontcolor      = "green2"

################################################# change frame #################################################
        Button = tk.Button(master,text=u'Settings' , width=8, bg=background, fg=fontcolor,
                                command=lambda:tkraise.change_frame(settingsArea))
        Button.place(x=5,y=3, height=20)
        Button = tk.Button(master,text=u'Run'      , width=8, bg=background, fg=fontcolor,
                                command=lambda:tkraise.change_frame(runArea))
        Button.place(x=73,y=3, height=20)
        Button = tk.Button(master,text=u'detection', width=8, bg=background, fg=fontcolor,
                                command=lambda:tkraise.change_frame(detectionArea))
        Button.place(x=141,y=3, height=20)
#終了
        Button = tk.Button(master,text=u'Exit', width=8, bg=background, fg=fontcolor,command=lambda:exit.exit_window(master))
        Button.place(x=209,y=3, height=20)

################################################# settings #################################################
        Button = tk.Button(settingsArea,text=u'hist', width=5, bg=background, fg=fontcolor,
                                command=lambda:admin.admin(entry_list, listbox, chk, textbox, mode="hist"))
        Button.place(x=205,y=192, height=18)
        Button = tk.Button(settingsArea,text=u'...', bg=background, fg=fontcolor,
                                command=lambda:loadDataFile.load_dataFile(entry_list[0]))
        Button.place(x=390, y=93, height=15 , width=15)
        Button = tk.Button(settingsArea,text=u'...', bg=background, fg=fontcolor,
                                command=lambda:loadDataFile.load_dataFile(entry_list[1]))
        Button.place(x=390, y=113, height=15 , width=15)
        Button = tk.Button(settingsArea,text=u'Load', width=5, bg=background, fg=fontcolor,
                                command=lambda:loadSetting.read_setting_file(entry_list))
        Button.place(x=340,y=73, height=18)
#設定を保存
        Button = tk.Button(settingsArea,text=u'Save Settings', bg=background, fg=fontcolor,command=lambda:admin.admin(entry_list, listbox, chk, textbox, mode="saveSetting"))
        Button.place(x=310, y=390, height=30 , width=90)

################################################# run #################################################
        setpositionX   = 35
        deltapositionX = 120
        setpositionY   = 50
        deltapositionY = 40
        
        #def rgb():
        #        admin.admin(entry_list, listbox, chk, textbox, mode="rgb")
        #def callback():
        #        test = threading.Thread(target=rgb, daemon=True)
        #        test.start()

#RGB画像生成
        Button = tk.Button(runArea,text=u'RGB', bg=background, fg=fontcolor, command=lambda:admin.admin(entry_list, listbox, chk, textbox, mode="rgb"))
        Button.place(x=setpositionX + deltapositionX*0, y=setpositionY + deltapositionY*0, height=30 , width=110)
#NDVI算出
        Button = tk.Button(runArea,text=u'NDVI', bg=background, fg=fontcolor,command=lambda:admin.admin(entry_list, listbox, chk, textbox, mode="ndvi"))
        Button.place(x=setpositionX + deltapositionX*1, y=setpositionY + deltapositionY*0, height=30 , width=110)
#FDI算出
        Button = tk.Button(runArea,text=u'FDI', bg=background, fg=fontcolor, command=lambda:admin.admin(entry_list, listbox, chk, textbox, mode="fdi"))
        Button.place(x=setpositionX + deltapositionX*2, y=setpositionY + deltapositionY*0, height=30 , width=110)
#NDVI＆FDI算出
        Button = tk.Button(runArea,text=u'NDVI&FDI', bg=background, fg=fontcolor,command=lambda:admin.admin(entry_list, listbox, chk, textbox, mode="ndvi&fdi"))
        Button.place(x=setpositionX + deltapositionX*0, y=setpositionY + deltapositionY*1, height=30 , width=110)
#エクセルに保存
        Button = tk.Button(runArea,text=u'Save Excel', bg=background, fg=fontcolor,command=lambda:admin.admin(entry_list, listbox, chk, textbox, mode="excel"))
        Button.place(x=setpositionX + deltapositionX*1, y=setpositionY + deltapositionY*1, height=30 , width=110)
#分類
        Button = tk.Button(runArea,text=u'Judge', bg=background, fg=fontcolor,command=lambda:admin.admin(entry_list, listbox, chk, textbox, mode="judge"))
        Button.place(x=setpositionX + deltapositionX*2, y=setpositionY + deltapositionY*1, height=30 , width=110)
#解析結果読み込み
        Button = tk.Button(runArea,text=u'Load Judge', bg=background, fg=fontcolor,command=lambda:admin.admin(entry_list, listbox, chk, textbox, mode="loadJudge"))
        Button.place(x=setpositionX + deltapositionX*0, y=setpositionY + deltapositionY*2, height=30 , width=110)
#ヒートマップ作成
        Button = tk.Button(runArea,text=u'heat map', bg=background, fg=fontcolor,command=lambda:admin.admin(entry_list, listbox, chk, textbox, mode="heatmap"))
        Button.place(x=setpositionX + deltapositionX*1, y=setpositionY + deltapositionY*2, height=30 , width=110)
#ヒートマップ作成(数字付き)
        Button = tk.Button(runArea,text=u'heat figure', bg=background, fg=fontcolor,command=lambda:admin.admin(entry_list, listbox, chk, textbox, mode="heatfigure"))
        Button.place(x=setpositionX + deltapositionX*2, y=setpositionY + deltapositionY*2, height=30 , width=110)


################################################# detection #################################################
        Button = tk.Button(detectionArea,text=u'del', width=5,
                                command=lambda:listDelete.list_delete(listbox))
        Button.place(x=580,y=300)
        Button = tk.Button(detectionArea,text=u'load', width=5,
                                command=lambda:admin.admin(entry_list, listbox, chk, textbox, mode="reload"))
        Button.place(x=635,y=300)
        Button = tk.Button(detectionArea,text=u'point load', width=13,
                                command=lambda:admin.admin(entry_list, listbox, chk, textbox, mode="pointload"))
        Button.place(x=580,y=355)

