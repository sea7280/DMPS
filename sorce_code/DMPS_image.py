import matplotlib.pyplot as plt


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


