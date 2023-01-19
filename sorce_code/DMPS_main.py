#ソフトウェアの起動ファイル

#ライブラリの読み込み
import tkinter as tk
import sys
sys.dont_write_bytecode = True
#別ファイルの紐付け
import DMPS_button as button
import DMPS_label as label
import DMPS_entry as entry
import DMPS_listbox as listbox
import DMPS_checkbutton as chk
import DMPS_frame as frame
import DMPS_textbox as textbox

#Applicationクラスの定義
class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)

        #メインウィンドウの生成
        self.master.geometry("430x470")
        self.master.title("DMPS")
        self.master.configure(bg="black")
        #フレームの生成。返り値をself.frameListで保持
        self.frameList = frame.create_frame(master)
        #ラベル生成
        label.create_label(self.frameList)
        #入力箇所（entry）の生成。返り値をself.entry_listで保持
        self.entry_list = entry.create_entry(self.frameList)
        #リストボックスの生成。返り値をself.listboxで保持
        self.listbox = listbox.create_listbox(self.frameList)
        #チェックボタンの生成。返り値をself.chkで保持
        self.chk = chk.create_checkbutton(self.frameList)
        #テキストボックスを生成。返り値をself.textboxで保持
        self.textbox = textbox.create_textbox(self.frameList)
        #ボタンの生成。フレーム、entry、リストボックス、チェックボタン、テキストボックスの変数を渡している
        button.create_button(master, self.frameList, self.entry_list, self.listbox, self.chk, self.textbox)

#Applicationの実行関数
def main():
    win = tk.Tk()
    app = Application(master=win)
    app.mainloop()



        
if __name__ == "__main__":
    #window = threading.Thread(target=main(), daemon=True)
    #window.start()
    main()