# -*- coding: utf-8 -*-
import Clases as c
import pandas as pd
def pasar_turno(lista):
    aux=lista[0]
    k=len(lista)
    for i in range(k-1):
        lista[i]=lista[i+1]
    lista[k-1]=aux
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
            print(i.name,"\t\tDaño acumulado:",i.danoacumulado)           
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
    pn=c.aliado(iniciativa,name,vida)
def añadir_enemigo():
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
    for i in lista_personajes:
        names.append(i.name)
        inicias.append(i.iniciativa)
        if i.tipo == 1:
            tipos.append(1)
            pain.append(i.danoacumulado)
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
    c.lista_personajes=[]
    df=pd.read_csv('Partida.csv')
    names = df['Name']
    inicias = df['Iniciativa']
    tipo = df['tipo']
    ps = df['PS']
    for i in range (len(names)):
        if tipo[i] == 0:#aliado
            p1=c.aliado(inicias[i],names[i],ps[i])
        else:
            p2=c.enemigo(inicias[i],names[i])
            p2.danoacumulado=ps[i]
def menu(lista_personajes,lista_de_iniciativa,lista_aliados,lista_enemigos):
    
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
        return menu(lista_personajes,lista_de_iniciativa,lista_aliados,lista_enemigos)
    if a==2:
        añadir_aliado()
        ciclo(lista_personajes,lista_de_iniciativa)
        return menu(lista_personajes,lista_de_iniciativa,lista_aliados,lista_enemigos)
    if a==3:
        añadir_enemigo()
        ciclo(lista_personajes,lista_de_iniciativa)
        return menu(lista_personajes,lista_de_iniciativa,lista_aliados,lista_enemigos)
    if a==4:
        eliminar(lista_aliados,lista_enemigos,lista_personajes)
        return menu(lista_personajes,lista_de_iniciativa,lista_aliados,lista_enemigos)
    if a==5:
        pasar_turno(lista_personajes)
        return menu(lista_personajes,lista_de_iniciativa,lista_aliados,lista_enemigos)
    if a==6:
        Guardar(lista_personajes)
        return menu(lista_personajes,lista_de_iniciativa,lista_aliados,lista_enemigos)
    if a ==7:
        Cargar()
        return menu(lista_personajes,lista_de_iniciativa,lista_aliados,lista_enemigos)

