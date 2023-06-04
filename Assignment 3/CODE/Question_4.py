import pandas as pd
import numpy as np
import sys

def createTrie(query):
    df = dict()
    for q in query:
        curr_dict = df
        for letter in q:
            curr_dict = curr_dict.setdefault(letter, {})
    return df
        
def getQuery(file):
    inf = open(file, 'r')
    data = inf.readlines()
    df = []
    for i in range(len(data)):
        data[i] = data[i].strip()
    df = createTrie(data)
    inf.close()
    return data, df

def getDNA(file):
    inf = open(file, 'r')
    data = inf.readlines()
    DNA =''
    for d in data:
        if '>' in d:
            continue
        else:
            DNA = DNA + d.strip()
    inf.close()
    return DNA

def Eval(query, n):
    stats = {}
    r = len(query)
    for l in query:
        print(l)
        E = round(float(n)*((1.0/4.0)**float(len(l))), 4)
        stats[l] = [E, 0]
    return stats

def AhoCorasick(dictionary, DNA):
    query, Trie = getQuery(dictionary)
    dna = getDNA(DNA)
    stats = Eval(query, len(dna))
    #print(dna)
    
    v = Trie
    l = 0
    c = 0
    align = ''
    
    while l != len(dna):
        #print(dna[c])
        print(v)
        if dna[c] in v: #if successful in transition
            align += dna[c]
            if align in stats:
                stats[align][-1]+=1
                #print(align, stats[align])
                c+=1
                l=c
                v=Trie
                align=''
            else:
                v=v[dna[c]]
                c+=1
        else: #if fail in transition (no failed links)
            c=l+1
            l=c
            v=Trie
            align=''

    df = pd.DataFrame(temp, columns=['l', 'E-value', 'Observed Count'])
    df['Difference'] = df['Observed Count'] - df['E-value']
    conditions = [
    (df['Difference'] > 0) ,
    (df['Difference'] == 0),
    (df['Difference'] < 0)]
    choices = ['greater', 'no change', 'less']
    df['Change'] = np.select(conditions, choices, default='no change')
    df.to_csv('queries.aligned.csv')


###########
try :
    dictionary = 'queries.txt'
    DNA = 'DNA.txt'
    AhoCorasick(dictionary, DNA)
except IndexError as e:
    print(f"{e}")
