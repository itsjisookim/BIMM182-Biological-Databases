import pandas as pd

def speedUp(ls, n, m, r):
    tab = []
    for l in ls:
        sup = (4**float(l))/(2*(r**2))
        e = 1-0.85
        sensitivity = 1-(1-(1-e)**l)**(r-l+1)
        tab.append([l, sup, sensitivity])
    
    df = pd.DataFrame(tab, columns=['l', 'Speed Up', 'Sensitivity'])
    print(df)


ls = [5,11,15,20,25,30,35,40]
n = 10**7
m = 10**7
r = 100
speedUp(ls,n,m,r)