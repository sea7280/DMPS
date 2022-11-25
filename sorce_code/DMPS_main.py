import tkinter as tk
import sys
sys.dont_write_bytecode = True

import DMPS_button as button
import DMPS_label as label
import DMPS_entry as entry
import DMPS_listbox as listbox
import DMPS_checkbutton as chk

class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)

        self.master.geometry("700x400")
        self.master.title("DMPS")
        self.master.configure(bg="gray80")

        label.create_label(self.master)
        self.entry_list = entry.create_entry(self.master)
        self.listbox = listbox.create_listbox(master)
        self.chk = chk.create_checkbutton(master)
        button.create_button(self.master,self.entry_list, self.listbox, self.chk)



def main():
    win = tk.Tk()
    app = Application(master=win)
    app.mainloop()

if __name__ == "__main__":
    main()