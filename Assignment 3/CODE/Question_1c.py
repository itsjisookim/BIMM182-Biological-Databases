import pandas as pd
import numpy as np

def l_mer(query, l):
    l_mers=[]
    for i in range(len(query)-l+1):
        l_mers.append(query[i:i+l])
    return l_mers

def Expected(m, query, l, n):
    #C,G = 0.4
    #A,T = 0.1
    
    Total_P = 0.0
    l_mers = l_mer(query, l)
    for i in l_mers:
        P = 1.0
        for j in range(len(i)):
            if query[j] == 'C' or query[j] == 'G':
                P=P*0.4
            else:
                P=P*0.1
        Total_P+=P

    print(round(Total_P*n,5))



##### EXECUTION
query = "AATAAGCCGC"
m = 10
l = 5
n=0
inf = open('DNA.txt', 'r')
data = inf.readlines()
for d in data:
    if '>' in d:
        continue
    else:
        n = n+len(d.strip())
inf.close()
Expected(m, query, l, n)


