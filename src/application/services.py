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
from src.infraestructure.repository import (
    rolRepository,
    usuarioRepository,
    estudianteRepository,
    profesorRepository,
    monitorRepository,
    recursoRepository,
    equipoPortatilRepository,
    laboratorioRepository,
    prestamoRepository,
    novedadRepository,
)

#rolservice
class RolService:
    def __init__(self, db: Session):
        self.repo = rolRepository(db)

    def listar(self) -> List[Rol]:
        return self.repo.get_all()

    def get_rol_by_id(self, id_rol: int) -> Optional[Rol]:
        return self.repo.get_by_id(id_rol)
    
    def crear(self, nombre_rol: str) -> Rol:
        rol = Rol(nombre_rol=nombre_rol)
        return self.repo.create(rol)
    
    def eliminar(self, id_rol: int) -> bool:
        return self.repo.delete(id_rol)
    
    def actualizar(self, id_rol: int, nombre_rol: str) -> Optional[Rol]:
        rol = self.repo.get_by_id(id_rol)
        if not rol:
            return None
        rol.nombre_rol = nombre_rol
        return self.repo.update(rol)

class UsuarioService:
    def __init__(self, db: Session):
        self.repo = usuarioRepository(db)

    def listar(self) -> List[Usuarios]:
        return self.repo.get_all()

    def get_usuario_by_id(self, id_usuario: int) -> Optional[Usuarios]:
        return self.repo.get_by_id(id_usuario)
    
    def get_by_nombre(self, nombre_completo: str) -> Optional[Usuarios]:
        return self.repo.get_by_nombreUsuario(nombre_completo)
    
    def get_by_correo(self, correo: str) -> Optional[Usuarios]:
        return self.repo.get_by_correo(correo)  
    
    def crear(self, id_rol: int, nombre_completo: str, correo: str, contrasena_hash: str) -> Usuarios:
        new_usuario = Usuarios(
            id_rol=id_rol,
            nombre_completo=nombre_completo,
            correo=correo,
            contrasena_hash=contrasena_hash,
        )
        return self.repo.create(new_usuario)
    
    def eliminar(self, id_usuario: int) -> bool:    
        return self.repo.delete(id_usuario)
    
    def actualizar(self, id_usuario: int, **kwargs) -> Optional[Usuarios]:
        usuario = self.repo.get_by_id(id_usuario)
        if not usuario:
            return None
        for key, value in kwargs.items():
            setattr(usuario, key, value)
        return self.repo.update(usuario)

class EstudianteService:
    def __init__(self, db: Session):
        self.repo = estudianteRepository(db)

    def listar(self) -> List[Estudiantes]:
        return self.repo.get_all()

    def get_by_id(self, id_usuario: int) -> Optional[Estudiantes]:
        return self.repo.get_by_id(id_usuario)

    def crear(self, id_usuario: int, matricula: str, programa: str) -> Estudiantes:
        estudiante = Estudiantes(id_usuario=id_usuario, matricula=matricula, programa=programa)
        return self.repo.create(estudiante)

    def eliminar(self, id_usuario: int) -> bool:
        return self.repo.delete(id_usuario)

    def actualizar(self, id_usuario: int, **kwargs) -> Optional[Estudiantes]:
        estudiante = self.repo.get_by_id(id_usuario)
        if not estudiante:
            return None
        for key, value in kwargs.items():
            setattr(estudiante, key, value)
        return self.repo.update(estudiante)

class ProfesorService:
    def __init__(self, db: Session):
        self.repo = profesorRepository(db)

    def listar(self) -> List[Profesores]:
        return self.repo.get_all()

    def get_by_id(self, id_usuario: int) -> Optional[Profesores]:
        return self.repo.get_by_id(id_usuario)

    def crear(self, id_usuario: int, departamento: str) -> Profesores:
        profesor = Profesores(id_usuario=id_usuario, departamento=departamento)
        return self.repo.create(profesor)

    def eliminar(self, id_usuario: int) -> bool:
        return self.repo.delete(id_usuario)

    def actualizar(self, id_usuario: int, **kwargs) -> Optional[Profesores]:
        profesor = self.repo.get_by_id(id_usuario)
        if not profesor:
            return None
        for key, value in kwargs.items():
            setattr(profesor, key, value)
        return self.repo.update(profesor)

class MonitorService:
    def __init__(self, db: Session):
        self.repo = monitorRepository(db)

    def listar(self) -> List[Monitores]:
        return self.repo.get_all()

    def get_by_id(self, id_usuario: int) -> Optional[Monitores]:
        return self.repo.get_by_id(id_usuario)

    def crear(self, id_usuario: int, id_turno: int) -> Monitores:
        monitor = Monitores(id_usuario=id_usuario, id_turno=id_turno)
        return self.repo.create(monitor)

    def eliminar(self, id_usuario: int) -> bool:
        return self.repo.delete(id_usuario)

    def actualizar(self, id_usuario: int, **kwargs) -> Optional[Monitores]:
        monitor = self.repo.get_by_id(id_usuario)
        if not monitor:
            return None
        for key, value in kwargs.items():
            setattr(monitor, key, value)
        return self.repo.update(monitor)

