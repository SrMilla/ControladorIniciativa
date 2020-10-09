# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 19:31:17 2020

@author: rawre
"""
import os 
import pandas as pd
##Charge kind state and attacks#####
df = pd.read_excel("ESTADOS.xlsx", header= None)
state1=[]
state2=[]
tipe_attack=[]
for i in range(10):
    state1.append(df[0][i])
for i in range(13):
    tipe_attack.append(df[1][i])
for i in range (14):
    state2.append(df[2][i])
dir="./Tokens/"
p=os.listdir(dir)
lista_nombres_npcs=[]
# print(p[303])
for i in p:
    # lista_nombres_npcs.append(i.strip(".png"))
        lista_nombres_npcs.append(i[:len(i)-4])

# print(lista_nombres_npcs[303])
abc=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
abcmin=[]
dic_npc={}
for i in abc:
    dic_npc[i]=[]
    for j in lista_nombres_npcs:
        if j.startswith(i):
            # print(j+"empieza por"+i)
            dic_npc[i].append(j)
p="t"+""+"r"
# print(dic_npc[1])
# abc=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# print(p[0].strip(".png"))