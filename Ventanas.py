# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 01:10:10 2020

@author: rawre
"""


from tkinter import *
from tkinter import ttk
import tkinter as tk
listan=[]
from PIL import ImageTk, Image
# from Clases import lista_personaje
import Funciones as f
import Clases as c
lista_personaje=[]
lista_equipo=[]
class vp ():
    
    def __init__(self,lista_personaje):
        global lista_equipo
        # Frame.__init__(self, master=None)
        self.pp = Tk()
        # self.lista_personaje=lista_personaje
        self.pp.title("Controlador de iniciativa")
        self.primerjugador_name=tk.StringVar()
        self.primerjugador_name.set("")
        self.listan=[]
        ancho="1000"
        largo="420"
        pant=ancho+"x"+largo
        ia=int(ancho)
        il=int(largo)
        self.fuente= "BookAntiqua 11"
        self.pp.geometry(pant)
        #############################Pestañas############
        self.tab_control=ttk.Notebook(self.pp)
        self.tab1=ttk.Frame(self.tab_control)
        self.tab2=ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1,text="Principal")
        self.tab_control.add(self.tab2,text="Tormenta de Baldur")
        self.tab_control.pack(expand=1,fill='both')
        
        
        
        
        ########################################3
        self.lta= Label(self.tab1,text="El turno es de:",font = self.fuente)
        # self.lta.grid(column=0,row=0)
        self.lta.place(x=60,y=60)
        
        self.lap=Label(self.tab1,text="Primer personaje",font = self.fuente)
        self.lap.place(x=180,y=60)
        
        
        self.lta2= Label(self.tab1,text="Con vida:",font = self.fuente)
        self.lta2.place(x=60,y=80)
        self.lap2=Label(self.tab1,text="Vida del primer personaje",font = self.fuente)
        self.lap2.place(x=180,y=80)
        # self.lta2.grid(column=0,row=2)
        
        # self.lta2 = Label
        # NO NECESARIO YA QUE ESTA EN EL MENU
        # self.botonCargar= ttk.Button(self.tab1,text="Cargar",command=self.Cargar)
        # self.botonCargar.grid(column=9,row=2)
        
        # self.botonVaciar =ttk.Button(self.tab1,text="Vaciar",command=self.Vaciar)
        # self.botonVaciar.grid(column=9,row=3)
        ################AÑADIR PERSONAJE##############################
        
        
        
        
        self.labelNombreNuevo=Label(self.tab1,text="Nombre personaje nuevo:",font=self.fuente)
        self.labelNombreNuevo.place(x=600,y=60)
        
        self.labelPsNuevo=Label(self.tab1,text="Vida personaje nuevo:",font=self.fuente)
        self.labelPsNuevo.place(x=600,y=80)
        
        self.labelIniciativaNuevo=Label(self.tab1,text="Iniciativa personaje:",font=self.fuente)
        self.labelIniciativaNuevo.place(x=600,y=100)
        
        self.entryNombre=Entry(self.tab1)
        self.entryNombre.place(x=780,y=60)
        
        self.spinIniciativa=ttk.Spinbox(self.tab1,width=10,from_=0,to=99)
        self.spinIniciativa.set(1)
        self.spinIniciativa.place(x=780,y=100)
        
        self.spinPSNuevo2=ttk.Spinbox(self.tab1,width=10,from_=0,to=999)
        self.spinPSNuevo2.set(0)
        self.spinPSNuevo2.place(x=780,y=80)
        
        
        
        self.tiponuevo=BooleanVar()

        self.chekTipoAliado=ttk.Radiobutton(self.tab1,text="Aliado",value=True,variable=self.tiponuevo)
        self.chekTipoAliado.place(x=600,y=120)
        
        self.chekTipoEnemigo=ttk.Radiobutton(self.tab1,text="Enemigo",value=False,variable=self.tiponuevo)
        self.chekTipoEnemigo.place(x=780,y=120)

        self.botonNuevoPersonaje=ttk.Button(self.tab1,text="Añadir personaje",command=self.AnadirPersonaje)
        self.botonNuevoPersonaje.place(x=690,y=150)
        
        
        
        #########################BOTONES#####################################
        
        
        
        self.botonPasarturno = ttk.Button(self.tab1,text="Siguiente turno:",command=self.PasarTurno)
        # self.botonPasarturno.grid(column=0,row=1)
        self.botonPasarturno.place(x=400,y=160)
        # self.botonPasarturno.grid(column=9,row=2)
        # self.botonEliminarPersonaje.place(x=400,y=200)
        self.spinPs = ttk.Spinbox(self.tab1, from_=0,to=99)
        self.spinPs.place(x=400,y=200)
        self.spinPs.set(0)
        self.botonCurar = ttk.Button(self.tab1,text="Curar",command=self.curar)
        # self.botonCurar.grid(column=9, row=3)
        self.botonCurar.place(x=400,y=240)
        self.botonPain = ttk.Button(self.tab1,text="Pain",command=self.danar)
        self.botonPain.place(x=400,y=280)
        # self.botonPain.grid(column=9, row=4)
        self.botonEliminarPersonaje = ttk.Button(self.tab1,text="Eliminar personaje",command=self.eliminar)
        self.botonEliminarPersonaje.place(x=400,y=320)
        self.botonAnadirpersonaje = ttk.Button(self.tab1,text="Nuevo personaje",command=self.NuevoPersonaje)
        # self.botonAnadirpersonaje.grid(column=9,row=5)
        
        ##########################################
        
        self.jpgaliado ="aliado.jpg"
        self.fotoAliado = ImageTk.PhotoImage(Image.open(self.jpgaliado))
        self.panel = tk.Label(self.tab1, image = self.fotoAliado)
        self.panel.place(x=400,y=20)
        
        self.jpgenemigo="enemigo.jpg"
        self.fotoEnemigo = ImageTk.PhotoImage(Image.open(self.jpgenemigo))
    

        
        
        
        # load = Image.open("aliado.jpg")
        # render = ImageTk.PhotoImage(load)
        # self.img = Label(self.tab1, image=render)
        # self.img.image = render
        # self.img.place(x=400,y=20)
        # img.grid(column=9, row=7)
        
        
        # self.personaje = Label(self.tab1,textvariable=self.primerjugador_name)
        # self.personaje.grid(column=1,row=1)
        
        
        
        
        
        
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
        
        scrollbar_personaje = Scrollbar(self.tab1)  
        # scrollbar_personaje.pack(side = RIGHT, fill = Y)  
        
        self.listbox_personajes = Listbox(self.tab1, yscrollcommand = scrollbar_personaje.set,width=35,height=10,font = self.fuente)  
        # self.listbox_personajes.grid(column=1, row=1)
        scrollbar_personaje.config(command=self.listbox_personajes.yview)
        self.listbox_personajes.place(x=60,y=150)
        # self.nuevodispo()
        ####################LAD 2################
        f.cargarequipo(lista_equipo)

        


        self.labelequipo1=Label(self.tab2,text=lista_equipo[0].name,font=self.fuente)
        self.labelequipo2=Label(self.tab2,text=lista_equipo[1].name,font=self.fuente)
        self.labelequipo3=Label(self.tab2,text=lista_equipo[2].name,font=self.fuente)
        self.labelequipo4=Label(self.tab2,text=lista_equipo[3].name,font=self.fuente)
        self.labelequipo5=Label(self.tab2,text=lista_equipo[4].name,font=self.fuente)
        self.labelequipo6=Label(self.tab2,text=lista_equipo[5].name,font=self.fuente)
        self.labelequipo7=Label(self.tab2,text=lista_equipo[6].name,font=self.fuente)
        self.labelequipo8=Label(self.tab2,text=lista_equipo[7].name,font=self.fuente)
        
        self.labelequipo1.place(x=80,y=60)
        self.labelequipo2.place(x=80,y=100)
        self.labelequipo3.place(x=80,y=140)
        self.labelequipo4.place(x=80,y=180)
        self.labelequipo5.place(x=600,y=60)
        self.labelequipo6.place(x=600,y=100)
        self.labelequipo7.place(x=600,y=140)
        self.labelequipo8.place(x=600,y=180)
        
        self.spinIniE1=Spinbox(self.tab2,from_=0,to=99,width=3)
        self.spinIniE2=Spinbox(self.tab2,from_=0,to=99,width=3)
        self.spinIniE3=Spinbox(self.tab2,from_=0,to=99,width=3)
        self.spinIniE4=Spinbox(self.tab2,from_=0,to=99,width=3)
        self.spinIniE5=Spinbox(self.tab2,from_=0,to=99,width=3)
        self.spinIniE6=Spinbox(self.tab2,from_=0,to=99,width=3)
        self.spinIniE7=Spinbox(self.tab2,from_=0,to=99,width=3)
        self.spinIniE8=Spinbox(self.tab2,from_=0,to=99,width=3)

        self.spinIniE1.place(x=220,y=60)
        self.spinIniE2.place(x=220,y=100)
        self.spinIniE3.place(x=220,y=140)
        self.spinIniE4.place(x=220,y=180)
        self.spinIniE5.place(x=740,y=60)
        self.spinIniE6.place(x=740,y=100)
        self.spinIniE7.place(x=740,y=140)
        self.spinIniE8.place(x=740,y=180)

        # self.jpge1=
        # e1=lista_equipo[0].jpg
        # print("pp",e1)
        
        # self.jpge1=lista_equipo[0].jpg
        
        # self.fotoe1=ImageTk.PhotoImage(Image.open(self.jpge1))
        # self.panele1=tk.Label(self.tab2,image=self.fotoe1)
        # self.panele1.place(x=20,y=60)












        self.botonEquipo=ttk.Button(self.tab2,text="Añadir al equipo",command=self.cargarequipo)
        self.botonEquipo.place(x=440,y=270)

        

            
        
        
        
        
        
        
        # self.cargarequipo()
        
        
        self.pp.mainloop()
    def cargarequipo(self):
        global lista_personaje
        listaen=[]
        listaen.append(int(self.spinIniE1.get()))
        listaen.append(int(self.spinIniE2.get()))
        listaen.append(int(self.spinIniE3.get()))
        listaen.append(int(self.spinIniE4.get()))
        listaen.append(int(self.spinIniE5.get()))
        listaen.append(int(self.spinIniE6.get()))
        listaen.append(int(self.spinIniE7.get()))
        listaen.append(int(self.spinIniE8.get()))
        n=0
        for i in listaen:
            if i>0:
                lista_personaje.append(lista_equipo[n])
            n+=1
        self.actualizar()
        
    # def cargarequipo(self):
    #     n=0
    #     for i in lista_equipo:
            
    #         self.labelEquipo=Label(self.tab2,text=i.name)
    #         self.labelEquipo.place(x=60,y=60+n)
    #         print(i.name)
    #         self.labelEquipo.place_forget()
    #         n+=20
    def Vaciar(self):
        self.listbox_personajes.delete(0,END)
        
    def Cargar(self):
        global lista_personaje
        lista_personaje = []
        f.Cargar()
        lista_personaje=c.lista_personajes.copy()
        self.actualizar()
    def PasarTurno(self):
        global lista_personaje

        
        f.pasar_turno(lista_personaje)#se carga
        self.actualizar()
    def actualizar(self):
        global lista_personaje
        self.listbox_personajes.delete(0,END)#se vacia
        n=0
        print("pp",lista_personaje[0])
        for i in lista_personaje:
            if(i.tipo==0):
                t=i.name+'     PS:'+str(i.vida)
                self.listbox_personajes.insert(END,t)
                self.listbox_personajes.itemconfigure(n,bg="#00aa00", fg="#fff")

            else:
                t=i.name+'     DR:'+str(i.danoacumulado)
                self.listbox_personajes.insert(END,t)
                self.listbox_personajes.itemconfigure(n,bg="#ff0000", fg="#fff")
                # self.lap2.configure(text=lista_personaje[0].danoacumulado)
            if lista_personaje[0].tipo==0:
                self.lap2.configure(text=lista_personaje[0].vida)
                self.lta2.configure(text="Con vida:")
                if lista_personaje[0].jpg == "None":
                    self.panel.configure(image=self.fotoAliado)
                else:
                    self.fotoa=ImageTk.PhotoImage(Image.open(lista_personaje[0].jpg))
                    
                    self.panel.configure(image=self.fotoa)
                    
            else:
                self.lap2.configure(text=lista_personaje[0].danoacumulado)
                self.lta2.configure(text="Con un daño de:")
                self.panel.configure(image=self.fotoEnemigo)
            
            

            n+=1
        self.lap.configure(text=lista_personaje[0].name)
        

    def eliminar(self):
        global lista_personaje
        w=self.listbox_personajes.curselection()
        w=w[0]
        p=lista_personaje[w]
        lista_personaje.remove(p)
        self.actualizar()

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
    def AnadirPersonaje(self):
        global lista_personaje
        nombre=self.entryNombre.get()
        vida=int(self.spinPSNuevo2.get())
        iniciativa=int(self.spinIniciativa.get())
        if self.tiponuevo.get() :#es aliado
            p=c.aliado(iniciativa,nombre,vida)
        else:
            p=c.enemigo(iniciativa,nombre,vida)
        lista_personaje.append(p)
        self.actualizar()
        self.spinPSNuevo2.set(0)
        self.spinIniciativa.set(0)
        # self.entryNombre.insert("")
      
        # print(iniciativa)
        # print(vida)
       
        # print(nombre)
    
        # print(self.listan)

   
        #PONER LO DE: ESTAS SEGURO DE ELIMINAR A *****
        
        
   
        
                
        
        
        
        
        self.pp.mainloop()
# class vNP:
#     def __init__(self,padre):
#         # self.lista=lista.copy()
#         self.padre = padre
#         self.tipo=BooleanVar()
#         self.pantalla = Toplevel(padre.pp)
#         self.pantalla.transient(padre.pp)
#         self.pantalla.grab_set()
#         self.pantalla.bind("<Return>", self.Guardar)
        
#         self.pantalla.title("Nuevo personaje")
#         self.pantalla.geometry('350x200')
        
#         self.entryNombre=Entry(self.pantalla,width=10)
#         self.entryNombre.grid(column=1, row=0)
        
#         self.lNombre=Label(self.pantalla,text="Nombre")
#         self.lNombre.grid(column=0, row=0)

#         self.spinIniciativa=ttk.Spinbox(self.pantalla,width=10,from_=0,to=99)
#         self.spinIniciativa.grid(column=1,row=1)
        
#         self.lIniciativa=Label(self.pantalla,text="Iniciativa:")
#         self.lIniciativa.grid(column=0, row=1)

#         self.spinPS=ttk.Spinbox(self.pantalla,width=10,from_=0,to=99)
#         self.spinPS.grid(column=1,row=2)
#         self.lPS=Label(self.pantalla,text="PS/Daño recibido:")
#         self.lPS.grid(column=0, row=2)
        
       
        
#         self.chekTipoAliado=ttk.Radiobutton(self.pantalla,text="Aliado",value=True,variable=self.tipo)
#         self.chekTipoAliado.grid(column=1, row=3)
        
#         self.chekTipoEnemigo=ttk.Radiobutton(self.pantalla,text="Enemigo",value=False,variable=self.tipo)
#         self.chekTipoEnemigo.grid(column=0, row=3)
        
#         self.botonGuardar=ttk.Button(self.pantalla,text="Guardar",command=self.Guardar)
#         self.botonGuardar.grid(column=0, row=4)
#         self.botonGuardar.bind("<Return>", self.Guardar)
        
        
     
        
        
        
        
#         self.pantalla.mainloop()
        
#     def Guardar(self,event=None):
#         global lista_personaje
#         print("El enemigo es tipo:",self.tipo.get())
#         self.nombre=self.entryNombre.get()
#         self.iniciativa=int(self.spinIniciativa.get())
#         self.ps=int(self.spinPS.get())
        
#         # print("El personaje es:",self.nombre,"con Ps:",self.ps,"y es tipo",self.tipoE)
#         if self.tipo.get():
#             #es aliado
#             print("Es bueno")
#             p=c.aliado(self.iniciativa,self.entryNombre.get(),self.ps)
#         else:
#             p=c.enemigo(self.iniciativa,self.entryNombre.get(),self.ps)
#         lista_personaje.append(p)
#         #Actualizamos la lista
#         self.padre.actualizar()
#         self.pantalla.destroy()
    
                
t=vp(lista_personaje)
# vNP()
# p.Cargar()
# p=c.lista_personajes