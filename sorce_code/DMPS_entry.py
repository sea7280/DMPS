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
    
    entry_file.place(        x=110,y=75)
    entry_acolite_file.place(x=110,y=95)
    entry_lumi.place(        x=240,y=120)
    entry_lumi_hist.place(   x=220,y=150)
    entry_px.place(          x=200,y=180)
    entry_py.place(          x=260,y=180)
    entry_delta.place(       x=320,y=180)
    entry_ndvi_min.place(    x=240,y=210)
    entry_ndvi_max.place(    x=300,y=210)
    entry_fdi_min.place(     x=240,y=240)
    entry_fdi_max.place(     x=300,y=240)
    entry_savefile.place(    x=210,y=270)
    
    entry_lumi.insert(0,10000)
    entry_lumi_hist.insert(0,10000)
    entry_px.insert(0,0)
    entry_py.insert(0,0)
    entry_delta.insert(0,0)
    entry_ndvi_min.insert(0,-1)
    entry_ndvi_max.insert(0,1)
    entry_fdi_min.insert(0,0)
    entry_fdi_max.insert(0,0.1)

    entry_list = [entry_file        
                ,entry_acolite_file
                ,entry_lumi        
                ,entry_lumi_hist   
                ,entry_px          
                ,entry_py          
                ,entry_delta       
                ,entry_ndvi_min    
                ,entry_ndvi_max    
                ,entry_fdi_min     
                ,entry_fdi_max     
                ,entry_savefile]
    
    return entry_list