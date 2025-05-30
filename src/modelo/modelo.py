from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.modelo.declarative_base import Base

class Alumno(Base):
    __tablename__ = 'alumnos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    cursos = relationship("Curso", back_populates="alumno", cascade="all, delete-orphan")


class Curso(Base):
    __tablename__ = 'cursos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    alumno_id = Column(Integer, ForeignKey('alumnos.id'))
    alumno = relationship("Alumno", back_populates="cursos")