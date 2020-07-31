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
        
        # Frame.__init__(self, master=None)
        self.pp = Tk()
        # self.lista_personaje=lista_personaje
        self.pp.title("Controlador de iniciativa")
        self.primerjugador_name=tk.StringVar()
        self.primerjugador_name.set("")
        self.listan=[]
        
        
        
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
        print(self.listan)
        # self.nuevodispo()

        self.pp.mainloop()

    def Vaciar(self):
        self.listbox_personajes.delete(0,END)
        
    def Cargar(self):
        global lista_personaje
        lista_personaje = []
        f.Cargar()
        lista_personaje=c.lista_personajes.copy()
        print(lista_personaje[0])
        self.actualizar()
    def PasarTurno(self):
        global lista_personaje
        print("pp",lista_personaje[0])

        
        f.pasar_turno(lista_personaje)#se carga
        self.actualizar()
    def actualizar(self):
        global lista_personaje
        self.listbox_personajes.delete(0,END)#se vacia
        n=0
        print("pp",lista_personaje[0])
        for i in lista_personaje:
            p=str(i.name)
            print(p)
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
        global lista_personaje
        w=self.listbox_personajes.curselection()
        w=w[0]
        p=lista_personaje[w]
        lista_personaje.remove(p)
        self.actualizar()
        print(self.listan)

    def curar(self):
        global lista_personaje
        w=self.listbox_personajes.curselection()
        w=w[0]
        lista_personaje[w].curar(int(self.spinPs.get()))
        self.spinPs.set(0)
        self.actualizar()
    def danar(self):
        global lista_personaje
        w=self.listbox_personajes.curselection()
        w=w[0]
        lista_personaje[w].atacar(int(self.spinPs.get()))
        self.spinPs.set(0)
        self.actualizar()
    def Guardar(self):
        global lista_personaje
        f.Guardar(lista_personaje)
  
    def NuevoPersonaje(self):
        self.listan=[]
        print(self.listan)
        t=vNP(self)
        self.pp.wait_window(t.pantalla)
        
        # print(self.listan)

   
        #PONER LO DE: ESTAS SEGURO DE ELIMINAR A *****
        
        
   
        
                
        
        
        
        
        self.pp.mainloop()
class vNP:
    def __init__(self,padre):
        # self.lista=lista.copy()
        self.padre = padre
        self.tipo=BooleanVar()
        self.pantalla = Toplevel(padre.pp)
        self.pantalla.transient(padre.pp)
        self.pantalla.grab_set()
        self.pantalla.bind("<Return>", self.Guardar)
        
        self.pantalla.title("Nuevo personaje")
        self.pantalla.geometry('350x200')
        
        self.entryNombre=Entry(self.pantalla,width=10)
        self.entryNombre.grid(column=1, row=0)
        
        self.lNombre=Label(self.pantalla,text="Nombre")
        self.lNombre.grid(column=0, row=0)

        self.spinIniciativa=ttk.Spinbox(self.pantalla,width=10,from_=0,to=99)
        self.spinIniciativa.grid(column=1,row=1)
        
        self.lIniciativa=Label(self.pantalla,text="Iniciativa:")
        self.lIniciativa.grid(column=0, row=1)

        self.spinPS=ttk.Spinbox(self.pantalla,width=10,from_=0,to=99)
        self.spinPS.grid(column=1,row=2)
        self.lPS=Label(self.pantalla,text="PS/Daño recibido:")
        self.lPS.grid(column=0, row=2)
        
       
        
        self.chekTipoAliado=ttk.Radiobutton(self.pantalla,text="Aliado",value=True,variable=self.tipo)
        self.chekTipoAliado.grid(column=1, row=3)
        
        self.chekTipoEnemigo=ttk.Radiobutton(self.pantalla,text="Enemigo",value=False,variable=self.tipo)
        self.chekTipoEnemigo.grid(column=0, row=3)
        
        self.botonGuardar=ttk.Button(self.pantalla,text="Guardar",command=self.Guardar)
        self.botonGuardar.grid(column=0, row=4)
        self.botonGuardar.bind("<Return>", self.Guardar)
        
        
     
        
        
        
        
        self.pantalla.mainloop()
        
    def Guardar(self,event=None):
        global lista_personaje
        print("El enemigo es tipo:",self.tipo.get())
        self.nombre=self.entryNombre.get()
        self.iniciativa=int(self.spinIniciativa.get())
        self.ps=int(self.spinPS.get())
        
        # print("El personaje es:",self.nombre,"con Ps:",self.ps,"y es tipo",self.tipoE)
        if self.tipo.get():
            #es aliado
            print("Es bueno")
            p=c.aliado(self.iniciativa,self.entryNombre.get(),self.ps)
        else:
            p=c.enemigo(self.iniciativa,self.entryNombre.get(),self.ps)
        lista_personaje.append(p)
        #Actualizamos la lista
        self.padre.actualizar()
        self.pantalla.destroy()
    
                
t=vp(lista_personaje)
# vNP()
# p.Cargar()
# p=c.lista_personajes