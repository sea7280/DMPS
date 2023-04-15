import tkinter as tk
import sys
sys.dont_write_bytecode = True

def create_label(area):
    setteingFrame   = area[0]
    runFrame = area[1]
    customFrame  = area[2]
    

    background = "black"
    fontcolor = "green2"

################################################# main #################################################
    setpositionY = 30
    label = tk.Label(setteingFrame, text=u'Settings'        , bg=background, fg=fontcolor, font=("",14)).place(x=10, y=0)
    label = tk.Label(setteingFrame, text=u'Load Settings→'   ,
                    bg=background, fg=fontcolor, font=("",13)).place(x=5, y=setpositionY)
    label = tk.Label(setteingFrame, text=u'Data:'           , bg=background, fg=fontcolor, font=("",13)).place(x=5, y=setpositionY + 30)
    label = tk.Label(setteingFrame, text=u'ACOLITE:'        , bg=background, fg=fontcolor, font=("",13)).place(x=5, y=setpositionY + 60)
    label = tk.Label(setteingFrame, text=u'Luminance'       , bg=background, fg=fontcolor, font=("",13)).place(x=50, y=setpositionY + 90)
    label = tk.Label(setteingFrame, text=u'Luminance hist'  , bg=background, fg=fontcolor, font=("",13)).place(x=50, y=setpositionY + 120)
    label = tk.Label(setteingFrame, text=u'Top left point'  , bg=background, fg=fontcolor, font=("",13)).place(x=50, y=setpositionY + 150)
    label = tk.Label(setteingFrame, text=u':'               , bg=background, fg=fontcolor, font=("",13)).place(x=263,y=setpositionY + 151)
    label = tk.Label(setteingFrame, text=u'Sampling range'  , bg=background, fg=fontcolor, font=("",13)).place(x=50, y=setpositionY + 180)
    label = tk.Label(setteingFrame, text=u'×'               , bg=background, fg=fontcolor, font=("",13)).place(x=257,y=setpositionY + 181)
    label = tk.Label(setteingFrame, text=u'NDVI Range'      , bg=background, fg=fontcolor, font=("",13)).place(x=50, y=setpositionY + 210)
    label = tk.Label(setteingFrame, text=u'〜'              , bg=background, fg=fontcolor, font=("",13)).place(x=257,y=setpositionY + 210)
    label = tk.Label(setteingFrame, text=u'FDI Range'       , bg=background, fg=fontcolor, font=("",13)).place(x=50, y=setpositionY + 240)
    label = tk.Label(setteingFrame, text=u'〜'              , bg=background, fg=fontcolor, font=("",13)).place(x=257,y=setpositionY + 240)
    label = tk.Label(setteingFrame, text=u'Save File Name'  , bg=background, fg=fontcolor, font=("",13)).place(x=10, y=setpositionY + 270)
    label = tk.Label(setteingFrame, text=u'plot title'      , bg=background, fg=fontcolor, font=("",13)).place(x=10, y=setpositionY + 300)
    label = tk.Label(setteingFrame, text=u'Check if you want to standardize. →'
                                                            , bg=background, fg=fontcolor, font=("",13)).place(x=5,  y=setpositionY + 330)
    label = tk.Label(setteingFrame, text=u'Teacher data'    , bg=background, fg=fontcolor, font=("",13)).place(x=5,  y=setpositionY + 360)

################################################# button #################################################
    label = tk.Label(runFrame,      text=u'Run'             , bg=background, fg=fontcolor, font=("",11)).place(x=10, y=0)
    label = tk.Label(runFrame, text=u'Analyze satellite data and generate images from each button.'
                                                            , bg=background, fg=fontcolor, font=("",10)).place(x=5,  y=setpositionY)

################################################# custom #################################################

    label = tk.Label(customFrame, text=u'a : blueband'         , bg=background, fg=fontcolor, font=("",14)).place(x=20,  y=setpositionY)
    label = tk.Label(customFrame, text=u'b : greenband'        , bg=background, fg=fontcolor, font=("",14)).place(x=20,  y=setpositionY+30)
    label = tk.Label(customFrame, text=u'c : redband'          , bg=background, fg=fontcolor, font=("",14)).place(x=20,  y=setpositionY+60)
    label = tk.Label(customFrame, text=u'd : nirband'          , bg=background, fg=fontcolor, font=("",14)).place(x=20,  y=setpositionY+90)
    label = tk.Label(customFrame, text=u'e : acolite blueband' , bg=background, fg=fontcolor, font=("",14)).place(x=200,  y=setpositionY)
    label = tk.Label(customFrame, text=u'f : acolite greenband', bg=background, fg=fontcolor, font=("",14)).place(x=200,  y=setpositionY+30)
    label = tk.Label(customFrame, text=u'g : acolite redband'  , bg=background, fg=fontcolor, font=("",14)).place(x=200,  y=setpositionY+60)
    label = tk.Label(customFrame, text=u'h : acolite nirband'  , bg=background, fg=fontcolor, font=("",14)).place(x=200,  y=setpositionY+90)
    label = tk.Label(customFrame, text=u'i : acolite RE2band'  , bg=background, fg=fontcolor, font=("",14)).place(x=200,  y=setpositionY+120)
    label = tk.Label(customFrame, text=u'j : acolite SWIRband' , bg=background, fg=fontcolor, font=("",14)).place(x=200,  y=setpositionY+150)
    label = tk.Label(customFrame, text=u'ndvi : ndvi'          , bg=background, fg=fontcolor, font=("",14)).place(x=20,  y=setpositionY+120)
    label = tk.Label(customFrame, text=u'fdi  : fdi'            , bg=background, fg=fontcolor, font=("",14)).place(x=20,  y=setpositionY+150)

    label = tk.Label(customFrame, text=u'A', bg=background, fg=fontcolor, font=("",12)).place(x=10,  y=220)
    label = tk.Label(customFrame, text=u'B', bg=background, fg=fontcolor, font=("",12)).place(x=10,  y=310)
################################################# point #################################################
    #label = tk.Label(detectionFrame, text=u'Plastic Point'  , bg=background, fg=fontcolor, font=("",10)).place(x=10, y=0)