class RecursoService:
    def __init__(self, db: Session):
        self.repo = recursoRepository(db)

    def listar(self) -> List[Recursos]:
        return self.repo.get_all()

    def get_by_id(self, id_recurso: int) -> Optional[Recursos]:
        return self.repo.get_by_id(id_recurso)

    def crear(self, id_placa: str, marca: str, estado: str, tipo_recurso: str) -> Recursos:
        recurso = Recursos(id_placa=id_placa, marca=marca, estado=estado, tipo_recurso=tipo_recurso)
        return self.repo.create(recurso)

    def eliminar(self, id_recurso: int) -> bool:
        return self.repo.delete(id_recurso)

    def actualizar(self, id_recurso: int, **kwargs) -> Optional[Recursos]:
        recurso = self.repo.get_by_id(id_recurso)
        if not recurso:
            return None
        for key, value in kwargs.items():
            setattr(recurso, key, value)
        return self.repo.update(recurso)

class EquipoPortatilService:
    def __init__(self, db: Session):
        self.repo = equipoPortatilRepository(db)

    def listar(self) -> List[Equipos_portatiles]:
        return self.repo.get_all()

    def get_by_id(self, id_recurso: int) -> Optional[Equipos_portatiles]:
        return self.repo.get_by_id(id_recurso)

    def crear(self, id_recurso: int, modelo: str, sistema_operativo: str) -> Equipos_portatiles:
        equipo = Equipos_portatiles(id_recurso=id_recurso, modelo=modelo, sistema_operativo=sistema_operativo)
        return self.repo.create(equipo)

    def eliminar(self, id_recurso: int) -> bool:
        return self.repo.delete(id_recurso)

    def actualizar(self, id_recurso: int, **kwargs) -> Optional[Equipos_portatiles]:
        equipo = self.repo.get_by_id(id_recurso)
        if not equipo:
            return None
        for key, value in kwargs.items():
            setattr(equipo, key, value)
        return self.repo.update(equipo)

class LaboratorioService:
    def __init__(self, db: Session):
        self.repo = laboratorioRepository(db)

    def listar(self) -> List[laboratorios]:
        return self.repo.get_all()

    def get_by_id(self, id_recurso: int) -> Optional[laboratorios]:
        return self.repo.get_by_id(id_recurso)

    def crear(self, id_recurso: int, capacidad: int, software: str, ubicacion: str) -> laboratorios:
        laboratorio = laboratorios(id_recurso=id_recurso, capacidad=capacidad, software=software, ubicacion=ubicacion)
        return self.repo.create(laboratorio)

    def eliminar(self, id_recurso: int) -> bool:
        return self.repo.delete(id_recurso)

    def actualizar(self, id_recurso: int, **kwargs) -> Optional[laboratorios]:
        laboratorio = self.repo.get_by_id(id_recurso)
        if not laboratorio:
            return None
        for key, value in kwargs.items():
            setattr(laboratorio, key, value)
        return self.repo.update(laboratorio)

class PrestamoService:
    def __init__(self, db: Session):
        self.repo = prestamoRepository(db)

    def listar(self) -> List[Prestamos]:
        return self.repo.get_all()

    def get_by_id(self, id_prestamo: int) -> Optional[Prestamos]:
        return self.repo.get_by_id(id_prestamo)

    def crear(
        self,
        id_reserva: int,
        id_monitor_entrega: int,
        hora_entrega: datetime,
        hora_devolucion: Optional[datetime],
        estado_recepcion: Optional[str],
    ) -> Prestamos:
        prestamo = Prestamos(
            id_reserva=id_reserva,
            id_monitor_entrega=id_monitor_entrega,
            hora_entrega=hora_entrega,
            hora_devolucion=hora_devolucion,
            estado_recepcion=estado_recepcion,
        )
        return self.repo.create(prestamo)

    def eliminar(self, id_prestamo: int) -> bool:
        return self.repo.delete(id_prestamo)

    def actualizar(self, id_prestamo: int, **kwargs) -> Optional[Prestamos]:
        prestamo = self.repo.get_by_id(id_prestamo)
        if not prestamo:
            return None
        for key, value in kwargs.items():
            setattr(prestamo, key, value)
        return self.repo.update(prestamo)

class NovedadService:
    def __init__(self, db: Session):
        self.repo = novedadRepository(db)

    def listar(self) -> List[Novedades]:
        return self.repo.get_all()

    def get_by_id(self, id_novedad: int) -> Optional[Novedades]:
        return self.repo.get_by_id(id_novedad)

    def crear(
        self,
        id_recurso: int,
        id_usuario_reporta: int,
        id_prestamo: Optional[int],
        descripcion: str,
        gravedad: str,
        estado: Optional[str],
    ) -> Novedades:
        novedad = Novedades(
            id_recurso=id_recurso,
            id_usuario_reporta=id_usuario_reporta,
            id_prestamo=id_prestamo,
            descripcion=descripcion,
            gravedad=gravedad,
            estado=estado or "Reportada",
        )
        return self.repo.create(novedad)

    def eliminar(self, id_novedad: int) -> bool:
        return self.repo.delete(id_novedad)

    def actualizar(self, id_novedad: int, **kwargs) -> Optional[Novedades]:
        novedad = self.repo.get_by_id(id_novedad)
        if not novedad:
            return None
        for key, value in kwargs.items():
            setattr(novedad, key, value)
        return self.repo.update(novedad)
