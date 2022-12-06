import tkinter as tk
import sys
sys.dont_write_bytecode = True

import DMPS_exit as exit
import DMPS_admin as admin
import DMPS_loadDataFile as loadDataFile
import DMPS_loadSetting as loadSetting
import DMPS_listDelete as listDelete
import DMPS_tkraise as tkraise

def create_button(master, area, entry, listbox, chk):
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

################################################# settings #################################################
        Button = tk.Button(settingsArea,text=u'hist', width=5, bg=background, fg=fontcolor,
                                command=lambda:admin.admin(entry_list, listbox, chk, mode="hist"))
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

################################################# run #################################################
        setpositionX   = 35
        deltapositionX = 120
        setpositionY   = 50
        deltapositionY = 40
#ボタンの位置直しましょう
        Button = tk.Button(runArea,text=u'RGB', bg=background, fg=fontcolor, command=lambda:admin.admin(entry_list, listbox, chk, mode="rgb"))
        Button.place(x=setpositionX + deltapositionX*0, y=setpositionY + deltapositionY*0, height=30 , width=110)
        Button = tk.Button(runArea,text=u'NDVI', bg=background, fg=fontcolor,command=lambda:admin.admin(entry_list, listbox, chk, mode="ndvi"))
        Button.place(x=setpositionX + deltapositionX*1, y=setpositionY + deltapositionY*0, height=30 , width=110)
        Button = tk.Button(runArea,text=u'FDI', bg=background, fg=fontcolor, command=lambda:admin.admin(entry_list, listbox, chk, mode="fdi"))
        Button.place(x=setpositionX + deltapositionX*2, y=setpositionY + deltapositionY*0, height=30 , width=110)
        Button = tk.Button(runArea,text=u'NDVI&FDI', bg=background, fg=fontcolor,command=lambda:admin.admin(entry_list, listbox, chk, mode="ndvi&fdi"))
        Button.place(x=setpositionX + deltapositionX*0, y=setpositionY + deltapositionY*1, height=30 , width=110)
        Button = tk.Button(runArea,text=u'Save Excel', bg=background, fg=fontcolor,command=lambda:admin.admin(entry_list, listbox, chk, mode="excel"))
        Button.place(x=setpositionX + deltapositionX*1, y=setpositionY + deltapositionY*1, height=30 , width=110)
        Button = tk.Button(runArea,text=u'Save Settings', bg=background, fg=fontcolor,command=lambda:admin.admin(entry_list, listbox, chk, mode="saveSetting"))
        Button.place(x=setpositionX + deltapositionX*2, y=setpositionY + deltapositionY*1, height=30 , width=110)
        Button = tk.Button(runArea,text=u'Judge', bg=background, fg=fontcolor,command=lambda:admin.admin(entry_list, listbox, chk, mode="judge"))
        Button.place(x=setpositionX + deltapositionX*0, y=setpositionY + deltapositionY*2, height=30 , width=110)
        Button = tk.Button(runArea,text=u'Load Judge', bg=background, fg=fontcolor,command=lambda:admin.admin(entry_list, listbox, chk, mode="loadJudge"))
        Button.place(x=setpositionX + deltapositionX*1, y=setpositionY + deltapositionY*2, height=30 , width=110)
        Button = tk.Button(runArea,text=u'heat map', bg=background, fg=fontcolor,command=lambda:admin.admin(entry_list, listbox, chk, mode="heatmap"))
        Button.place(x=setpositionX + deltapositionX*2, y=setpositionY + deltapositionY*2, height=30 , width=110)

        Button = tk.Button(runArea,text=u'Exit', bg=background, fg=fontcolor,command=lambda:exit.exit_window(master))
        Button.place(x=470,y=360, height=110 , width=30)

################################################# detection #################################################
        Button = tk.Button(detectionArea,text=u'del', width=5,
                                command=lambda:listDelete.list_delete(listbox))
        Button.place(x=580,y=300)
        Button = tk.Button(detectionArea,text=u'load', width=5,
                                command=lambda:admin.admin(entry_list, listbox, chk, mode="reload"))
        Button.place(x=635,y=300)
        Button = tk.Button(detectionArea,text=u'point load', width=13,
                                command=lambda:admin.admin(entry_list, listbox, chk, mode="pointload"))
        Button.place(x=580,y=355)

