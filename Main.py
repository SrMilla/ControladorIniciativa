# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 01:10:10 2020

@author: rawre
"""


from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
# import tkFont
# import tkinter as tk
# from PIL import ImageTk, Image
import tkinter.font as TkFont
listan=[]
from PIL import ImageTk, Image
import PIL
import os, sys
import Data as dt
import os
# from Clases import lista_personaje
import Funciones as f
import Clases as c
lista_personaje=[]
lista_equipo=[]
cl3=None
target=None
taget_rep=None
ruta_fotos="./imagenes/"
ruta_tokens="./Tokens/"
ruta_tokens_M="./Tokens_Medianos/"
def resolver_ruta(ruta_relativa):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath('.'), ruta_relativa)
class vp ():
    
    def __init__(self,lista_personaje):
        
        global lista_equipo
        self.pp = Tk()
        self.pp.title("Controlador de iniciativa")
        self.primerjugador_name=StringVar()
        self.primerjugador_name.set("")
        self.listan=[]
        ancho="1500"
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
        self.tab3=ttk.Frame(self.tab_control)
        
        
        # self.NPCA=ttk.Frame(self.tab3)
        # self.tab_control.add(self.NPCA, text="A")
        self.tab_control.add(self.tab1,text="Principal")
        self.tab_control.add(self.tab2,text="Tormenta de Baldur")
        self.tab_control.add(self.tab3,text="NPCs")
        self.tabNPC=ttk.Notebook((self.pp))
        
        # self.tab_controlNPCs=ttk.Notebook(self.pp)
        # self.tabA=ttk.Frame(self.tab_control)
        # self.tab_controlNPCs(self.tabA,text="A")
        
        
        self.tab_control.pack(expand=1,fill='both')
        ########################################FRAME
        
        
        
        
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
       
        # self.botonCurar = ttk.Button(self.tab1,text="Curar",command=self.curar)
        # # self.botonCurar.grid(column=9, row=3)
        # self.botonCurar.place(x=400,y=240)
        # self.botonPain = ttk.Button(self.tab1,text="Pain",command=self.danar)
        # self.botonPain.place(x=400,y=280)
        # self.botonPain.grid(column=9, row=4)
        self.botonEliminarPersonaje = Button(self.tab1,text="Eliminar personaje",command=self.eliminar)
        self.botonEliminarPersonaje.place(x=1350,y=350)
        # self.botonAnadirpersonaje = ttk.Button(self.tab1,text="Nuevo personaje",command=self.NuevoPersonaje)
        # self.botonAnadirpersonaje.grid(column=9,row=5)
        self.reset = ttk.Button(self.tab1,text="Resetear",command=self.Seleccion)
        self.reset.place(x=0,y=0)
        ##################Tablon de anuncios##############
        self.tablon= scrolledtext.ScrolledText(self.tab1,width=40,height=7.5,state=DISABLED)
        self.tablon.place(x=600,y=200)
        
        
        
        
        
        
        
        
        
        
        
        
        ################FOTOS##########################
        
        self.jpgaliado =ruta_fotos+"aliado.png"
        self.fotoAliado = ImageTk.PhotoImage(Image.open(self.jpgaliado))
        self.fotoenemi= ImageTk.PhotoImage(Image.open(ruta_fotos+"enemigo.png"))
        
        self.panel = Label(self.tab1, image = self.fotoAliado)
        self.panel.place(x=400,y=20)
        
        
        self.jpgenemigo=ruta_fotos+"enemigo.png"
        self.fotoEnemigo = ImageTk.PhotoImage(Image.open(self.jpgenemigo))
    
#########################tercera columna
        self.panel2 =Label(self.tab1,image=self.fotoenemi)
        self.panel2.place(x=1000,y=20)
        
        
        self.lap3=Label(self.tab1,text="Nombre",font=self.fuente)
        self.lap3.place(x=1000,y=150)
        self.lap4=Label(self.tab1,text="La vida",font=self.fuente)
        self.lap4.place(x=1000,y=170) 
        self.lap5=Label(self.tab1,text="Type of damage:",font=self.fuente)
        self.lap5.place(x=1000,y=190)
        
        self.combo = ttk.Combobox(self.tab1)
        self.combo['values']=dt.tipe_attack
        self.combo.place(x=1000,y=220)
        self.combo.set(dt.tipe_attack[0])
        
        self.boton_ataque_tipo=Button(self.tab1,text="Atacar",command=self.danartipo)
        self.boton_ataque_tipo.place(x=1000,y=250)
        
        self.boton_ataque_tipo=Button(self.tab1,text="Curar",command=self.curar)
        self.boton_ataque_tipo.place(x=1050,y=250)
        
        self.spinPs = ttk.Spinbox(self.tab1, from_=0,to=99)
        self.spinPs.place(x=1000,y=280)
        self.spinPs.set(0)
        
        self.combo_altered=ttk.Combobox(self.tab1)
        self.combo_altered['values']=dt.state1
        self.combo_altered.place(x=1000,y=310)
        self.combo_altered.set(dt.state1[0])
        
        self.boton_altered=Button(self.tab1,text="Añadir estado",command=self.altered)
        self.boton_altered.place(x=1000,y=340)
        
        
        self.listbox_daño = Listbox(self.tab1)
        self.listbox_daño.place(x=1200,y=20)
        
        self.listbox_estado = Listbox(self.tab1)
        self.listbox_estado.place(x=1350,y=20)
        
        self.listbox_estado_user = Listbox(self.tab1)
        self.listbox_estado_user.place(x=400,y=200)
        
     #################Tercera pestaña
        self.fotos_array=[]
        self.combo_letras=[]
        self.combo_npc=[]
        self.panel_npc=[]
        self.spin_npc=[]
        self.Button_npc=[]
        posx=120
        posy=75
        
        # self.Button_npc.append(ttk.Button(self.tab3,text="Añadir",command=self.BotonNpc(self.combo_npc[0],self.spin_npc[0])))
        # self.Button_npc.append(ttk.Button(self.tab3,text="Añadir",command=self.BotonNpc(self.combo_npc[1],self.spin_npc[1])))
        # self.Button_npc.append(ttk.Button(self.tab3,text="Añadir",command=self.BotonNpc(self.combo_npc[2],self.spin_npc[2])))
        # self.Button_npc.append(ttk.Button(self.tab3,text="Añadir",command=self.BotonNpc(self.combo_npc[3],self.spin_npc[3])))

        
        
        
        
        
        for i in range (4):
            aux=ttk.Combobox(self.tab3,width=2)
            self.combo_letras.append(aux)
            self.combo_letras[i].place(x=posx,y=posy+i*70)
            self.combo_letras[i]['values']=dt.abc
            self.combo_letras[i].set("A")            
            aux2= ttk.Combobox(self.tab3)
            self.combo_npc.append(aux2)
            self.combo_npc[i].place(x=posx+50,y=posy+i*70)
            self.combo_npc[i]['values']=dt.dic_npc["A"]
            self.combo_npc[i].set(dt.dic_npc["A"][0])
            aux3=ImageTk.PhotoImage(Image.open(ruta_tokens+dt.dic_npc["A"][0]+".png"))
            self.fotos_array.append(aux3)
            # self.fotos_array[i]=            
            aux4=Label(self.tab3,image=self.fotos_array[i])
            self.panel_npc.append(aux4)
            self.panel_npc[i].place(x=posx-70,y=posy-25+i*70)
            aux5=ttk.Spinbox(self.tab3,width=5,from_=0,to=999,)
            self.spin_npc.append(aux5)
            self.spin_npc[i].place(x=posx+200,y=posy+i*70)
            self.spin_npc[i].set(0)
            aux6=Button(self.tab3,text="Añadir",command=self.BotonNpc(self.combo_npc[i],self.spin_npc[i]))
            self.Button_npc.append(ttk.Button(self.tab3,text="Añadir"))
            self.Button_npc[i].place(x=posx+250,y=posy-5+i*70)
        self.Button_npc[0].configure(command=lambda:self.BotonNpc(self.combo_npc[0],self.spin_npc[0]))
        self.Button_npc[1].configure(command=lambda:self.BotonNpc(self.combo_npc[1],self.spin_npc[1]))
        self.Button_npc[2].configure(command=lambda:self.BotonNpc(self.combo_npc[2],self.spin_npc[2]))
        self.Button_npc[3].configure(command=lambda:self.BotonNpc(self.combo_npc[3],self.spin_npc[3]))

        
        
        
        
        
        self.combo_letras[0].bind('<<ComboboxSelected>>',lambda event:self.mostrarDicNpc(self.combo_letras[0],self.combo_npc[0], 0, self.panel_npc[0]))
        self.combo_npc[0].bind('<<ComboboxSelected>>',lambda event:self.mostrarFotoNpc(self.combo_npc[0],0, self.panel_npc[0]))
        
        self.combo_letras[1].bind('<<ComboboxSelected>>',lambda event:self.mostrarDicNpc(self.combo_letras[1],self.combo_npc[1], 1, self.panel_npc[1]))
        self.combo_npc[1].bind('<<ComboboxSelected>>',lambda event:self.mostrarFotoNpc(self.combo_npc[1],1, self.panel_npc[1]))  
        
        self.combo_letras[2].bind('<<ComboboxSelected>>',lambda event:self.mostrarDicNpc(self.combo_letras[2],self.combo_npc[2], 2, self.panel_npc[2]))
        self.combo_npc[2].bind('<<ComboboxSelected>>',lambda event:self.mostrarFotoNpc(self.combo_npc[2],2, self.panel_npc[2]))  
         
        self.combo_letras[3].bind('<<ComboboxSelected>>',lambda event:self.mostrarDicNpc(self.combo_letras[3],self.combo_npc[3], 3, self.panel_npc[3]))
        self.combo_npc[3].bind('<<ComboboxSelected>>',lambda event:self.mostrarFotoNpc(self.combo_npc[3],3, self.panel_npc[3]))  
        
        # self.combo_letras[0].bind('<<ComboboxSelected>>',lambda event:self.mostrarDicNpc(self.combo_letras[0],self.combo_npc[0], 0, self.panel_npc[0]))
        # self.combo_npc[0].bind('<<ComboboxSelected>>',lambda event:self.mostrarFotoNpc(self.combo_npc[0], 0, self.panel_npc[0]))   
        
        
        # self.combo_letra1 = ttk.Combobox(self.tab3,width=2)
        # self.combo_letra1.place(x=120,y=75)
        # self.combo_letra1['values']=dt.abc
        # self.combo_letra1.set("A")
        # self.combo_letra1.bind('<<ComboboxSelected>>',lambda event:self.mostrarDicNpc(self.combo_letra1,self.combo_npc1, 0, self.panel_npc1))
        
        
        # self.fotos_array.append(ImageTk.PhotoImage(Image.open(ruta_tokens+dt.dic_npc["A"][0]+".png")))

        # # self.foto_npc1=ImageTk.PhotoImage(Image.open(ruta_tokens+dt.dic_npc["A"][0]+".png"))
        # self.panel_npc1=Label(self.tab3,image=self.fotos_array[0])
        # self.panel_npc1.place(x=50,y=50)
        # self.combo_npc1 = ttk.Combobox(self.tab3)
        # self.combo_npc1.place(x=170,y=75)
        # self.combo_npc1['values']=dt.dic_npc["A"]
        # self.combo_npc1.set(dt.dic_npc["A"][0])
        # self.combo_npc1.bind('<<ComboboxSelected>>',lambda event:self.mostrarFotoNpc(self.combo_npc1, 0, self.panel_npc1)) 
        
                                     
        
        
        
        
        
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
        self.listbox_personajes.bind('<<ListboxSelect>>',lambda event:self.modificar_col3())
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
    def BotonNpc(self,combo2,spin):
        #solo enemigos
        global lista_personaje
        ini=int(spin.get())
        # print("Iniciativa:"+str(ini))
        # print("Nombre:"+combo2.get())
        if ini>0:
            p=c.enemigo(ini,combo2.get(),0)
            p.repe(lista_personaje)
            lista_personaje.append(p)
            self.actualizar()
    def mostrarDicNpc(self,combo,combo2,fotaca,panel):
        t=combo.get()
        combo2['values']=dt.dic_npc[t]
        combo2.set(dt.dic_npc[t][0])
        self.mostrarFotoNpc(combo2,fotaca,panel)
    def mostrarFotoNpc(self,combo,fotaca,panel):
        """
        

        Parameters
        ----------
        combo : Combobox
            Combobox del cual obtendremos el nombre del NPC.
        foto : Image
            La imagen a editar.
        panel : Panel
            Panel donde pondremos la foto.

        Returns
        -------
        Cambia la imagen del Npc.

        """
        t=combo.get()
        # print(t)
        k=Image.open(ruta_tokens+t+".png")
        # k.show()
        # print(fotaca)
        self.fotos_array[fotaca]=ImageTk.PhotoImage(k)
        # foto.show()
        panel.configure(image=self.fotos_array[fotaca])
        
    def ponerfotos3(self):
        """
        Esta funcion permite poner la foto del png en la tercera columna

        Returns
        -------
        None.

        """
        global lista_equipo
        global target
        global target_rep

        # print(target)
        t=f.buscarnombreobjetivo(lista_personaje,target,target_rep)
        # print("rrr"+str(t))
        t=lista_personaje[t]
        foto_turno=ruta_tokens_M+t.name+".png"
        if os.path.isfile(foto_turno):
            self.fotob=ImageTk.PhotoImage(Image.open(foto_turno))
            self.panel2.configure(image=self.fotob)
        else:
            if lista_personaje[0].tipo==0:
                self.panel2.configure(image=self.fotoAliado)
                
            else:
                self.panel2.configure(image=self.fotoEnemigo)
                
    def tablondañof(self):
        
        
        global target
        global lista_personaje
        global target_rep

        print(target)
        if target ==None:
            target=lista_personaje[0].name
            target_rep=lista_personaje[0].rep
        print("el daño:"+str(target))
        o=f.buscarnombreobjetivo(lista_personaje,target,target_rep)
        print(o)
        o=lista_personaje[int(o)]
        p=0
        self.listbox_daño.delete(0,END)
        for i in dt.tipe_attack:
            if 0<o.type_damage[i]:
                t=(i+":"+str(o.type_damage[i]))
                self.listbox_daño.insert(p, t)
                p+=1
    def tablonestadoobjetivo(self):
        global target
        global lista_personaje
        global target_rep

        o=f.buscarnombreobjetivo(lista_personaje,target,target_rep)
        self.listbox_estado.delete(0,END)
        p=0
        for i in lista_personaje[o].altered:
            self.listbox_estado.insert(p, i)
            p+=1
    def tablonestadouser(self):
        global lista_personaje
        self.listbox_estado_user.delete(0,END)
        p=0
        for i in lista_personaje[0].altered:
            self.listbox_estado_user.insert(p, i)
            p+=1
    def altered(self):
        global target
        global lista_personaje
        global target_rep
        a=self.combo_altered.get()
        print(a)
        t=f.buscarnombreobjetivo(lista_personaje,target,target_rep)
        lista_personaje[t].altered.append(a)
        self.tablonestadoobjetivo()
    def actualizar_col3(self):
        global target
        global lista_personaje
        self.lap3.configure(text=target.name)
        texto=""
        #Se pone la vida
        if int(lista_personaje[target].tipo)==0:
            texto+=str(lista_personaje[target].vida)
            self.lap4.configure(text=target.vida)
        else:
            texto+=str(target.danoacumulado)
            self.lap4.configure(text=target.danoacumulado)
     
    
    def modificar_col3(self):
        global target
        global target_rep
        print(target)
        target=self.listbox_personajes.curselection()[0]
        target=lista_personaje[target]
        self.lap3.configure(text=target.name+"_"+target.rep)
        if int(target.tipo)==0:
            self.lap4.configure(text=target.vida)
        else:
            self.lap4.configure(text=target.danoacumulado)
        texto=""
       
        target_rep=target.rep
        target=target.name
        
        self.tablondañof()
        self.ponerfotos3()
        self.tablonestadoobjetivo()

    
    def cargarequipo(self):
        """
        Esta funcion se encarga de cargar en lista_de_personaje los distintos personajes del equipo
        que tenga una iniciativa mayor que uno.
        ------
        How it works
        Se crea una lista vacia y esta recoge los spinbox del tab2 y luego hace un for en el cual se van añadiendo a lista de lista_personaje
        aquellos que tengan una iniciativa mayor que 0
        ------

        Returns
        -------
        None.

        """
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
                lista_equipo[n].iniciativa=i
                lista_personaje.append(lista_equipo[n])
            n+=1
        self.tablonf("SE HA UNIDO LA TORMENTA DE BALDUR")
        self.actualizar()
        
    # def cargarequipo(self):
    #     n=0
    #     for i in lista_equipo:
            
    #         self.labelEquipo=Label(self.tab2,text=i.name)
    #         self.labelEquipo.place(x=60,y=60+n)
    #         print(i.name)
    #         self.labelEquipo.place_forget()
    #         n+=20
    def tablonf(self,text):
        """
        Esta funcion se encarga de añadir texto a un textrol
        
        How it works
        ---
        Primero cambia el estado del tablon para poder editarlo,añade un salto,añade el texto y lo vuelve a cerrar
        
        
        ---
        Parameters
        text:El texto que queremos añadir al tablon
        ----------
        text : TYPE str
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.tablon.config(state='normal')
        self.tablon.insert(END,"\n")
        self.tablon.insert(END,text)        
        self.tablon.yview(END)
        self.tablon.config(state='disable')
    # def tablondañof(self,text):
    #     """
    #     Igual que la funcion tablonf(self,text)

    #     Parameters
    #     ----------
    #     text : TYPE
    #         DESCRIPTION.

    #     Returns
    #     -------
    #     None.

    #     """
    #     self.tablondaño.config(state='normal')
    #     self.tablondaño.insert(END,"\n")
    #     self.tablondaño.insert(END,text)        
    #     self.tablondaño.yview(END)
    #     self.tablondaño.config(state='disable')
        
    def Vaciar(self):
        """
        Esta funcion resetea tanto la lista_personake como la listbox

        Returns
        -------
        None.

        """
        global lista_personaje
        lista_personaje=[]
        self.listbox_personajes.delete(0,END)
        
    def Cargar(self):
        """
        Esta funcion simplemente vacia la lista_personaje y luego llama a la funcion Cargar y esta devuelve una partida que estaba a medias

        Returns
        -------
        None.

        """
        global lista_personaje
        lista_personaje = []
        f.Cargar()
        lista_personaje=c.lista_personajes.copy()
        self.tablonf("¡Se ha cargado los personajes!")

        self.actualizar()
    def PasarTurno(self):
        """
        Esta funcion pasa de turno poniendo al primero como el ultimo y el segundo primero y asi consecutivamente
        ------
       
        Primero lo anuncia en el tablon,luego llama a la funcion pasar turno y anuncia de quien es el turno

        Returns
        -------
        None.

        """
        global lista_personaje
        text=(lista_personaje[0].name+"_"+lista_personaje[0].rep+ "ha terminado su turno")
        self.tablonf(text)
        f.pasar_turno(lista_personaje)#se carga
        text="Es el turno de "+lista_personaje[0].name+"_"+lista_personaje[0].rep
       
        self.tablonf(text)

        self.actualizar()
    def actualizar(self):
        """
        

        Returns
        -------
        None.

        """
        global lista_personaje
        self.listbox_personajes.delete(0,END)#se vacia
        n=0
        for i in lista_personaje:
            if(i.tipo==0):
                t=i.name+"_"+i.rep+'     PS:'+str(i.vida)
                self.listbox_personajes.insert(END,t)
                self.listbox_personajes.itemconfigure(n,bg="#00aa00", fg="#fff")

            else:
                t=i.name+"_"+i.rep+'     DR:'+str(i.danoacumulado)
                self.listbox_personajes.insert(END,t)
                self.listbox_personajes.itemconfigure(n,bg="#ff0000", fg="#fff")
            n+=1
        foto_turno=ruta_tokens_M+lista_personaje[0].name+".png"
        if os.path.isfile(foto_turno):
            self.fotoa=ImageTk.PhotoImage(Image.open(foto_turno))
            self.panel.configure(image=self.fotoa)
            if lista_personaje[0].tipo==0:
                self.lap2.configure(text=lista_personaje[0].vida)
                self.lta2.configure(text="Con vida:")
            else:
                self.lap2.configure(text=lista_personaje[0].danoacumulado)
                self.lta2.configure(text="Con un daño de:")
        else:
            if lista_personaje[0].tipo==0:
                self.panel.configure(image=self.fotoAliado)
                self.lap2.configure(text=lista_personaje[0].vida)
                self.lta2.configure(text="Con vida:")
            else:
                self.panel.configure(image=self.fotoEnemigo)
                self.lap2.configure(text=lista_personaje[0].danoacumulado)
                self.lta2.configure(text="Con un daño de:")
        self.lap.configure(text=lista_personaje[0].name)
        self.tablondañof()
        self.tablonestadoobjetivo()
        self.tablonestadouser()

    def eliminar(self):
        global lista_personaje
        w=self.listbox_personajes.curselection()
        w=w[0]
        p=lista_personaje[w]
        lista_personaje.remove(p)
        text=("Se ha eliminado a "+p.name+"a manos de "+lista_personaje[0].name)
        self.tablonf(text)
        self.actualizar()

    def curar(self):
        global lista_personaje
        global target
        global target_rep

        w=f.buscarnombreobjetivo(lista_personaje,target,target_rep)

        # w=self.listbox_personajes.curselection()
        # w=w[0]
        lista_personaje[w].curar(int(self.spinPs.get()))
        text=("Se han curado "+(self.spinPs.get())+" PSs a "+lista_personaje[w].name)
        if lista_personaje[w].tipo==0:
            self.lap4.configure(text=lista_personaje[w].vida)
        else :
            self.lap4.configure(text=lista_personaje[w].danoacumulado)
        self.tablonf(text)
        self.spinPs.set(0)
        self.actualizar()
        
        
    def danar(self):
        global lista_personaje
        global target_rep
        global target

        w=f.buscarnombreobjetivo(lista_personaje,target,target_rep)
        # w=w[0]
        lista_personaje[w].atacar(int(self.spinPs.get()))
        text=lista_personaje[w].name+" ha recibido "+self.spinPs.get()+" de daño por parte de "+lista_personaje[0].name
        self.tablonf(text)
        self.spinPs.set(0)
        self.actualizar()
    def danartipo(self):
        global lista_personaje
        global target
        global target_rep

        t=self.combo.get()
        # print(t)
        # w=self.listbox_personajes.curselection()
        # print(w)
        # print(target)
        w=f.buscarnombreobjetivo(lista_personaje,target,target_rep)
        # print(w)
        # w=w[0]
        lista_personaje[w].type_damage[t]+=int(self.spinPs.get())
        lista_personaje[w].atacar(int(self.spinPs.get()))
        
        text=lista_personaje[w].name+" ha recibido "+self.spinPs.get()+" de daño "+t+" por parte de "+lista_personaje[0].name
        if lista_personaje[w].tipo==0:
            self.lap4.configure(text=lista_personaje[w].vida)
        else :
            self.lap4.configure(text=lista_personaje[w].danoacumulado)
        self.tablonf(text)
        self.spinPs.set(0)
        self.actualizar()
        
    def Guardar(self):
        """
        Esta funcion simplemente se encarga de guardar los datos de la partida actual en un csv
        
        ppp
        -------
        cosa

        Returns
        -------
        None.

        """
        global lista_personaje
        self.tablonf("Se han guardado los datos")
        f.Guardar(lista_personaje)
  
    # def NuevoPersonaje(self):
    #     self.listan=[]
    #     print(self.listan)
    #     t=vNP(self)
    #     self.pp.wait_window(t.pantalla)
    
    
    
    
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
        text="Se ha añadido a "+nombre+" con "+str(vida)+ " de daño/vida y "+str(iniciativa)+" de iniciativa"
        self.tablonf(text)
        self.actualizar()
        self.spinPSNuevo2.set(0)
        self.spinIniciativa.set(1)
        # self.entryNombre.insert("")
      
        # print(iniciativa)
        # print(vida)
       
        # print(nombre)
    
        # print(self.listan)

   
        #PONER LO DE: ESTAS SEGURO DE ELIMINAR A *****
        
        
        
        
    def Seleccion(self):  
        global lista_personaje   
        n=len(lista_personaje)                        #Se le pasa un vector y su tamano
        for i in range(0,n-1):                      #Se recorre el vector desde la primera posicion a la ultima
            min=i                                  #Se toma como minimo el elemento en la posicion i  
            for j in range(i+1,n):                  #Se inicia un segundo recorrido saltandose la primera posicion
                if lista_personaje[min].iniciativa < lista_personaje[j].iniciativa:                   #Si el minimo tomado anteriormente es superior a alguno del segundo recorrido
                    min=j                           
            aux=lista_personaje[min]
            lista_personaje[min]=lista_personaje[i]
            lista_personaje[i]=aux
        self.actualizar()
            # lin[min]=lin[i] 
            # lin[i]=aux  
            # lid[i]=aux2
        
                
        
        
        
        
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
    
if __name__== '__main__':
    t=vp(lista_personaje)
    
# vNP()
# p.Cargar()
# p=c.lista_personajes