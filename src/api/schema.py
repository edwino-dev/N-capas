#DTO de phydantic 
#son como los contratos del api, definen la estructura de los datos que se reciben y
# se envian a traves del api

from datetime import datetime
from typing import Optional
from pydantic import BaseModel

#rol
class RolCreate(BaseModel):
    nombre_rol: str

class RolResponse(BaseModel):
    id_rol: int
    nombre_rol: str

    model_config = {'from_attributes': True}

#usuarios
class UsuarioCreate(BaseModel):
    id_rol: int
    nombre_completo: str
    correo: str
    contrasena_hash: str

class UsuarioResponse(BaseModel):
    id_usuario: int
    id_rol: int
    nombre_completo: str
    correo: str

    model_config = {'from_attributes': True}

class UsuarioUpdate(BaseModel):
    nombre_completo: Optional[str] = None
    correo: Optional[str] = None
    contrasena_hash: Optional[str] = None
    id_rol: Optional[int] = None

    model_config = {'from_attributes': True}

#estudiantes
class EstudianteCreate(BaseModel):
    id_usuario: int
    matricula: str
    programa: str

class EstudianteResponse(BaseModel):
    id_usuario: int
    matricula: str
    programa: str

    model_config = {'from_attributes': True}

class EstudianteUpdate(BaseModel):
    matricula: Optional[str] = None
    programa: Optional[str] = None

    model_config = {'from_attributes': True}

#profesores
class ProfesorCreate(BaseModel):
    id_usuario: int
    departamento: str

class ProfesorResponse(BaseModel):
    id_usuario: int
    departamento: str

    model_config = {'from_attributes': True}

class ProfesorUpdate(BaseModel):
    departamento: Optional[str] = None

    model_config = {'from_attributes': True}

#monitores
class MonitorCreate(BaseModel):
    id_usuario: int
    id_turno: int

class MonitorResponse(BaseModel):
    id_usuario: int
    id_turno: int

    model_config = {'from_attributes': True}

class MonitorUpdate(BaseModel):
    id_turno: Optional[int] = None

    model_config = {'from_attributes': True}

#recursos
class RecursoCreate(BaseModel):
    id_placa: str
    marca: str
    estado: str
    tipo_recurso: str

class RecursoResponse(BaseModel):
    id_recurso: int
    id_placa: str
    marca: str
    estado: str
    tipo_recurso: str

    model_config = {'from_attributes': True}

class RecursoUpdate(BaseModel):
    id_placa: Optional[str] = None
    marca: Optional[str] = None
    estado: Optional[str] = None
    tipo_recurso: Optional[str] = None

    model_config = {'from_attributes': True}

#equipos portatiles
class EquipoPortatilCreate(BaseModel):
    id_recurso: int
    modelo: str
    sistema_operativo: str

class EquipoPortatilResponse(BaseModel):
    id_recurso: int
    modelo: str
    sistema_operativo: str

    model_config = {'from_attributes': True}

class EquipoPortatilUpdate(BaseModel):
    modelo: Optional[str] = None
    sistema_operativo: Optional[str] = None

    model_config = {'from_attributes': True}

#laboratorios
class LaboratorioCreate(BaseModel):
    id_recurso: int
    capacidad: int
    software: str
    ubicacion: str

class LaboratorioResponse(BaseModel):
    id_recurso: int
    capacidad: int
    software: str
    ubicacion: str

    model_config = {'from_attributes': True}

class LaboratorioUpdate(BaseModel):
    capacidad: Optional[int] = None
    software: Optional[str] = None
    ubicacion: Optional[str] = None

    model_config = {'from_attributes': True}

#prestamos
class PrestamoCreate(BaseModel):
    id_reserva: int
    id_monitor_entrega: int
    hora_entrega: datetime
    hora_devolucion: Optional[datetime] = None
    estado_recepcion: Optional[str] = None

class PrestamoResponse(BaseModel):
    id_prestamo: int
    id_reserva: int
    id_monitor_entrega: int
    hora_entrega: datetime
    hora_devolucion: Optional[datetime] = None
    estado_recepcion: Optional[str] = None

    model_config = {'from_attributes': True}

class PrestamoUpdate(BaseModel):
    id_reserva: Optional[int] = None
    id_monitor_entrega: Optional[int] = None
    hora_entrega: Optional[datetime] = None
    hora_devolucion: Optional[datetime] = None
    estado_recepcion: Optional[str] = None

    model_config = {'from_attributes': True}

#novedades
class NovedadCreate(BaseModel):
    id_recurso: int
    id_usuario_reporta: int
    id_prestamo: Optional[int] = None
    descripcion: str
    gravedad: str
    estado: Optional[str] = "Reportada"

class NovedadResponse(BaseModel):
    id_novedad: int
    id_recurso: int
    id_usuario_reporta: int
    id_prestamo: Optional[int] = None
    descripcion: str
    gravedad: str
    estado: str
    fecha_reporte: datetime

    model_config = {'from_attributes': True}

class NovedadUpdate(BaseModel):
    id_recurso: Optional[int] = None
    id_usuario_reporta: Optional[int] = None
    id_prestamo: Optional[int] = None
    descripcion: Optional[str] = None
    gravedad: Optional[str] = None
    estado: Optional[str] = None

    model_config = {'from_attributes': True}

  