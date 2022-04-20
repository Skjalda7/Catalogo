import numpy as np
import pandas as pd

df_a = pd.read_csv("datasets/amazon.csv")
df_d = pd.read_csv("datasets/disney.csv")
df_n = pd.read_csv("datasets/netflix.csv")

# saco la columna 'show_id'
df_aa = df_a.drop(['show_id'], axis=1)
df_dd = df_d.drop(['show_id'], axis=1)
df_nn = df_n.drop(['show_id'], axis=1)

# cambio el nombre de una columna
amazon = df_aa.rename({'listed_in': 'genre'}, axis=1)
disney = df_dd.rename({'listed_in': 'genre'}, axis=1)
netflix = df_nn.rename({'listed_in': 'genre'}, axis=1)

# juntar los 3 csv, previamente agregar la columna en cada csv con el nombre de la plataforma
ama=amazon.assign(plataforma='Amazon Prime Video')
dis=disney.assign(plataforma='Disney+')
net=netflix.assign(plataforma='Netflix')

# unis los 3 df juntos en uno solo, luego borras la columna 'date_added' porque te colgaste de hacerlo antes
bbdd_1=pd.concat([ama, dis, net], axis=0)
bbdd1=bbdd_1.drop(['date_added'], axis=1)

# reemplazar los null por '-'
bbdd=bbdd1.replace([np.nan], '-')

