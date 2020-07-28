# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 01:10:10 2020

@author: rawre
"""


from tkinter import *
from tkinter import ttk
import tkinter as tk
listan=[]
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
        # NO NECESARIO YA QUE ESTA EN EL MENU
        # self.botonCargar= ttk.Button(self.pp,text="Cargar",command=self.Cargar)
        # self.botonCargar.grid(column=9,row=2)
        
        # self.botonVaciar =ttk.Button(self.pp,text="Vaciar",command=self.Vaciar)
        # self.botonVaciar.grid(column=9,row=3)
        
        self.botonPasarturno = ttk.Button(self.pp,text="Siguiente turno",command=self.PasarTurno)
        self.botonPasarturno.grid(column=9,row=1)
        
        self.botonPasarturno = ttk.Button(self.pp,text="Eliminar personaje",command=self.eliminar)
        self.botonPasarturno.grid(column=9,row=2)
       
        self.botonCurar = ttk.Button(self.pp,text="Curar",command=self.curar)
        self.botonCurar.grid(column=9, row=3)
        
        self.botonPain = ttk.Button(self.pp,text="Pain",command=self.danar)
        self.botonPain.grid(column=9, row=4)
        
        self.botonAnadirpersonaje = ttk.Button(self.pp,text="Nuevo personaje",command=self.NuevoPersonaje)
        self.botonAnadirpersonaje.grid(column=9,row=5)
        
        
        self.spinPs = ttk.Spinbox(self.pp, from_=0,to=99)
        self.spinPs.grid(column=9, row=6)
        #
        
        
        self.personaje = Label(self.pp,textvariable=self.primerjugador_name)
        self.personaje.grid(column=1,row=1)
        
        
        
        
        
        
        menu =Menu(self.pp)
        new_item = Menu(menu)
        new_item.add_command(label='Nuevo',command=self.Vaciar)
        new_item.add_command(label='Cargar csv',command=self.Cargar)
        new_item.add_command(label='Guardar csv',command=self.Guardar)
        menu.add_cascade(label='File', menu=new_item)
        self.pp.config(menu=menu)

        # bio_label = Label(self.pp, text="Biografía:")
        # bio_label.grid(row=6, column=0, sticky="e", padx=2, pady=2)
        
        # bio_texto = Text(self.pp, width=15, height=5)
        # bio_texto.grid(row=6, column=1, padx=2, pady=2)
        
        scrollbar_personaje = Scrollbar(self.pp)  
        # scrollbar_personaje.pack(side = RIGHT, fill = Y)  
        
        self.listbox_personajes = Listbox(self.pp, yscrollcommand = scrollbar_personaje.set )  
        self.listbox_personajes.grid(column=1, row=1)
        scrollbar_personaje.config(command=self.listbox_personajes.yview)
        
        

        self.pp.mainloop()

    def Vaciar(self):
        self.listbox_personajes.delete(0,END)
        
    def Cargar(self):
        self.lista_personaje = []
        f.Cargar()
        self.lista_personaje=c.lista_personajes.copy()
        self.actualizar()
    def PasarTurno(self):
        f.pasar_turno(self.lista_personaje)#se carga
        self.actualizar()
    def actualizar(self):
        self.listbox_personajes.delete(0,END)#se vacia
        n=0
        for i in self.lista_personaje:
            p=str(i.name)
            # p+=t
            if(i.tipo==0):
                t=i.name+'     PS:'+str(i.vida)
                self.listbox_personajes.insert(END,t)
                self.listbox_personajes.itemconfigure(n,bg="#00aa00", fg="#fff")
            else:
                t=i.name+'     DR:'+str(i.danoacumulado)
                self.listbox_personajes.insert(END,t)
                self.listbox_personajes.itemconfigure(n,bg="#ff0000", fg="#fff")
            n+=1
    def eliminar(self):
        w=self.listbox_personajes.curselection()
        w=w[0]
        p=self.lista_personaje[w]
        self.lista_personaje.remove(p)
        self.actualizar()
    def curar(self):
        w=self.listbox_personajes.curselection()
        w=w[0]
        self.lista_personaje[w].curar(int(self.spinPs.get()))
        self.spinPs.set(0)
        self.actualizar()
    def danar(self):
        w=self.listbox_personajes.curselection()
        w=w[0]
        self.lista_personaje[w].atacar(int(self.spinPs.get()))
        self.spinPs.set(0)
        self.actualizar()
    def Guardar(self):
        f.Guardar(self.lista_personaje)
    def NuevoPersonaje(self):
        t=vNP()
        print(listan[0])
        
        #PONER LO DE: ESTAS SEGURO DE ELIMINAR A *****
        
        
        
        
        
        
        # self.pp.updateGUI()
        
    # def ActualizarLista
        
                
        
        
        
        
        self.pp.mainloop()
class vNP():
    def __init__(self):
        
        self.pantalla = Tk()
        self.pantalla.title("Nuevo personaje")
        self.pantalla.geometry('350x200')
        
        self.entryNombre=Entry(self.pantalla,width=10)
        self.entryNombre.grid(column=0, row=0)
        
        self.spinIniciativa=ttk.Spinbox(self.pantalla,width=10,from_=0,to=99)
        self.spinIniciativa.grid(column=0,row=1)
        
        self.botonGuardar=Button(self.pantalla,text="Guardar",command=self.Guardar)
        self.botonGuardar.grid(column=0, row=2)
        
        
        
        
        self.pantalla.mainloop()
        
    def Guardar(self):
        self.iniciativa=int(self.spinIniciativa.get())
        self.nombre=self.entryNombre.get()
        listan.append(self.nombre)
        self.pantalla.destroy()

        
t=vp(lista_personaje)
# vNP()
# p.Cargar()
# p=c.lista_personajes