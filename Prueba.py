# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 01:20:19 2020

@author: rawre
"""
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

# import tkinter as tk
listan=[]
from PIL import ImageTk, Image
import PIL
import os, sys

# from Clases import lista_personaje
import Funciones as f
import Clases as c
lista_personaje=[]
lista_equipo=[]

def menu(): 
    print("¿Que quieres hacer?")
    print("1.Atacar")
    print("2.Anadir aliado")
    print("3.Anadir enemigo")
    print("4.Quitar aliado")
    print("5.Pasar turno")
    print("6.Guardar")
    print("7.Cargar")
    print("0.Salir")
    a=int((input()))
    if a==0:
        return True
    # if a==1:
    #     atacar(lista_personajes)
    #     return menu(lista_personajes,lista_de_iniciativa,lista_aliados,lista_enemigos)
    if a==2:
        print(a)
        return menu()
    if a==3:
        print(a)
        return menu()
    if a==4:
        print(a)
        return menu()
    if a==5:
        print(a)
        return menu()
    if a==6:
        print(a)
        return menu()
    if a ==7:
        print(a)
        return menu()
class vp():
    def __init__(self):
        self.pp=Tk()
        self.pp.title("Prueba")
        self.pp.geometry("1000x420")
        # self.pp.geometry(pant)

        self.jpgaliado ="aliado.jpg"
        self.fotoAliado = ImageTk.PhotoImage(Image.open("aliado.jpg"))
        self.panel = Label(self.pp, image = self.fotoAliado)
        self.panel.place(x=00,y=20)
        self.pp.mainloop()

t=vp()
# menu()