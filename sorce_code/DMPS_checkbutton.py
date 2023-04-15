#チェックボタンの生成ファイル

#ライブラリの読み込み
import tkinter as tk

#チェックの端生成関数
def create_checkbutton(area):
    #色の指定
    background = "black"
    fontcolor = "green2"
    #出力先フレームの設定
    settingsArea = area[0]
# チェックONにする
    bln = tk.BooleanVar()
    bln.set(True)

    # チェックボタン作成
    chk = tk.Checkbutton(settingsArea, variable=bln, bg=background, fg=fontcolor)
    chk.place(x=290, y=360)
    #ウィジェットを返り値として渡す
    return bln