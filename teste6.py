#Imprima as primeiras 5 linhas do DataFrame

import pandas as pd

df = pd.read_csv('data.csv')

print(df.head())