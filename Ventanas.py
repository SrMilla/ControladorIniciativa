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
        
        self.botonVaciar =ttk.Button(self.pp,text="Vaciar",command=self.Vaciar)
        self.botonVaciar.grid(column=9,row=3)
        
        self.botonPasarturno = ttk.Button(self.pp,text="Siguiente turno",command=self.PasarTurno)
        self.botonPasarturno.grid(column=9,row=4)
        
        self.botonPasarturno = ttk.Button(self.pp,text="Eliminar personaje",command=self.eliminar)
        self.botonPasarturno.grid(column=9,row=1)
       
        self.personaje = Label(self.pp,textvariable=self.primerjugador_name)
        self.personaje.grid(column=1,row=1)
        
        # bio_label = Label(self.pp, text="Biografía:")
        # bio_label.grid(row=6, column=0, sticky="e", padx=2, pady=2)
        
        # bio_texto = Text(self.pp, width=15, height=5)
        # bio_texto.grid(row=6, column=1, padx=2, pady=2)
        
        scrollbar_personaje = Scrollbar(self.pp)  
        # scrollbar_personaje.pack(side = RIGHT, fill = Y)  
        
        self.listbox_personajes = Listbox(self.pp, yscrollcommand = scrollbar_personaje.set )  
        self.listbox_personajes.grid(column=4, row=5)
        scrollbar_personaje.config(command=self.listbox_personajes.yview)
        
        






        self.pp.mainloop()

    def Vaciar(self):
        self.listbox_personajes.delete(0,END)
        
    def Cargar(self):
        self.lista_personaje = []
        f.Cargar()
        self.lista_personaje=c.lista_personajes.copy()
        self.actulizar()
    def PasarTurno(self):
        f.pasar_turno(self.lista_personaje)#se carga
        self.actulizar()
    def actulizar(self):
        print("w")
        self.listbox_personajes.delete(0,END)#se vacia
        n=0
        for i in self.lista_personaje:
            p=str(i.name)
            # p+=t
            if(i.tipo==0):
                t=i.name+'\t PS:'+str(i.vida)
                self.listbox_personajes.insert(END,t)
                self.listbox_personajes.itemconfigure(n,bg="#00aa00", fg="#fff")
                
            else:
                self.listbox_personajes.insert(END,p)
                self.listbox_personajes.itemconfigure(n,bg="#ff0000", fg="#fff")
            n+=1
    def eliminar(self):
        w=self.listbox_personajes.curselection()
        w=w[0]
        p=self.lista_personaje[w]
        self.lista_personaje.remove(p)
        self.actulizar()
        
        
        
        #PONER LO DE: ESTAS SEGURO DE ELIMINAR A *****
        
        
        
        
        
        
        # self.pp.updateGUI()
        
    # def ActualizarLista
        
                
        
        
        
        
        self.pp.mainloop()
p=vp(lista_personaje)

# p.Cargar()
# p=c.lista_personajes