# Para manejar la conexión a la base de datos SQLite3
# y realizar las operaciones de inserción, actualización y eliminación de datos
# en la tabla de usuarios

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker