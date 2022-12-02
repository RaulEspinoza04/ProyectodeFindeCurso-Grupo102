from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .declarative_base import Base


class Estudiante(Base):
    __tablename__ = 'estudiante'

    IDEstudiante = Column(Integer, primary_key=True)
    NombresE = Column(String(30))
    ApellidoPaternoE = Column(String(30))
    ApellidoMaternoE = Column(String(30))
    ContrasenaE = Column(String(15))
    Asignaturas = relationship('Asignatura', secondary='asignatura_estudiante')