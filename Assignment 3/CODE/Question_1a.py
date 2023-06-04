import pandas as pd
import numpy as np

df = []
def Expected(m0,me,l):
    m = m0
    while m != me:
        E = float(m)*(round((1.0/4.0)**float(l), 8))
        df.append([m, E])
        m*=10
    return df
        
def log_df(df):
    df = pd.DataFrame(df, columns=['m', 'E-value/n'])
    df['log10(E-value/n)'] = np.log10(df['E-value/n'])
    print(df)




##### EXECUTION
m0=10
me=1000000000000000
l=10

df = Expected(m0,me,l)
log_df(df)
