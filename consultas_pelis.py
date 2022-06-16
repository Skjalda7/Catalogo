import pandas as pd
import psycopg2

# Establezco conexion
conexion1 = psycopg2.connect(database="pelis", user="postgres", password="password")

# Genero el cursor
try:
    with conexion1.cursor() as cursor:
        consulta = "SELECT genre, title, rating FROM catalogo"
        cursor.execute(consulta)
        # Con fetchall traemos todas las filas
        peliculas = cursor.fetchall() # Aca almaceno toda la columna dentro de la variable 'peliculas'
except psycopg2.Error as e:
    print("NOPE: ", e)
finally:
    conexion1.close()

db=pd.DataFrame(peliculas) # Tomo la variable peliculas y la paso a df, para poder manipular mejor la busqueda
# PERO EL DF NO MANTIENE EL NOMBRE DE LAS COLUMNAS AYUDA


busqueda = input("Casting buscado: ")





'''' el método read_sql por defecto lee únicamente el método connect de sqlalchemy'''
''' Además los modelos los creaste con SQL alchemy por lo que lo ideal es que sigas con esa metodología'''

''' algo que podrías realizar paraque la query funcione respecto a la búsqueda es crear un f string asi: '''

Query = f'SELECT * FROM CATALOGO WHERE CASTING = {busqueda}'




# --------------------------------------

# SI USO ESTE METODO, LA QUERY ME DEVUELVE LA LISTA DE COLUMNAS, NO LOS VALORES
#from sqlalchemy import create_engine
#import pandas as pd

#conexion = create_engine('postgresql://postgres:password@localhost/pelis')

#busqueda = input("Casting buscado: ")
#query = "SELECT * FROM catalogo"
#data=pd.read_sql(query, conexion)
#for d in data:
#    print(d)
