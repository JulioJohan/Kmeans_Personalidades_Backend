#Librerias api
from fastapi import APIRouter,Response,HTTPException,status
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns


router = APIRouter(prefix="/kmeans",
                   tags=["kmeans"],
                   responses={status.HTTP_404_NOT_FOUND:{"message": "No encontrado"}})


# @router.post('/entrenamiento')
# async def entrenamiento():
#     return {'kmeans':'entrenamiento'}        

@router.post('/entrenamiento')
async def read_file_csv():

   


   #  datos =  pd.read_csv('files/datos_personalidades.csv')

   #  # Inicializa el escalador
   #  scaler = StandardScaler()

   #  # Ajusta y transforma los datos numéricos
   #  estandarizacion = scaler.fit_transform(datos)

   #  # El resultado tendrá media 0 y desviación estándar 1 solo para las columnas numéricas
   #  print(estandarizacion)

   #  #Normalizacion de los varoles - Para que se encuentren dentro del mismo rango
   #  datos_normalizados = (datos - datos.min()) / (datos.max() - datos.min())
   #  datos_normalizados


   #  #Aplicando el modelo a los datos

   #  #Crea el modelo
   #  clustering = KMeans(n_clusters=4, max_iter = 1000)

   #  #Aplica el modelo solo a los datos numéricos
   #  clustering.fit(datos_normalizados)

   #  #Agregando la clasificacion al archivo original 

   #  datos['KMeans_Cluster'] = clustering.labels_    #Los resultados del clustering se guardan en labels_ dentro del modelo
   #  datos.head()

   #  return Response("Hola")


#Entrenamiento de modelo
   X = datos.loc[:,['extrovertido','introvertido','intuicion','sentido','pensamiento','sentimiento','juicio','percepcion']]
   #El numero de clusters son todos los posibles grupos que son
   modelo = KMeans(n_clusters = 4)
   #Prediccion del modelo
   predicciones = modelo.fit_predict(X)
   print(predicciones)

   X['personalidad_mbti'] = predicciones
   print('Cantidad de personas por personalidad')
   print(X['personalidad_mbti'].value_counts())

   #Representacion de los resultados en grafica
   

   return Response( 'Hola' )