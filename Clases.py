# -*- coding: utf-8 -*-
# lista2=[]
# global N
"""
Created on Sat Jul 25 18:03:22 2020

@author: rawre
"""
import pandas as pd
from tkinter import *
import Funciones as f
import Data as dt

# personaje
# puntosdevida
# iniciativa
# name
# danoacumulado
lista=[]
lista_de_iniciativa=[]
lista_personajes=[]
lista_enemigos=[]
lista_aliados=[]
class personaje:
    
    def __init__(self,iniciativa,name):
        self.iniciativa=iniciativa
        self.name=name
        self.id=id(self)
        self.rep=""
        lista.append(id(self))
        lista_de_iniciativa.append(iniciativa)
        lista_personajes.append(self)
        self.type_damage=dict() 
        for i in dt.tipe_attack:
            p=i
            self.type_damage[i]=0
        self.altered=[]
    def cambiariniciativa(self,l):
        self.iniciativa=l
    def ponerImagen(self,imagen):
        self.jpg =imagen
        # self.foto = ImageTk.PhotoImage(Image.open(self.jpg))
    def repe(self,lista):
        t=f.saberRepeticion(lista,self.name)
        self.rep=t
class enemigo(personaje):
    def __init__(self,iniciativa,name):
        self.danoacumulado=0
        self.tipo=1
        self.jpg="None"
        personaje.__init__(self,iniciativa,name)
        lista_enemigos.append(self)
        
        # msg=('Se ha anadido a {0} con {1} de iniciativa')
        # print(msg.format(self.name,self.iniciativa))
    def __init__(self,iniciativa,name,ps):
        # self.danoacumulado=0
        self.tipo=1
        self.jpg="None"

        self.danoacumulado=ps
        personaje.__init__(self,iniciativa,name)
        lista_enemigos.append(self)
        # msg=('Se ha anadido a {0} con {1} de iniciativa')
        # print(msg.format(self.name,self.iniciativa))
    
    def atacar(self,ps):
        self.danoacumulado+=ps
    def curar(self,ps):
        self.atacar(-ps)
        if self.danoacumulado<0:
            self.danoacumulado=0
class aliado(personaje):
    def __init__(self,iniciativa,name,vida):
        self.tipo=0
        self.vida=vida
        self.jpg="None"
        self.rep=""
        personaje.__init__(self,iniciativa,name)
        lista_aliados.append(self)
        # msg=('Se ha anadido a {0} con {1} de iniciativa y {2}')
        # print(msg.format(self.name,self.iniciativa,self.vida))
    def atacar(self,ps):
        self.vida=self.vida-ps
        if self.vida<1:
            lista_aliados.remove(self)
            lista_personajes.remove(self)
    def curar(self,ps):
        self.atacar(-ps)

# f.menu(lista_personajes,lista_de_iniciativa,lista_aliados,lista_enemigos)