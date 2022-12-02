from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .declarative_base import Base


class Asignatura(Base):
    __tablename__ = 'asignatura'

    id = Column(Integer, primary_key=True)
    NombreA = Column(String(30))
    creditosA = Column(Integer)
    docentes = relationship('Docente', secondary='asignatura_docente')
    estudiantes = relationship('Estudiante', secondary='asignatura_estudiante')

class AsignaturaDocente(Base):
    __tablename__ = 'asignatura_docente'

    asignatura_id = Column(
        Integer,
        ForeignKey('Asignatura.id'),
        primary_key=True)
    docente_id = Column(
        Integer,
        ForeignKey('Docente.id'),
        primary_key=True)

class AsignaturaEstudiante(Base):
    __tablename__ = 'asignatura_estudiante'

    asignatura_id = Column(
        Integer,
        ForeignKey('asignatura.id'),
        primary_key=True)

    estudiante_id = Column(
        Integer,
        ForeignKey('estudiante.id'),
        primary_key=True)





