from sqlalchemy import create_engine, MetaData

# UrlBD Mysql
engine = create_engine("mysql+pymysql://root:password@localhost:3306/nombreBD")

conexion = engine.connect()



