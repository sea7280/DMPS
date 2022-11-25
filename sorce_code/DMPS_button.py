import tkinter as tk
import sys
sys.dont_write_bytecode = True

import DMPS_exit as exit
import DMPS_admin as admin
import DMPS_loadDataFile as loadDataFile
import DMPS_loadSetting as loadSetting
import DMPS_listDelete as listDelete


def create_button(master, entry, listbox, chk):
        entry_list = entry
        
        Button = tk.Button(master,text=u'hist', width=5, command=lambda:admin.admin(entry_list, listbox, chk, mode="hist"))
        Button.place(x=285,y=145)
        Button = tk.Button(master,text=u'...', height=1 ,width=2, command=lambda:loadDataFile.load_dataFile(entry_list[0]))
        Button.place(x=420,y=70)
        Button = tk.Button(master,text=u'...',height=1 ,width=2, command=lambda:loadDataFile.load_dataFile(entry_list[1]))
        Button.place(x=420,y=95)
        Button = tk.Button(master,text=u'Load Setting', width=11, command=lambda:loadSetting.read_setting_file(entry_list))
        Button.place(x=470,y=60)
        Button = tk.Button(master,text=u'RGB', width=11, command=lambda:admin.admin(entry_list, listbox, chk, mode="rgb"))
        Button.place(x=470,y=90)
        Button = tk.Button(master,text=u'NDVI', width=11, command=lambda:admin.admin(entry_list, listbox, chk, mode="ndvi"))
        Button.place(x=470,y=120)
        Button = tk.Button(master,text=u'FDI', width=11, command=lambda:admin.admin(entry_list, listbox, chk, mode="fdi"))
        Button.place(x=470,y=150)
        Button = tk.Button(master,text=u'NDVI&FDI', width=11, command=lambda:admin.admin(entry_list, listbox, chk, mode="ndvi&fdi"))
        Button.place(x=470,y=180)
        Button = tk.Button(master,text=u'Save Excel', width=11, command=lambda:admin.admin(entry_list, listbox, chk, mode="excel"))
        Button.place(x=470,y=210)
        Button = tk.Button(master,text=u'Save Setting', width=11, command=lambda:admin.admin(entry_list, listbox, chk, mode="saveSetting"))
        Button.place(x=470,y=240)
        Button = tk.Button(master,text=u'Judge', width=11, command=lambda:admin.admin(entry_list, listbox, chk, mode="judge"))
        Button.place(x=470,y=270)
        Button = tk.Button(master,text=u'Load Judge', width=11, command=lambda:admin.admin(entry_list, listbox, chk, mode="loadJudge"))
        Button.place(x=470,y=300)
        Button = tk.Button(master,text=u'Exit', width=11,command=lambda:exit.exit_window(master))
        Button.place(x=470,y=330)
        Button = tk.Button(master,text=u'del', width=5, command=lambda:listDelete.list_delete(listbox))
        Button.place(x=580,y=300)
        Button = tk.Button(master,text=u'load', width=5,command=lambda:admin.admin(entry_list, listbox, chk, mode="reload"))
        Button.place(x=635,y=300)

