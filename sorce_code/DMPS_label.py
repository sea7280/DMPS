import tkinter as tk

def create_label(master):
    label = tk.Label(master, text=u'Select File'   , bg="gray80", font=("",12), width=12, anchor=tk.CENTER).place(x=80, y=40)
    label = tk.Label(master, text=u'Data:'         , bg="gray80", font=("",12), width=12, anchor=tk.CENTER).place(x=10, y=70)
    label = tk.Label(master, text=u'ACOLITE:'      , bg="gray80", font=("",12), width=12, anchor=tk.CENTER).place(x=10, y=90)
    label = tk.Label(master, text=u'Luminance'     , bg="gray80", font=("",12), width=12, anchor=tk.CENTER).place(x=80, y=120)
    label = tk.Label(master, text=u'Luminance hist', bg="gray80", font=("",12), width=12, anchor=tk.CENTER).place(x=80, y=150)
    label = tk.Label(master, text=u'px,py,delta'   , bg="gray80", font=("",12), width=12, anchor=tk.CENTER).place(x=80, y=180)
    label = tk.Label(master, text=u'NDVI Range'    , bg="gray80", font=("",12), width=12, anchor=tk.CENTER).place(x=80, y=210)
    label = tk.Label(master, text=u'〜'            , bg="gray80", font=("",12), width=12, anchor=tk.CENTER).place(x=230, y=210)
    label = tk.Label(master, text=u'FDI Range'     , bg="gray80", font=("",12), width=12, anchor=tk.CENTER).place(x=80, y=240)
    label = tk.Label(master, text=u'〜'            , bg="gray80", font=("",12), width=12, anchor=tk.CENTER).place(x=230, y=243)
    label = tk.Label(master, text=u'Save File Name', bg="gray80", font=("",12), width=12, anchor=tk.CENTER).place(x=80, y=270)
    label = tk.Label(master, text=u'plt title'     , bg="gray80", font=("",12), width=12, anchor=tk.CENTER).place(x=80, y=300)
    label = tk.Label(master, text=u'Plastic Point' , bg="gray80", font=("",10), width=12, anchor=tk.CENTER).place(x=580, y=30)