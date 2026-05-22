#la conexion a la base de datos
#este archivo es el responsable de conectar a la base de datos y ejecutar las consultas
#MySQL usando SQLalchemy como nuestro orm (objet relational mapping)
#convierte tablas datos de mysql a clases pythyon
#tres conceptos claves 
#1. engine: es el objeto que se encarga de conectar a la base de datos y ejecutar las consultas
#2. session: es el objeto que se encarga de manejar las transacciones y consultas a la base de datos
#3. base: es el objeto que se encarga de definir las tablas y clases de la base de datos heredan modelos ORM

import os
from dotenv import load_dotenv 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#cargar las variables de entorno
load_dotenv()
#esto evita tener que  escribir las variables directamente en el codigo y asi mantenerlas seguras
#esta es la cadena de conexion a la base de datos, se construye a partir de las variables de entorno
DATABASE_URL = (f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT', '3306')}/{os.getenv('DB_NAME')}")

#crear el engine de sqlalchemy
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
#pool_pre_ping=True es una opcion que permite verificar si la conexion a la base de datos esta activa antes de ejecutar una consulta, esto ayuda a evitar errores de conexion
#crear la sessionmaker, que es una fabrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
#autocommit=False significa que las transacciones no se confirmaran automaticamente, 
# esto nos da control sobre cuando confirmar

#crear la base declarativa, que es la clase base para los modelos ORM
Base = declarative_base() 
#utilizamos un genrador que provee una sesion de DB a cada endpoint de fastapi get_db 
def get_db():
    db = SessionLocal()
    try:
        yield db #entrega la sesion de DB al endpoint, el endpoint puede usar esta sesion para ejecutar consultas a la base de datos
    finally:
        db.close()