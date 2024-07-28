from fastapi import FastAPI
from typing import Union
# from config.database import conexion

#import routes
from routes.user import user
from routes.kmeans import kmeans
from routes.ejemplo_kmeans import ejemplo_kmeans

#Instalar dependencias en python
#python3 -m venv venv o python -m venv venv

#Entrar a las dependecias de python:
#source venv/bin/activate


#Ejecutar para que configurar donde descarga las dependencias
# pip3 config set global.trusted-host "pypi.org files.pythonhosted.org pypi.python.org" --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org

#instalar todas las dependencias 
#pip install -r requirements.txt

#inciar la aplicacion
#uvicorn main:app --reload
app = FastAPI()


app.include_router(user.router)
app.include_router(kmeans.router)
app.include_router(ejemplo_kmeans.router)

@app.get('/')
async def read_root():
    return {'Probando':'world'}


@app.get('/items/{item_id}')
async def read_item(item_id: int,q: Union[str, None] = None):
    return {'item_id':item_id,'q':q}