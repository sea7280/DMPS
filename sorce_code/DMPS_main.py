import tkinter as tk

import DMPS_button as button
import DMPS_label as label
import DMPS_entry as entry

class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)

        self.master.geometry("700x350")
        self.master.title("DMPS")
        self.master.configure(bg="gray80")
        
        button.create_button(self.master)
        label.create_label(self.master)
        entry_list = entry.create_entry(self.master)

def main():
    win = tk.Tk()
    app = Application(master=win)
    app.mainloop()

if __name__ == "__main__":
    main()