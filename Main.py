# -*- coding: utf-8 -*-
# lista2=[]
# global N
"""
Created on Sat Jul 25 18:03:22 2020

@author: rawre
"""
import pandas as pd
from tkinter import *
# personaje
# puntosdevida
# iniciativa
# name
# dañoacumulado
lista=[]
lista_de_iniciativa=[]
lista_personajes=[]
lista_enemigos=[]
lista_aliados=[]
enemigo=[]
aliado=[]
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

    # def  __str__(self):
    #     msg=("{0} con {1} de vida y un {2} de iniciativa")
    #     return msg.format(self.name,self.puntosdevida,self.iniciativa)
     
class enemigo(personaje):
    def __init__(self,iniciativa,name):
        self.dañoacumulado=0
        self.tipo=1
        personaje.__init__(self,iniciativa,name)
        lista_enemigos.append(self)
        msg=('Se ha añadido a {0} con {1} de iniciativa')
        print(msg.format(self.name,self.iniciativa))
        
        
    def añadirdaño(self,daño):
        self.dañoacumulado+=daño
    def curar(self,ps):
        self.añadirdaño(-ps)
        if self.dañoacumulado<0:
            self.dañoacumulado=0
class aliado(personaje):
    def __init__(self,iniciativa,name,vida):
        self.tipo=0
        self.vida=vida
        personaje.__init__(self,iniciativa,name)
        lista_aliados.append(self)
        msg=('Se ha añadido a {0} con {1} de iniciativa y {2}')
        print(msg.format(self.name,self.iniciativa,self.vida))
    def atacar(self,ps):
        self.vida=self.vida-ps
        if self.vida<1:
            lista_aliados.remove(self)
            lista_personajes.remove(self)
            
    def curar(self,ps):
        self.atacar(-ps)
        
    def crear(self):
        print("Nombre:")
        name=input()
        print("Iniciativa")
        iniciativa=int(input())
        print("Cuanta vida:")
        vida=int(input())
        self.__init__(iniciativa,name,vida)
        

def Seleccion(lin,n,lid):                             #Se le pasa un vector y su tamaño
    for i in range(0,n-1):                      #Se recorre el vector desde la primera posicion a la ultima
        min=i                                   #Se toma como minimo el elemento en la posicion i  
        for j in range(i+1,n):                  #Se inicia un segundo recorrido saltandose la primera posicion
            if lin[min] < lin[j]:                   #Si el minimo tomado anteriormente es superior a alguno del segundo recorrido
                min=j                           
        aux=lin[min]  
        aux2=lid[min]                            
        lin[min]=lin[i] 
        lid[min]=lid[i]                            
        lin[i]=aux  
        lid[i]=aux2
        
def pasar_turno(lista):
    aux=lista[0]
    k=len(lista)
    for i in range(k-1):
        lista[i]=lista[i+1]
    lista[k-1]=aux
    
    
def quitarpersonaje(lista_aliados,lista_enemigos,personaje,lista_personajes):
    if personaje.tipo == 0:
        lista_aliados.remove(personaje)
    else:
        lista_enemigos.remove(personaje)
    lista_personajes.remove(personaje)
    
    
def imprimirlista(lista_personajes):
    for i in lista_personajes:
        if i.tipo==0 :
            print(i.name,"\t\tPV",i.vida)
        else:
            print(i.name,"\t\tDaño acumulado:",i.dañoacumulado)
def atacar(lista):
    n=0
    print("¿A quien atacas?")
    for i in lista:
        print(n,".",i.name)
        n+=1
    victima=int(input())
   
    print("Atacas a",lista[victima].name)
    print("¿Cuanta vida le quitas?")
    daño=int(input())
    if lista[victima].tipo==0:
        lista[victima].atacar(daño)
    else:
        lista[victima].añadirdaño(daño)
        
def añadir_aliado():
    print("Nombre del aliado:")
    name=input()
    print("Cuanta iniciativa:")
    iniciativa=int(input())
    print("Cuanta vida maxima")
    vida=int(input())
    pn=aliado(iniciativa,name,vida)

