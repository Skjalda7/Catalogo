import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:password@localhost/pelis')
engine.connect()

''''el método read_sql por defecto lee únicamente el método connect de
sqlalchemy
Además los modelos los creaste con SQL alchemy por lo que lo ideal es que sigas
con esa metodología, algo que podrías realizar paraque la query funcione
respecto a la búsqueda es crear un f string asi: '''

# Esto ya crea un dataframe con éste método
db = pd.read_sql_table('catalogo', con=engine.connect())
busqueda = input("Casting buscado: ")
#  aplico el fstring mencionado anteriormente
query = f'SELECT * FROM CATALOGO WHERE CASTING={busqueda}'
# creo un df con la consulta
df = pd.read_sql_query(query, con=engine.connect())
print(df.head())
