from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


from config.database import Base


class Respuesta(Base):
    __tablename__ = "respuesta"

    id = Column(Integer, primary_key=True)
    extrovertido = Column(Integer)
    introvertido = Column(Integer)
    intuicion = Column(Integer)
    sentido = Column(Integer)
    pensamiento = Column(Integer)
    sentimiento = Column(Integer)
    juicio = Column(Integer)
    percepcion = Column(Integer)


