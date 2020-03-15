
from PIL import Image
import os

path =  "C:\Keras-retinanet-Training-on-custom-datasets-for-Object-Detection--master\dataset\images"
output= "C:\Keras-retinanet-Training-on-custom-datasets-for-Object-Detection--master\dataset\\"


def resize():
    dirs = os.listdir(path)
    for img in dirs:
        image = Image.open(path+img)
        name, ext = os.path.splitext(img)
        img_resize = image.resize((650, 420), Image.ANTIALIAS)
        img_resize.save(output+name+ext, quality=100)


resize()
