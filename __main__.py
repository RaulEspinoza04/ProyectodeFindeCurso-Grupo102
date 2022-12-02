from src.modelo.asignatura import Asignatura
from src.modelo.docente import Docente
from src.modelo.estudiante import Estudiante
from src.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
    # Crea la BD
    Base.metadata.create_all(engine)
    # Abre la session
    session = Session()
    # crear Docentes
    Docente1 = Docente(NombresD="Samuel Carlos", ApellidoPaternoD="Aquino",
                       ApellidoMaternoD="Torres", ContrasenaD=123456)
    Docente2 = Docente(NombresD="Raul", ApellidoPaternoD="Perez",
                       ApellidoMaternoD="Martinez", ContrasenaD=153456)
    Docente3 = Docente(NombresD="Carlos", ApellidoPaternoD="Lima",
                       ApellidoMaternoD="Rodriguez", ContrasenaD=127856)
    Docente4 = Docente(NombresD="Manuel", ApellidoPaternoD="Aquino",
                       ApellidoMaternoD="Alvarez", ContrasenaD=853456)
    session.add(Docente1)
    session.add(Docente2)
    session.add(Docente3)
    session.add(Docente4)
    session.commit()
    # Crea la BD
    Base.metadata.create_all(engine)
    # Abre la sesion
    session = Session()

    # Crear estudiantes

    Estudiante1 = Estudiante(NombresE="Lorenzo Carlos", ApellidoPaternoE="Quiñonez", ApellidoMaternoE="Quispe",
                             ContrasenaE=753456)
    Estudiante2 = Estudiante(NombresE="Samuel de Luque", ApellidoPaternoE="Manzanarez", ApellidoMaternoE="Dominguez",
                             ContrasenaE=7896456)
    session.add(Estudiante1)
    session.add(Estudiante2)

    # Crear assignaturas
    Asignatura1 = Asignatura(NombreA="MatematicaI", CreditosA=4)
    Asignatura2 = Asignatura(NombreA="Comunicacion", CreditosA=3)
    Asignatura3 = Asignatura(NombreA="Literatura", CreditosA=1)
    session.add(Asignatura1)
    session.add(Asignatura2)
    session.add(Asignatura3)

    # Relacionar docentes con asignaturas
    Docente1.asignaturas = [Asignatura2, Asignatura1]
    Docente2.asignaturas = [Asignatura2, Asignatura3]

    # Relacionar estudiantes con asignaturas
    Estudiante1.asignaturas = [Asignatura2, Asignatura3]
    Estudiante2.asignaturas = [Asignatura2, Asignatura3]
    session.commit()

    session.commit()
    session.close()
