# ProblemSet 2 : Question 1
# Jisoo Kim A15638045

import pandas as pd

def ISOtable():
    dict = {'C-12': [0] ,
            'C-13' : [3.125],
            'H-1' : [7.289],
            'O-16' : [-4.737],
            'O-18' : [-0.782],
            'N-14' : [2.863],
            'N-15' : [0.101],
            'S-32' : [-26.016],
            'S-33' : [-26.586],
            'S-34' : [-29.932] }
    df = pd.DataFrame.from_dict(dict, orient='index', columns=['mass'])
    print(df)
    return df

def ISOprofile(peptide):
    return

####
commonISO = ISOtable()
ISOprofile('SLAMMER')