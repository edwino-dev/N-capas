#los CRUD
#el repositorio es el encargado de hacer la conexion con la base de datos
#es el encargado de hacer las operaciones de crear, leer, actualizar y eliminar los datos en la base de datos
from typing import List, Optional, Type, TypeVar
from sqlalchemy.orm import Session
from src.domain.models import (
    Usuarios,
    Rol,
    Estudiantes,
    Profesores,
    Monitores,
    Recursos,
    Equipos_portatiles,
    laboratorios,
    Prestamos,
    Novedades,
)
 
t = TypeVar('T')    

class baseRepository:
    def __init__(self, model: Type, db: Session):
        self.model = model
        self.db = db
    
    def get_all(self, skip: int = 0, limit: int = 100) -> List:
        return self.db.query(self.model).offset(skip).limit(limit).all()
    
    def get_by_id(self, record_id: int) -> Optional[object]:
        pk = self.model.__mapper__.primary_key[0].name
        return self.db.query(self.model).filter(getattr(self.model, pk) == record_id).first()
    
    def create(self, obj) -> object: 
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj
    
    def update(self, obj) -> object:
        self.db.commit()
        self.db.refresh(obj)
        return obj
    
    def delete(self, record_id: int) -> bool:
        obj = self.get_by_id(record_id)
        if not obj:
            return False
        self.db.delete(obj)
        self.db.commit()
        return True

#metodos especificos

class rolRepository(baseRepository):
    def __init__(self, db: Session):
        super().__init__(Rol, db)

    def get_by_nombre(self, nombre: str) -> Optional[Rol]:
        return self.db.query(Rol).filter(Rol.nombre_rol == nombre).first()
    
class usuarioRepository(baseRepository):
    def __init__(self, db: Session):
        super().__init__(Usuarios, db)

    def get_by_nombreUsuario(self, nombre: str) -> Optional[Usuarios]:
        return self.db.query(Usuarios).filter(Usuarios.nombre_completo == nombre).first()
    
    def get_by_correo(self, correo: str) -> Optional[Usuarios]:
        return self.db.query(Usuarios).filter(Usuarios.correo == correo).first()

class estudianteRepository(baseRepository):
    def __init__(self, db: Session):
        super().__init__(Estudiantes, db)

class profesorRepository(baseRepository):
    def __init__(self, db: Session):
        super().__init__(Profesores, db)

class monitorRepository(baseRepository):
    def __init__(self, db: Session):
        super().__init__(Monitores, db)

class recursoRepository(baseRepository):
    def __init__(self, db: Session):
        super().__init__(Recursos, db)

class equipoPortatilRepository(baseRepository):
    def __init__(self, db: Session):
        super().__init__(Equipos_portatiles, db)

class laboratorioRepository(baseRepository):
    def __init__(self, db: Session):
        super().__init__(laboratorios, db)

class prestamoRepository(baseRepository):
    def __init__(self, db: Session):
        super().__init__(Prestamos, db)

class novedadRepository(baseRepository):
    def __init__(self, db: Session):
        super().__init__(Novedades, db)
