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
        lista.append(id(self))
        lista_de_iniciativa.append(iniciativa)
        lista_personajes.append(self)
    def cambiariniciativa(self,l):
        self.iniciativa=l
class enemigo(personaje):
    def __init__(self,iniciativa,name):
        self.danoacumulado=0
        self.tipo=1
        personaje.__init__(self,iniciativa,name)
        lista_enemigos.append(self)
        msg=('Se ha anadido a {0} con {1} de iniciativa')
        print(msg.format(self.name,self.iniciativa))
    def __init__(self,iniciativa,name,ps):
        # self.danoacumulado=0
        self.tipo=1
        self.danoacumulado=ps
        personaje.__init__(self,iniciativa,name)
        lista_enemigos.append(self)
        msg=('Se ha anadido a {0} con {1} de iniciativa')
        print(msg.format(self.name,self.iniciativa))
    
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
        personaje.__init__(self,iniciativa,name)
        lista_aliados.append(self)
        msg=('Se ha anadido a {0} con {1} de iniciativa y {2}')
        print(msg.format(self.name,self.iniciativa,self.vida))
    def atacar(self,ps):
        self.vida=self.vida-ps
        if self.vida<1:
            lista_aliados.remove(self)
            lista_personajes.remove(self)
    def curar(self,ps):
        self.atacar(-ps)

# f.menu(lista_personajes,lista_de_iniciativa,lista_aliados,lista_enemigos)