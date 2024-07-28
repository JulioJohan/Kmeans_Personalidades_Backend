from pydantic import BaseModel


class RespuestaBase(BaseModel):
    id: int
    extrovertido:int
    introvertido:int
    intuicion:int
    sentido:int
    pensamiento:int
    sentimiento:int
    juicio:int
    percepcion:int

class Respuesta(RespuestaBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True