# ProblemSet 1 : Question 1
# Jisoo Kim A15638045
import pandas as pd
import math

def get_diNuc(nuc):
    dinuc = []
    for first in nuc:
        for second in nuc:
            dinuc.append(first + second)
    return dinuc

def getFreq(infile):
    nuc  = ['A', 'T', 'C', 'G']
    dinuc = get_diNuc(nuc)

    difreq = {}
    for n in dinuc:
        difreq[n] = [0, 0]

    freq ={}

    inf = open(infile, 'r')
    data = inf.readlines()
    inf.close()
    total_di = 0
    N = 0
    for d in data:
        if '>' in d:
            continue
        else:
            #print(d)
            d = d.strip()
            for n in dinuc:
                n_ct = d.count(n)
                difreq[n][-1] = difreq[n][-1]+n_ct
                total_di+= n_ct

            N+=len(d)
            for mono in nuc:
                if mono in freq:
                    freq[mono] = freq[mono] + d.count(mono)
                else:
                    freq[mono] = d.count(mono)

    for f in freq:
        freq[f] = freq[f]/N
    for df in difreq:
        difreq[df][0] = round(freq[df[0]] * freq[df[1]],4)
    
    final = pd.DataFrame.from_dict(difreq, orient='index', columns = ['Expected', 'Observed'])
    final['Observed'] = round(final['Observed']/total_di,4)
    final['Diff'] = final['Observed']-final['Expected']
    return final

#### 
FreqTable = getFreq('chrA.fasta')
print(FreqTable)

