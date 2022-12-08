import matplotlib.pyplot as plt
import sys
sys.dont_write_bytecode = True
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

#------------------------------------ image ---------------------------------------
def image_create(data,min,max,title):
        plt.figure(figsize=(7,5))
        #先ほど配列に変換したデータの輝度値について、300本の柱で表示することにします
        plt.hist(data.flatten(),bins=300,range=(min, max))

        plt.figure(figsize=(7,5))
        plt.imshow(data,vmin=min,vmax=max,cmap='Oranges')
        plt.title(title)
        plt.colorbar()

        plt.show()
        plt.close()

def image_create_double(dataA,dataB,minA,maxA,minB,maxB):

        plt.figure(figsize=(10,6))
        plt.subplot(1,2,1)
        plt.imshow(dataA,vmin=minA,vmax=maxA,cmap='Oranges')
        plt.title("NDVI")
        plt.colorbar()

        plt.subplot(1,2,2)
        plt.imshow(dataB,vmin=minB,vmax=maxB,cmap='Oranges')
        plt.title("FDI")
        plt.colorbar()

        plt.show()
        plt.close()

