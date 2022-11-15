import DMPS_pathGet as pathGet
import DMPS_truecolor as truecolor

def admin(entry, mode):

    minX      = int(entry[4].get())  #0
    minY      = int(entry[5].get())  #1
    delta     = int(entry[6].get())  #2
    luminance = int(entry[2].get())  #3

    title = entry[12].get()  #3  pltタイトル

    point = [minX, minY, delta, luminance]

    satellite_filepath = pathGet.pathGet(entry)

    if mode == "rgb":
        truecolor.truecolor(satellite_filepath, point, title)