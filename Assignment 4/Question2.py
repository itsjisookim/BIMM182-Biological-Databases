# ProblemSet 1 : Question 2
# Jisoo Kim A15638045
import pandas as pd
import math
from decimal import *

def get_diNuc(nuc):
    dinuc = []
    for first in nuc:
        for second in nuc:
            dinuc.append(first + second)
    return dinuc

def Markov(S): #get markov chain by calculating frequency
    nuc  = ['A', 'T', 'C', 'G']
    dinuc = get_diNuc(nuc)

    difreq = {}
    for n in dinuc:
        difreq[n] = [0]

    total_di = 0

    for n in dinuc:
        n_ct = S.count(n)
        difreq[n][0] = difreq[n][0]+n_ct
        total_di+= n_ct
    '''
    for mono in nuc:
        if mono in freq:
            freq[mono] = freq[mono] + S.count(mono)
        else:
            freq[mono] = S.count(mono)
    '''   
    final = pd.DataFrame.from_dict(difreq, orient='index', columns = ['Observed'])
    final['Observed'] = final['Observed']/total_di
    #final['Diff'] = final['Observed']-final['Expected']
    #print(final)
    return final

def get_CpG(seq, islands):
    inf = open(seq, 'r')
    data = inf.readlines()
    inf.close()
    S =''
    for d in data:
        if '>' in d:
            continue
        else:
            #print(d)
            d = d.strip()
            S += d

    inf = open(islands, 'r')
    data = inf.readlines()
    inf.close()
    Islands = []
    start = 0
    CPG = S
    non_CPG = ''
    ct = 0
    for d in data:
        interval = d.split()
        interval = [int(p) for p in interval]
        ct+=1
        Islands.append(interval)
        non_CPG += S[start:interval[0]]
        CPG += S[interval[0]:interval[-1]]
        start = interval[-1]
        if len(data) == ct and interval[-1] != len(S):
            non_CPG+= S[interval[-1]:]
    
    return S, CPG, non_CPG, Islands

def CpGpotential(S, Islands, CPG_HMM, non_CPG_HMM, outfile):
    start = 0
    FINAL = []
    out = open(outfile, 'w')
    for i in Islands:
        if start != i[0]: ##when there is gap between previous cpg interval (non_cpg region)
            P_CPG = Decimal(1.0)
            P_non_CPG = Decimal(1.0)
            s = S[start:i[0]]
            for j in range(len(s)-1):
                P_CPG = P_CPG * Decimal(CPG_HMM['Observed'].loc[s[j:j+2]])
                P_non_CPG = P_non_CPG * Decimal(non_CPG_HMM['Observed'].loc[s[j:j+2]])
            potential = P_CPG - P_non_CPG 
            if potential > 0: #non_cpg site
                stat='false postive'
            else:
                stat='true negative'
            line = [str(x) for x in [start, i[0], P_CPG, P_non_CPG, potential, stat]]
            FINAL.append(line)
            temp = [str(x) for x in [start, i[0], stat]]
            out.write('\t'.join(temp)+ '\n')

        ## CPG interval
        P_CPG = Decimal(1.0)
        P_non_CPG = Decimal(1.0)
        s = S[i[0]:i[-1]]
        for j in range(len(s)-1):
            P_CPG = P_CPG * Decimal(CPG_HMM['Observed'].loc[s[j:j+2]])
            P_non_CPG = P_non_CPG * Decimal(non_CPG_HMM['Observed'].loc[s[j:j+2]]) 
        potential = P_CPG - P_non_CPG 
        if potential >= 0: #non_cpg site
            stat='true postive'
        else:
            stat='false negative'
        line = [str(x) for x in [i[0], i[-1], P_CPG, P_non_CPG, potential, stat]]
        FINAL.append(line)
        temp = [str(x) for x in [start, i[0], stat]]
        out.write('\t'.join(temp)+ '\n')
        start=i[-1] #relocate pointer

        if i[-1] == len(S): #when there is non_cpg region on the edge
            P_CPG = Decimal(1.0)
            P_non_CPG = Decimal(1.0)
            s = S[i[-1]:]
            for j in range(len(s)-1):
                P_CPG = P_CPG * Decimal(CPG_HMM['Observed'].loc[s[j:j+2]])
                P_non_CPG = P_non_CPG * Decimal(non_CPG_HMM['Observed'].loc[s[j:j+2]])
            potential = P_CPG - P_non_CPG 
            if potential > 0: #non_cpg site
                stat='false postive'
            else:
                stat='true negative'
            line = [str(x) for x in [i[-1], len(S), P_CPG, P_non_CPG, potential, stat]]
            FINAL.append(line)
            temp = [str(x) for x in [start, i[0], stat]]
            out.write('\t'.join(temp) + '\n')
    out.close()
    df = pd.DataFrame(FINAL, columns=['Start', 'End', 'P(CPG)', 'P(nonCPG)', 'CPG Potential', 'stat'])
    #df = pd.DataFrame(FINAL, columns=['Start', 'End', 'CPG Potential '])
    df.to_csv(outfile.replace('txt', 'csv'))






#### 
S, CPG, non_CPG, Islands = get_CpG('chrA.fasta', 'chrA.islands')
CPG_HMM = Markov(CPG)
non_CPG_HMM = Markov(non_CPG)
CpGpotential(S, Islands, CPG_HMM, non_CPG_HMM, 'CPG_stat.txt')
