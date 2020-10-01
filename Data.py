# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 19:31:17 2020

@author: rawre
"""
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
