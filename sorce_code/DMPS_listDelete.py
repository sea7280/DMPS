#listboxの選択対象を削除

def list_delete(box):
    box.delete(box.curselection())