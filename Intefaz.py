# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 01:14:33 2020

@author: rawre
"""

import Clases as c
from tkinter import *
import pandas as pd



def clicked():

    res = "Nombre del personaje" + txt.get()

    lbl.configure(text= res)

# btn = Button(añadir, text="Click Me", command=clicked)

# btn.grid(column=4, row=4)
personaje_nuevo=[]
df=pd.DataFrame(columns=('Name','Iniciativa','PS'))
dic= {}
def ventana_de_añadir(df):
    r=False
    añadir = Tk()

    añadir.title("Añadir enemigo aliado")

    añadir.geometry('720x600')
    campos=["Name","Iniciativa","Ps/Daño recibido","Aliado/enemigo"]
    
    n=0
    for i in range(4):    
        lbl = Label(añadir, text=campos[i])
    
        espacio = Label(añadir,text="  ")
        lbl.grid(column=20,row=i)
    #BOTONES
    name= Entry(añadir,width=10)
    name.grid(column=21,row=0)
    
    pain=Spinbox(añadir,from_=0,to=999,width=5)
    pain.grid(column=21,row=2)
    
    ini=Spinbox(añadir,from_=0,to=40,width=5)
    ini.grid(column=21,row=1)
    
    aliade_estado=BooleanVar()
    aliade_estado.set(True)
    aliade =Checkbutton(añadir,var=aliade_estado)
    aliade.grid(column=21,row=3)
    
    
    def clicked():
        
        
     
        personaje_nuevo.append(name.get())
        personaje_nuevo.append(ini.get())
        personaje_nuevo.append(pain.get())
        personaje_nuevo.append(aliade.get())
        
        r=True
    def Cerrar():
        añadir.destroy()
        
    btn_guardar = Button(añadir,text='Guardar',command=clicked)
    btn_guardar.grid(column=10,row=10)
    btn_cerrar =Button(añadir, text='Cerrar', command=Cerrar)
    btn_cerrar.grid(column=11,row=10 )
    
    
    if r:
        
        print(personaje_nuevo)

    añadir.mainloop() 
    


ventana_de_añadir(df)
print(df)
c.Cargar()
c.lista_personajes

