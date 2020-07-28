# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 01:10:10 2020

@author: rawre
"""


from tkinter import *
from tkinter import ttk
import tkinter as tk

# from Clases import lista_personaje
import Funciones as f
import Clases as c
lista_personaje=[]
class vp ():
    def __init__(self,lista_personaje):
        self.pp = Tk()
        self.lista_personaje=lista_personaje
        self.pp.title("Controlador de iniciativa")
        self.primerjugador_name=tk.StringVar()
        self.primerjugador_name.set("")
        
        self.lta= Label(self.pp,text="El turno es de\tCon vida")
        self.lta.grid(column=1,row=0)
        
        self.botonCargar= ttk.Button(self.pp,text="Cargar",command=self.Cargar)
        self.botonCargar.grid(column=9,row=2)
        
        
       
        self.personaje = Label(self.pp,textvariable=self.primerjugador_name)
        self.personaje.grid(column=1,row=1)
        
        bio_label = Label(self.pp, text="Biografía:")
        bio_label.grid(row=6, column=0, sticky="e", padx=2, pady=2)
        
        bio_texto = Text(self.pp, width=15, height=5)
        bio_texto.grid(row=6, column=1, padx=2, pady=2)
        
        scroll_vert = Scrollbar(self.pp, command=bio_texto.yview)
        scroll_vert.grid(row=6, column=2, sticky="nsew")
        bio_texto.config(yscrollcommand=scroll_vert.set)
                
        






        self.pp.mainloop()


    def Cargar(self):
        f.Cargar()
        self.lista_personaje=c.lista_personajes.copy()
        p=c.lista_personajes[0].name
        p=self.lista_personaje[0].name

        # self.pp.update()
        # self.pp.after(0,vp)
        print(p)
        self.primerjugador_name.set(p)
        
        
        # self.pp.updateGUI()
        
    
        
                
        
        
        
        
        self.pp.mainloop()
p=vp(lista_personaje)
c=p.lista_personaje
# p.Cargar()
# p=c.lista_personajes