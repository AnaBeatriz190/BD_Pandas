#Obtenha uma visão geral rápida imprimindo as primeiras 10 linhas do DataFrame

import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))