import tkinter as tk

def create_entry(master):
    entry_file         = tk.Entry(master, width=50, font=("", 8 ))
    entry_acolite_file = tk.Entry(master, width=50, font=("", 8 ))
    entry_lumi         = tk.Entry(master, width=7 , font=("", 10),justify=tk.RIGHT)
    entry_lumi_hist    = tk.Entry(master, width=7 , font=("", 10),justify=tk.RIGHT)
    entry_px           = tk.Entry(master, width=7 , font=("", 10),justify=tk.RIGHT)
    entry_py           = tk.Entry(master, width=7 , font=("", 10),justify=tk.RIGHT)
    entry_delta        = tk.Entry(master, width=7 , font=("", 10),justify=tk.RIGHT)
    entry_ndvi_min     = tk.Entry(master, width=4 , font=("", 10),justify=tk.RIGHT)
    entry_ndvi_max     = tk.Entry(master, width=4 , font=("", 10),justify=tk.RIGHT)
    entry_fdi_min      = tk.Entry(master, width=4 , font=("", 10),justify=tk.RIGHT)
    entry_fdi_max      = tk.Entry(master, width=4 , font=("", 10),justify=tk.RIGHT)
    entry_savefile     = tk.Entry(master, width=25, font=("", 10))
    entry_plt_title    = tk.Entry(master, width=25, font=("", 10))
    
    entry_file.place(        x=110,y=75)
    entry_acolite_file.place(x=110,y=95)
    entry_lumi.place(        x=240,y=125)
    entry_lumi_hist.place(   x=220,y=155)
    entry_px.place(          x=200,y=185)
    entry_py.place(          x=260,y=185)
    entry_delta.place(       x=320,y=185)
    entry_ndvi_min.place(    x=240,y=215)
    entry_ndvi_max.place(    x=300,y=215)
    entry_fdi_min.place(     x=240,y=245)
    entry_fdi_max.place(     x=300,y=245)
    entry_savefile.place(    x=210,y=275)
    entry_plt_title.place(   x=210,y=305)
    
    entry_lumi.insert(0,10000)
    entry_lumi_hist.insert(0,10000)
    entry_px.insert(0,0)
    entry_py.insert(0,0)
    entry_delta.insert(0,0)
    entry_ndvi_min.insert(0,-1)
    entry_ndvi_max.insert(0,1)
    entry_fdi_min.insert(0,0)
    entry_fdi_max.insert(0,0.1)
    entry_plt_title.insert(0,'data')

    entry_list = [entry_file        #0
                ,entry_acolite_file #1
                ,entry_lumi         #2
                ,entry_lumi_hist    #3
                ,entry_px           #4
                ,entry_py           #5
                ,entry_delta        #6
                ,entry_ndvi_min     #7
                ,entry_ndvi_max     #8
                ,entry_fdi_min      #9
                ,entry_fdi_max      #10
                ,entry_savefile     #11
                ,entry_plt_title]   #12
    
    return entry_list