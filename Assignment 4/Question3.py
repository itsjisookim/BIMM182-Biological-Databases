# ProblemSet 2 : Question 1
# Jisoo Kim A15638045

import pandas as pd
import numpy as np

def ISOtable(atom):
    abundance = {
            'C': [98.93, 1.07], # C-12,13
            'H' : [99.9885, 0.0151], # H-1,2
            'O' : [99.757, 0.038, 0.205], # O-16,17,18
            'N' : [99.632, 0.368], # N-14,15
            'S' : [94.93, 0.76, 4.29]# S-32,33,34
    }
    #df = pd.DataFrame.from_dict(abundance, orient='index', columns=['abunance'])
    #print(df)
    return abundance[atom]

def AminoFormula(sym):
    #inorder of C, H, N, O, S
    order = ['C', 'H', 'N', 'O', 'S']
    amino = {'S': [3,7,1,3,0],
             'L': [6,13,1,2,0],
             'A': [3,7,1,2,0],
             'M': [5,11,1,2,1],
             'E': [5,9,1,4,0],
             'R' : [6,14,4,2,0]}

    return amino[sym], order

def ISOprofile(peptide):
    order = []
    formula = []
    for i in peptide:
        temp, order = AminoFormula(i)
        if len(formula) != len(temp):
            formula = temp
        else:
            formula = [a+b for a, b in zip(formula, temp)]
    print(order)
    print("formula : %s"%(formula))

    final = 1.0
    for j in range(len(formula)):
        abundance = ISOtable(order[j])
        #print(order[j], formula[j], abundance)
        coeff = [0 if a<0.1 else a/100 for a in abundance] #remove any abundance <0.1% while still being a placeholder for the polynomial
        '''
        while len(coeff) != 0:
            if coeff[0] == 0:
                coeff = coeff.pop(0)
            else:
                break
        '''
        p = np.poly1d(coeff[::-1])
        print(order[j], len(p**formula[j]))
        if order[j] == 'S':
            print(np.poly1d(p**formula[j]))
        final = final*(p**formula[j])

    
    FINAL_coeff = list(final)[::-1]
    df = pd.DataFrame(FINAL_coeff, columns = ['Peak Coefficient'])
    df.to_csv(peptide+'_isotopeProfile.csv')
    return df
    

####
ISOprofile('SLAMMER')
#p = np.poly1d([1, 2, 3])
#print(np.poly1d(p))