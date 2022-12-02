from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .declarative_base import Base


class Docente(Base):
    __tablename__ = 'docente'

    id = Column(Integer, primary_key=True)
    NombresD = Column(String(30))
    ApellidoPaternoD = Column(String(30))
    ApellidoMaternoD = Column(String(30))
    ContrasenaD = Column(String(15))
    asignaturas = relationship('Asignatura', secondary='asignatura_docente')

