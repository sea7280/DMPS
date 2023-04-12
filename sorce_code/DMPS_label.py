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
    setpositionY = 20
    label = tk.Label(setteingFrame, text=u'Settings'        , bg=background, fg=fontcolor, font=("",14)).place(x=10, y=0)
    label = tk.Label(setteingFrame, text=u'You can also load settings from the button on the right. →'   ,
                    bg=background, fg=fontcolor, font=("",10)).place(x=0, y=setpositionY + 50)
    label = tk.Label(setteingFrame, text=u'Data:'           , bg=background, fg=fontcolor, font=("",10)).place(x=20, y=setpositionY + 70)
    label = tk.Label(setteingFrame, text=u'ACOLITE:'        , bg=background, fg=fontcolor, font=("",10)).place(x=20, y=setpositionY + 90)
    label = tk.Label(setteingFrame, text=u'Set the maximum brightness.'
                                                            , bg=background, fg=fontcolor, font=("",10)).place(x=00, y=setpositionY + 110)
    label = tk.Label(setteingFrame, text=u'You can check the histogram of luminance from the button below.'
                                                            , bg=background, fg=fontcolor, font=("",10)).place(x=00, y=setpositionY + 130)
    label = tk.Label(setteingFrame, text=u'Luminance'       , bg=background, fg=fontcolor, font=("",10)).place(x=20, y=setpositionY + 150)
    label = tk.Label(setteingFrame, text=u'Luminance hist'  , bg=background, fg=fontcolor, font=("",10)).place(x=20, y=setpositionY + 170)
    label = tk.Label(setteingFrame, text=u'Please set the coordinates and range of the image.'
                                                        , bg=background, fg=fontcolor, font=("",10)).place(    x=0,  y=setpositionY + 190)
    label = tk.Label(setteingFrame, text=u'x : y ???'       , bg=background, fg=fontcolor, font=("",10)).place(x=20, y=setpositionY + 210)
    label = tk.Label(setteingFrame, text=u' : '             , bg=background, fg=fontcolor, font=("",10)).place(x=173,y=setpositionY + 211)
    label = tk.Label(setteingFrame, text=u'?? * ??'         , bg=background, fg=fontcolor, font=("",10)).place(x=20, y=setpositionY + 230)
    label = tk.Label(setteingFrame, text=u' * '             , bg=background, fg=fontcolor, font=("",10)).place(x=172,y=setpositionY + 231)
    label = tk.Label(setteingFrame, text=u'Set the maximum and minimum values for NDVI and FDI images.'
                                                            , bg=background, fg=fontcolor, font=("",10)).place(x=0,  y=setpositionY + 250)
    label = tk.Label(setteingFrame, text=u'NDVI Range'      , bg=background, fg=fontcolor, font=("",10)).place(x=20, y=setpositionY + 270)
    label = tk.Label(setteingFrame, text=u'〜'              , bg=background, fg=fontcolor, font=("",10)).place(x=171,y=setpositionY + 270)
    label = tk.Label(setteingFrame, text=u'FDI Range'       , bg=background, fg=fontcolor, font=("",10)).place(x=20, y=setpositionY + 290)
    label = tk.Label(setteingFrame, text=u'〜'              , bg=background, fg=fontcolor, font=("",10)).place(x=171,y=setpositionY + 290)
    label = tk.Label(setteingFrame, text=u'Please enter a file name.'
                                                            , bg=background, fg=fontcolor, font=("",10)).place(x=0,  y=setpositionY + 310)
    label = tk.Label(setteingFrame, text=u'Save File Name'  , bg=background, fg=fontcolor, font=("",10)).place(x=20, y=setpositionY + 330)
    label = tk.Label(setteingFrame, text=u'Set the output image name.'
                                                            , bg=background, fg=fontcolor, font=("",10)).place(x=0,  y=setpositionY + 350)
    label = tk.Label(setteingFrame, text=u'plt title'       , bg=background, fg=fontcolor, font=("",10)).place(x=20, y=setpositionY + 370)
    label = tk.Label(setteingFrame, text=u'Check if you want to standardize. →'
                                                            , bg=background, fg=fontcolor, font=("",10)).place(x=0,  y=setpositionY + 390)
    label = tk.Label(setteingFrame, text=u'Please select a teacher data. →'
                                                            , bg=background, fg=fontcolor, font=("",10)).place(x=0,  y=setpositionY + 410)

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