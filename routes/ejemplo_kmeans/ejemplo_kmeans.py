
#Librerias api
from fastapi import APIRouter,Response,HTTPException,status
#IA
import pandas
#graficas
import seaborn
import matplotlib.pyplot as plt
#retorna una grafica
from io import BytesIO

from sklearn.cluster import KMeans



router = APIRouter(prefix='/ejemplo_kmeans',
                    tags=['ejemplo_kmeans'],
                    responses = {status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

@router.post('/read_file_csv')
async def read_file_csv():
   datos =  pandas.read_csv('files/U5_02_housing.csv')
   print(datos.head())

   #Se leen los datos para el analisis de posibles caracteristicas
   grafica_uno = seaborn.scatterplot(x='latitude',y='longitude',
                                    data = datos,hue='median_house_value',palette="coolwarm")
   

   average_income = seaborn.scatterplot(x='latitude',y='longitude',data = datos,
                                       hue='median_income',palette="coolwarm",
                                       s = datos["median_income"].mean())


   #Entrenamiento de modelo
   X = datos.loc[:,['latitude','longitude','median_income']]
   #El numero de clusters son todos los posibles grupos que son
   modelo = KMeans(n_clusters = 6)
   #Prediccion del modelo
   predicciones = modelo.fit_predict(X)
   print(predicciones)
   X['segmento_economico'] = predicciones
   print('Cantidad de personas por segmento economico')
   print(X['segmento_economico'].value_counts())

   #Representacion de los resultados en graficas
   grafica_segmento_economico = seaborn.scatterplot(x='latitude',y='longitude',data=X, 
               hue="segmento_economico",palette="bright")
   

   return Response( media_type='image/png')


