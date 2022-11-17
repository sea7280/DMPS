from tkinter import messagebox
import datetime
import os
import sys
sys.dont_write_bytecode = True

def saveSettings(entry_detail):

    satpath        = entry_detail[0]
    acopath        = entry_detail[1]
    maxluminance   = entry_detail[2]
    hist_luminance = entry_detail[3]
    px             = entry_detail[4]
    py             = entry_detail[5]
    dt             = entry_detail[6]
    ndvi_min       = entry_detail[7]
    ndvi_max       = entry_detail[8]
    fdi_min        = entry_detail[9]
    fdi_max        = entry_detail[10]
    fn             = entry_detail[11]
    title          = entry_detail[12]
    
    if fn == "":
        messagebox.showerror('Error', 'No Save File Name')
    else:
        today = datetime.date.today()
        with open(os.getcwd() + f'/setting/{fn}.txt', mode='w') as file:
            file.write(f"day:{today}\n")
            file.write(f"Satellite data path:{satpath}\n")
            file.write(f"Acolite data path:{acopath}\n")
            file.write(f"luminance:{maxluminance}\n")
            file.write(f"hist luminance:{hist_luminance}\n")
            file.write(f"px:{px}\n")
            file.write(f"py:{py}\n")
            file.write(f"delta:{dt}\n")
            file.write(f"NDVI range:{ndvi_min}~{ndvi_max}\n")
            file.write(f"FDI range:{fdi_min}~{fdi_max}\n")
            file.write(f"file name:{fn}\n")
            file.write(f"graph title:{title}\n")
        messagebox.showinfo('Complete', 'Save Completed')