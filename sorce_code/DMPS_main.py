import tkinter as tk
import sys
sys.dont_write_bytecode = True

import DMPS_button as button
import DMPS_label as label
import DMPS_entry as entry
import DMPS_listbox as listbox
import DMPS_checkbutton as chk
import DMPS_frame as frame
class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)

        self.master.geometry("430x470")
        self.master.title("DMPS")
        self.master.configure(bg="black")

        self.frameList = frame.create_frame(master)
        label.create_label(self.frameList)
        self.entry_list = entry.create_entry(self.frameList)
        self.listbox = listbox.create_listbox(self.frameList)
        self.chk = chk.create_checkbutton(self.frameList)
        button.create_button(master, self.frameList, self.entry_list, self.listbox, self.chk)



def main():
    win = tk.Tk()
    app = Application(master=win)
    app.mainloop()

if __name__ == "__main__":
    main()