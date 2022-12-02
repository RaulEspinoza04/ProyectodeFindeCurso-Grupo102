from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .declarative_base import Base

class Asignatura(Base):
    __tablename__ = 'asignatura'

    IDAsignatura = Column(Integer, primary_key=True)
    NombreA = Column(String(30))
    creditosA = Column(Integer)
    docentes = relationship('Docente', secondary='asignatura_docente')
    estudiantes = relationship('Estudiante', secondary='asignatura_estudiante')


class AsignaturaDocente(Base):
    __tablename__ = 'asignatura_docente'

    asignatura_IDAsignatura = Column(
        Integer,
        ForeignKey('asignatura.IDAsignatura'),
        primary_key=True)

    docente_IDDocente = Column(
        Integer,
        ForeignKey('docente.IDDocente'),
        primary_key=True)


class AsignaturaEstudiante(Base):
    __tablename__ = 'asignatura_estudiante'

    asignatura_IDAsignatura = Column(
        Integer,
        ForeignKey('asignatura.IDAsignatura'),
        primary_key=True)

    estudiante_IDEstudiante = Column(
        Integer,
        ForeignKey('estudiante.IDEstudiante'),
        primary_key=True)
