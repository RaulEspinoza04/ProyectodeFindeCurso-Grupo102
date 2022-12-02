#H004
# H005
from src.modelo.asignatura import Asignatura
from src.modelo.docente import Docente
from src.modelo.estudiante import Estudiante
from src.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
    # Crea la BD
    Base.metadata.create_all(engine)
    # Abre la session
    session = Session()
    session.commit()
    session.close()