# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 23:00:56 2020

@author: rawre
"""

from PIL import Image
import os 
import Funciones as f
dir="./Tokens originales/"
dir_save="./Tokens/"
# dir="./TokensPeque/"
# lista=os.listdir(dir)
# img=Image.open(dir+lista[0])
# new=img.resize((64,64))
# new.save(dir_save+lista[0],'png')
# lista_fotos_64=[]
# for i in lista:
#     img=Image.open(dir+i)
#     new=img.resize((64,64))
#     lista_fotos_64.append(new)
# new.show()
# for i in p:

# img =Image.open()
f.RedimensionarCarpetaFotos(dir,64,dir_save)