import pandas as pd
#1
# x = pd.read_excel("pessoas.xlsx", usecols=[10, 11])

#2
x = pd.read_excel("pessoas.xlsx", usecols=['Dado1', 'Dado2'])
#oi = pd.read_excel("oi.xlsx", usecols=[10])
print(x)
