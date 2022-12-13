from tkinter import messagebox#listboxの選択対象を削除

def list_delete(box):
    index = box.curselection()
    if not index:
        messagebox.showerror('Error', 'Please select')
    else:
        for select in index:
            box.delete(select)