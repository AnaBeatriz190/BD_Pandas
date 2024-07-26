#Carregue o CSV em um DataFrame

import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string()) 