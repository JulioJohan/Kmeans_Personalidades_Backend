
from fastapi import APIRouter,Response,HTTPException,status,Depends


from sqlalchemy.orm import Session

from models import respuesta , respuesta_schema

from config.database import SessionLocal


#libreria kmeans y libreria ppara las imagenes 
import pandas
import seaborn
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from io import BytesIO
from sklearn.decomposition import PCA
import base64





router = APIRouter(prefix='/dbscan',
                    tags=['dbscan'],
                    responses = {status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/entrenamiento')
async def get_all(db: Session = Depends(get_db), skip: int = 0 ,limit: int = 1000):
    data_mysql = db.query(respuesta.Respuesta).offset(skip).limit(limit).all()
    # Supongamos que tienes una lista de objetos llamada `data`
    # Vamos a convertir cada objeto a un diccionario
    data_dicts = [obj.__dict__ for obj in data_mysql]
        
    data = pandas.DataFrame(data_dicts)

    #Eliminar la columand id y _sa_instance_state 
    dataframe_limpio = data.drop(columns=['id','_sa_instance_state'])
    print(dataframe_limpio)

    grafico_introvertido_extrovertido = seaborn.scatterplot(x='introvertido', y='extrovertido',
                                       data= dataframe_limpio,palette='coolwarm')
    
    grafico_intuicion_sentimiento = seaborn.scatterplot(x='intuicion', y='sentido',
                                       data= dataframe_limpio,palette='coolwarm')

    grafico_pensamiento_sentimiento = seaborn.scatterplot(x='pensamiento', y='sentimiento',
                                       data= dataframe_limpio,palette='coolwarm')


    grafico_juicio_percepcion = seaborn.scatterplot(x='juicio', y='percepcion',
                                       data= dataframe_limpio,palette='coolwarm')
    

    X = dataframe_limpio.loc[:,['introvertido','extrovertido']]


   


    cluster = DBSCAN(eps=3,min_samples=1).fit_predict(dataframe_limpio)

    
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(dataframe_limpio)

    # Generar el gráfico
    plt.scatter(X_pca[:, 0], X_pca[:, 1])
    plt.title('PCA of dataset')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')

    # Guardar el gráfico en un buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Convertir el contenido del buffer a base64
    grafico_caracteristicas_base_64 = base64.b64encode(buffer.read()).decode('utf-8')

    # Limpiar el gráfico actual
    plt.clf()

    # Ahora tienes el gráfico en base64 que puedes utilizar como quieras
    print(grafico_caracteristicas_base_64)

    response = {
        'excel':'',
        'grafica1':f"data:image/png;base64,{grafico_caracteristicas_base_64}",
        'grafica2':f"data:image/png;base64,{grafico_caracteristicas_base_64}",
    }
    return response