def añadir_enemigo():
    print("Nombre:")
    name=input()
    print("Iniciativa:")
    iniciativa=int(input())
    pe=enemigo(iniciativa,name)
    
def ciclo():
    actual=lista_personajes[0]
    Seleccion(lista_de_iniciativa,len(lista_de_iniciativa),lista_personajes)
    while not(lista_personajes[0] == actual):
        pasar_turno(lista_personajes)
        imprimirlista(lista_personajes)
def eliminar(lista_aliados,lista_enemigos,lista_personajes): 
    print("¿A quien quieres eliminar?")
    n=0
    for i in lista_personajes:
        print(n,i.name)
        n+=1
    p=int(input())
    quitarpersonaje(lista_aliados,lista_enemigos,lista_personajes[p],lista_personajes)
def Guardar(lista_personajes):
    names=[]
    inicias=[]
    tipos=[]
    pain=[]
    for i in lista_personajes:
        names.append(i.name)
        inicias.append(i.iniciativa)
        if i.tipo == 1:
            tipos.append(1)
            pain.append(i.dañoacumulado)
        else:
            tipos.append(0)
            pain.append(i.vida)
    data = {'Name': names,
            'Iniciativa': inicias,
            'tipo':tipos,
            'PS':pain}
    df = pd.DataFrame(data,columns =['Name','Iniciativa','tipo','PS'])
    df.to_csv('Partida.csv')
def Cargar():
    df=pd.read_csv('Partida.csv')
    names = df['Name']
    inicias = df['Iniciativa']
    tipo = df['tipo']
    ps = df['PS']
    for i in range (len(names)):
        if tipo[i] == 0:#aliado
            p1=aliado(inicias[i],names[i],ps[i])
        else:
            p2=enemigo(inicias[i],names[i])
            p2.dañoacumulado=ps[i]
   
def menu(lista_personajes):
    imprimirlista(lista_personajes)
    print("¿Que quieres hacer?")
    print("1.Atacar")
    print("2.Añadir aliado")
    print("3.Añadir enemigo")
    print("4.Quitar aliado")
    print("5.Pasar turno")
    print("6.Guardar")
    
    print("7.Cargar")
    print("0.Salir")
    a=int((input()))
    if a==0:
        return True
    if a==1:
        atacar(lista_personajes)
        return menu(lista_personajes)
    if a==2:
        añadir_aliado()
        ciclo()
        return menu(lista_personajes)
    if a==3:
        añadir_enemigo()
        ciclo()
        return menu(lista_personajes)
    if a==4:
        eliminar(lista_aliados,lista_enemigos,lista_personajes)
        return menu(lista_personajes)
    if a==5:
        pasar_turno(lista_personajes)
        return menu(lista_personajes)
    if a==6:
        Guardar(lista_personajes)
        return menu(lista_personajes)
    if a ==7:
        Cargar()
        return menu(lista_personajes)
    
ventana=Tk()
ventana.title("Iniciativa")
ventana.mainloop()

   
                   
    
# p=enemigo(10,"Ogro")
# p1=aliado(18,"Ayla",113)
# p2=aliado(20,"Errol",68)
# p3=aliado(6,"Khwrsiwe",92)
# p4=aliado(11,"Rampo",87)
# p5=aliado(3,"Thalis",183)

# p=enemigo(16,"Sectario_4")#24
# p=enemigo(15,"Sectario_5")
# p=enemigo(14,"Sectario_6")
# p=enemigo(10,"Sectario_7")#24
# p=enemigo(7,"Sectario_8")
# p=enemigo(4,"Sectario_9")
# p=enemigo(11,"Mindartis") #59
# p=enemigo(20,"Zelzara")


# Seleccion(lista_de_iniciativa,len(lista_de_iniciativa),lista_personajes)

# menu(lista_personajes)
# df=pd.read_csv('Partida.csv')
# p=df['Name'][0]
# menu(lista_personajes)