#entry作成ファイル

#ライブラリの読み込み
import tkinter as tk
import sys
sys.dont_write_bytecode = True

#entry作成関数
def create_entry(area):
    #出力先を指定
    settingsArea   = area[0]
    #背景色、フォントカラーの指定
    background = "black"
    fontcolor = "white"
    
    #出力座標の基準位置
    setpositionY = 90

    #entryの生成
    entry_file         = tk.Entry(settingsArea, width=50, bg=background, fg=fontcolor, font=("", 8 ))
    entry_acolite_file = tk.Entry(settingsArea, width=50, bg=background, fg=fontcolor, font=("", 8 ))
    entry_lumi         = tk.Entry(settingsArea, width=7 , bg=background, fg=fontcolor, font=("", 10),justify=tk.RIGHT)
    entry_lumi_hist    = tk.Entry(settingsArea, width=7 , bg=background, fg=fontcolor, font=("", 10),justify=tk.RIGHT)
    entry_px           = tk.Entry(settingsArea, width=7 , bg=background, fg=fontcolor, font=("", 10),justify=tk.RIGHT)
    entry_py           = tk.Entry(settingsArea, width=7 , bg=background, fg=fontcolor, font=("", 10),justify=tk.RIGHT)
    entry_deltaX       = tk.Entry(settingsArea, width=7 , bg=background, fg=fontcolor, font=("", 10),justify=tk.RIGHT)
    entry_deltaY       = tk.Entry(settingsArea, width=7 , bg=background, fg=fontcolor, font=("", 10),justify=tk.RIGHT)
    entry_ndvi_min     = tk.Entry(settingsArea, width=4 , bg=background, fg=fontcolor, font=("", 10),justify=tk.RIGHT)
    entry_ndvi_max     = tk.Entry(settingsArea, width=4 , bg=background, fg=fontcolor, font=("", 10),justify=tk.RIGHT)
    entry_fdi_min      = tk.Entry(settingsArea, width=4 , bg=background, fg=fontcolor, font=("", 10),justify=tk.RIGHT)
    entry_fdi_max      = tk.Entry(settingsArea, width=4 , bg=background, fg=fontcolor, font=("", 10),justify=tk.RIGHT)
    entry_savefile     = tk.Entry(settingsArea, width=40, bg=background, fg=fontcolor, font=("", 10))
    entry_plt_title    = tk.Entry(settingsArea, width=25, bg=background, fg=fontcolor, font=("", 10))
    entry_load_px      = tk.Entry(settingsArea, width=6 , bg=background, fg=fontcolor, font=("", 10))
    entry_load_py      = tk.Entry(settingsArea, width=6 , bg=background, fg=fontcolor, font=("", 10))
    #entry設置
    entry_file.place(        x=80,y=setpositionY  + 2)
    entry_acolite_file.place(x=80,y=setpositionY  + 22)
    entry_lumi.place(        x=150,y=setpositionY + 82)
    entry_lumi_hist.place(   x=150,y=setpositionY + 102)
    entry_px.place(          x=120,y=setpositionY + 142)
    entry_py.place(          x=190,y=setpositionY + 142)
    entry_deltaX.place(      x=120,y=setpositionY + 162)
    entry_deltaY.place(      x=190,y=setpositionY + 162)
    entry_ndvi_min.place(    x=140,y=setpositionY + 202)
    entry_ndvi_max.place(    x=190,y=setpositionY + 202)
    entry_fdi_min.place(     x=140,y=setpositionY + 222)
    entry_fdi_max.place(     x=190,y=setpositionY + 222)
    entry_savefile.place(    x=120,y=setpositionY + 262)
    entry_plt_title.place(   x=120,y=setpositionY + 302)
    entry_load_px.place(     x=580,y=330)
    entry_load_py.place(     x=635,y=330)
    
    #enrtyに初期値を設定
    entry_lumi.insert(0,10000)
    entry_lumi_hist.insert(0,10000)
    entry_px.insert(0,0)
    entry_py.insert(0,0)
    entry_deltaX.insert(0,0)
    entry_deltaY.insert(0,0)
    entry_ndvi_min.insert(0,-1)
    entry_ndvi_max.insert(0,1)
    entry_fdi_min.insert(0,0)
    entry_fdi_max.insert(0,0.1)
    entry_plt_title.insert(0,'data')
    entry_load_px.insert(0,0)
    entry_load_py.insert(0,0)

    #生成したentryを配列で保持
    entry_list = [entry_file        #0
                ,entry_acolite_file #1
                ,entry_lumi         #2
                ,entry_lumi_hist    #3
                ,entry_px           #4
                ,entry_py           #5
                ,entry_deltaX       #6
                ,entry_deltaY       #7
                ,entry_ndvi_min     #8
                ,entry_ndvi_max     #9
                ,entry_fdi_min      #10
                ,entry_fdi_max      #11
                ,entry_savefile     #12
                ,entry_plt_title    #13
                ,entry_load_px      #14
                ,entry_load_py]     #15
    #entry_listを返す
    return entry_list