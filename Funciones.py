# -*- coding: utf-8 -*-
import Clases as c
import pandas as pd
import os
from PIL import Image
def pasar_turno(lista):
    """
    Pone el primer valor en el ultimo y todos los demas los mueve uno mas
    
    Como funciona
    ----------
    Guarda en aux el primer valor luego recorre la lista de modo que el la posicion actual es ocupada por el siguiente valor. Finalmente añade el primero en ultimo lugar

    Parameters
    ----------
    lista :  Array 
        DESCRIPTION.

    Returns
    -------
    None.

    """
    aux=lista[0]
    k=len(lista)
    for i in range(k-1):
        lista[i]=lista[i+1]
    lista[k-1]=aux
def Seleccion(lin,n,lid):                            
    """
    Empleando el metodo de seleccion ordena la lista dependiendo de la inicitiva de mayor a menor

    Parameters
    ----------
    lin : array
        Es la una lista con las iniciativas .
    n : int
        Es la longuitud del array lin.
    lid : int
        DESCRIPTION.

    Returns
    -------
    None.

    """
    
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
def quitarpersonaje(lista_aliados,lista_enemigos,personaje,lista_personajes):
    """
    La funcion elimina a un personaje de las listas

    Parameters
    ----------
    lista_aliados : Array 
        Es un array de objetos tipo aliados.
    lista_enemigos : Array
        Es un array de objetos tipo enemigos.
    personaje : Objeto personaje
        Es el personaje que vamos a quitas.
    lista_personajes : Array
        Es la lista de personajes ordenados.

    Returns
    -------
    None.

    """
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
            print(i.name,"\t\tDano acumulado:",i.danoacumulado)           
def atacar(lista,n):
    n=0
    print("¿A quien atacas?")
    for i in lista:
        print(n,".",i.name)
        n+=1
    victima=int(input())
   
    print("Atacas a",lista[victima].name)
    print("¿Cuanta vida le quitas?")
    dano=int(input())
    if lista[victima].tipo==0:
        lista[victima].atacar(dano)
    else:
        lista[victima].anadirdano(dano)
def anadir_aliado():
    print("Nombre del aliado:")
    name=input()
    print("Cuanta iniciativa:")
    iniciativa=int(input())
    print("Cuanta vida maxima")
    vida=int(input())
    pn=c.aliado(iniciativa,name,vida)
def anadir_enemigo():
    print("Nombre:")
    name=input()
    print("Iniciativa:")
    iniciativa=int(input())
    pe=c.enemigo(iniciativa,name)
def ciclo(lista_personajes,lista_de_iniciativa):
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
    jpg=[]
    for i in lista_personajes:
        names.append(i.name)
        inicias.append(i.iniciativa)
        jpg.append(i.jpg)
        if i.tipo == 1:
            tipos.append(1)
            pain.append(i.danoacumulado)
        else:
            tipos.append(0)
            pain.append(i.vida)
        
    data = {'Name': names,
            'Iniciativa': inicias,
            'tipo':tipos,
            'PS':pain,
            'jpg':jpg}
        
        
    df = pd.DataFrame(data,columns =['Name','Iniciativa','tipo','PS','jpg'])
    df.to_csv('Partida.csv')
def Cargar():
    c.lista_personajes=[]
    df=pd.read_csv('Partida.csv')
    names = df['Name']
    inicias = df['Iniciativa']
    tipo = df['tipo']
    ps = df['PS']
    img = df['jpg']
    for i in range (len(names)):
        if tipo[i] == 0:#aliado
            p1=c.aliado(inicias[i],names[i],ps[i])
            p1.ponerImagen(img[i])
        else:
            p1=c.enemigo(inicias[i],names[i],ps[i])
            p1.ponerImagen(img[i])

            # p2.danoacumulado=ps[i]
def cargarequipo(lista):
        

    df=pd.read_csv('Tormenta.csv')
    names = df['Name']
    inicias = df['Iniciativa']
    tipo = df['tipo']
    ps = df['PS']
    img = df['jpg']
    for i in range (len(names)):
        if tipo[i] == 0:#aliado
            p1=c.aliado(inicias[i],names[i],ps[i])
            p1.ponerImagen(img[i])

        else:
            
            p1=c.enemigo(inicias[i],names[i],ps[i])
            p1.ponerImagen(img[i])

            # p2.danoacumulado=ps[i]
        lista.append(p1)
def buscarnombreobjetivo(lista,name,rep):
    # HAY QUE PONER PARA ENCUENTRE LA REPETICCION PARA ELLO SOLO DEBEMOS AÑADIR UN AND EN EL IF Y GUARDAR LA REP DEL OBJETIVO EN EL CODIGO PRINCIPAL
    p=0
    for i in lista:
        if name == i.name and rep==i.rep:
            return p
        p+=1
def RedimensionarCarpetaFotos(direccion,dimension,direccion_destino):
    
    lista=os.listdir(direccion)
    for i in lista:
        img=Image.open(direccion+i)
        new=img.resize((dimension,dimension))
        new.save(direccion_destino+i,'png')
def saberRepeticion(lista,nombre):
    repe=True
    lista_nombres=[]
    aux=nombre
    aux2=aux
    y=0
    for i in lista:
        lista_nombres.append(i.name+i.rep)
        print(i.name+i.rep)
    while repe:
        if aux2 in lista_nombres:
            y=1+y
            aux2=aux+str(y)
        else:
            repe=False
    if y==0:
        return ""
    return str(y)
            
            
# def menu(lista_personajes,lista_de_iniciativa,lista_aliados,lista_enemigos):
    
#     imprimirlista(lista_personajes)
#     print("¿Que quieres hacer?")
#     print("1.Atacar")
#     print("2.Anadir aliado")
#     print("3.Anadir enemigo")
#     print("4.Quitar aliado")
#     print("5.Pasar turno")
#     print("6.Guardar")
#     print("7.Cargar")
#     print("0.Salir")
#     a=int((input()))
#     if a==0:
#         return True
#     # if a==1:
#     #     atacar(lista_personajes)
#     #     return menu(lista_personajes,lista_de_iniciativa,lista_aliados,lista_enemigos)
#     if a==2:
#         anadir_aliado()
#         ciclo(lista_personajes,lista_de_iniciativa)
#         return menu(lista_personajes,lista_de_iniciativa,lista_aliados,lista_enemigos)
#     if a==3:
#         anadir_enemigo()
#         ciclo(lista_personajes,lista_de_iniciativa)
#         return menu(lista_personajes,lista_de_iniciativa,lista_aliados,lista_enemigos)
#     if a==4:
#         eliminar(lista_aliados,lista_enemigos,lista_personajes)
#         return menu(lista_personajes,lista_de_iniciativa,lista_aliados,lista_enemigos)
#     if a==5:
#         pasar_turno(lista_personajes)
#         return menu(lista_personajes,lista_de_iniciativa,lista_aliados,lista_enemigos)
#     if a==6:
#         Guardar(lista_personajes)
#         return menu(lista_personajes,lista_de_iniciativa,lista_aliados,lista_enemigos)
#     if a ==7:
#         Cargar()
#         return menu(lista_personajes,lista_de_iniciativa,lista_aliados,lista_enemigos)
# # lista_personajes=[]
# # lista_de_iniciativa=[]
# # lista_aliados=[]
# # lista_enemigos=[]
# # menu(lista_personajes,lista_de_iniciativa,lista_aliados,lista_enemigos)