# Para manejar la conexión a la base de datos SQLite3
# y realizar las operaciones de inserción, actualización y eliminación de datos
# en la tabla de usuarios

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from database import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
 
class User(Base):
    __tablename__ = "users"
 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    email = Column(String(50), unique=True, index=True)
 
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
 
#Para manejar la conexion SQLite
 
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
DATABASE_URL = "sqlite:///./test.db"
 
# Crear el motor de conexion de la base de datos.
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
 
# Crear una sesion
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
# Definir la base
Base = declarative_base()
 
#Validar los datos
 
from pydantic import BaseModel
 
class UserBase(BaseModel):
    name: str
    email: str
 
class UserCreate(UserBase):
    pass
 
class UserResponse(UserBase):
    id: int
 
    class Config:
        from_attributes = True
 