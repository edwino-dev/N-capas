#casos de uso del sistema 
#saben que hacer pero le delegan a los repositorios como hacer el crud
#responsabilidad de esta capa orquestar la comunicacion con los repositorios, aplicar las reglas de negocio
#una reserva de un laboratorio solo se aprueba si esta en estado pendiente
#transforamr los datos antes de retornarlos al api 
#Capa api se encarga de recibir las peticiones http 
#servicio aplica la logica del negocio
#repositorio se encarga de la comunicacion con la base de datos
from datetime import datetime
from typing import List, Optional   
from sqlalchemy.orm import Session
from src.domain.models import (Usuarios, Rol, Estudiantes, Profesores, Monitores, Novedades)
from src.infraestructure.repository import (baseRepository, rolRepository, usuarioRepository)

#rolservice
class RolService:
    def __init__(self, db: Session):
        self.repo  = rolRepository(db)
        
    def listar(self) -> List[Rol]:
        return self.repo.get_all()
        
    def get_rol_by_id(self, id_rol: int) -> Optional[Rol]:
        return self.repo.get_by_id(id_rol)
    
    def crear(self, nombrerol: str) -> Rol:
        return self.repo.create(nombre_rol = nombrerol)
    
    def eliminar(self, id_rol: int) -> bool:
        return self.repo.delete(id_rol)
    
    def actualizar(self, id_rol: int, nombre_rol: str) -> Optional[Rol]:
        rol = self.repo.get_by_id(id_rol)
        if not rol:
            return None
        rol.nombre_rol = nombre_rol
        return self.repo.update(rol)
    
    



#usuario service
class UsuarioService:
    def __init__(self, db: Session):
        self.repo  = usuarioRepository(db)
        
    def listar(self) -> List[Usuarios]:
        return self.repo.get_all()
        
    def get_usuario_by_id(self, id_usuario: int) -> Optional[Usuarios]:
        return self.repo.get_by_id(id_usuario)
    
    def get_by_nombre(self, nombre_completo: str) -> Optional[Usuarios]:
        return self.repo.get_by_nombre(nombre_completo)
    
    def get_by_correo(self, correo_electronico: str) -> Optional[Usuarios]:
        return self.repo.get_by_correo(correo_electronico)  
    
    def crear(self, id_rol : int, nombre_completo: str, correo: str, password: str, id_usuario: int) -> Usuarios:
        new_usuario = Usuarios(
            id_rol=id_rol,
            nombre_completo=nombre_completo,
            correo_electronico=correo,
            contrasena_hash=password
            
        )
        return self.repo.create(Usuarios)
    
    def eliminar(self, id_usuario: int) -> bool:    
        return self.repo.delete(id_usuario)
    
    def actualizar(self, id_usuario: int, nombre_completo: str, correo_electronico: str, contrasena: str, id_rol: int) -> Optional[Usuarios]:
        usuario = self.repo.get_by_id(id_usuario)
        if not usuario:
            return None
        usuario.nombre_completo = nombre_completo
        usuario.correo_electronico = correo_electronico
        usuario.contrasena = contrasena
        usuario.id_rol = id_rol
        return self.repo.update(usuario)
