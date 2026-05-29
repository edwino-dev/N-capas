#rutas de los endpoints de la Api
#aqui estan definidos los endpoint http
#es la capa mas externa de nuestro modelo, es la que interactua con el mundo exterior,
# recibe las peticiones http, llama a los servicios para procesar la logica del negocio y
# devuelve las respuestas http

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from src.infraestructure.database import get_db
from src.application.services import (
    RolService,
    UsuarioService,
    EstudianteService,
    ProfesorService,
    MonitorService,
    RecursoService,
    EquipoPortatilService,
    LaboratorioService,
    PrestamoService,
    NovedadService,
)
from src.api.schema import (
    RolCreate,
    RolResponse,
    UsuarioCreate,
    UsuarioResponse,
    UsuarioUpdate,
    EstudianteCreate,
    EstudianteResponse,
    EstudianteUpdate,
    ProfesorCreate,
    ProfesorResponse,
    ProfesorUpdate,
    MonitorCreate,
    MonitorResponse,
    MonitorUpdate,
    RecursoCreate,
    RecursoResponse,
    RecursoUpdate,
    EquipoPortatilCreate,
    EquipoPortatilResponse,
    EquipoPortatilUpdate,
    LaboratorioCreate,
    LaboratorioResponse,
    LaboratorioUpdate,
    PrestamoCreate,
    PrestamoResponse,
    PrestamoUpdate,
    NovedadCreate,
    NovedadResponse,
    NovedadUpdate,
)

router = APIRouter()

# Roles
@router.get("/roles", response_model=List[RolResponse], tags=["Roles"])
def listar_roles(db: Session = Depends(get_db)):
    
    return RolService(db).listar()

@router.get("/roles/{id_rol}", response_model=RolResponse, tags=["Roles"])
def obtener_rol(id_rol: int, db: Session = Depends(get_db)):
    service = RolService(db)
    rol = service.get_rol_by_id(id_rol)
    if not rol:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rol no encontrado")
    return rol

@router.post("/roles", response_model=RolResponse, status_code=status.HTTP_201_CREATED, tags=["Roles"])
def crear_rol(data: RolCreate, db: Session = Depends(get_db)):
    service = RolService(db)
    return service.crear(data.nombre_rol)

@router.put("/roles/{id_rol}", response_model=RolResponse, tags=["Roles"])
def actualizar_rol(id_rol: int, data: RolCreate, db: Session = Depends(get_db)):
    service = RolService(db)
    rol_actualizado = service.actualizar(id_rol, data.nombre_rol)
    if not rol_actualizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rol no encontrado")
    return rol_actualizado

@router.delete("/roles/{id_rol}", status_code=status.HTTP_204_NO_CONTENT, tags=["Roles"])
def eliminar_rol(id_rol: int, db: Session = Depends(get_db)):
    service = RolService(db)
    if not service.eliminar(id_rol):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rol no encontrado")

# Usuarios
@router.get("/usuarios", response_model=List[UsuarioResponse], tags=["Usuarios"])
def listar_usuarios(db: Session = Depends(get_db)):
    service = UsuarioService(db)
    return service.listar()

@router.get("/usuarios/{id_usuario}", response_model=UsuarioResponse, tags=["Usuarios"])
def obtener_usuario(id_usuario: int, db: Session = Depends(get_db)):
    service = UsuarioService(db)
    usuario = service.get_usuario_by_id(id_usuario)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuario

@router.post("/usuarios", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED, tags=["Usuarios"])
def crear_usuario(data: UsuarioCreate, db: Session = Depends(get_db)):
    service = UsuarioService(db)
    return service.crear(data.id_rol, data.nombre_completo, data.correo, data.contrasena_hash)

@router.put("/usuarios/{id_usuario}", response_model=UsuarioResponse, tags=["Usuarios"])
def actualizar_usuario(id_usuario: int, data: UsuarioUpdate, db: Session = Depends(get_db)):
    service = UsuarioService(db)
    usuario_actualizado = service.actualizar(id_usuario, **data.model_dump(exclude_none=True))
    if not usuario_actualizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuario_actualizado

@router.delete("/usuarios/{id_usuario}", status_code=status.HTTP_204_NO_CONTENT, tags=["Usuarios"])
def eliminar_usuario(id_usuario: int, db: Session = Depends(get_db)):
    service = UsuarioService(db)
    if not service.eliminar(id_usuario):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")

# Estudiantes
@router.get("/estudiantes", response_model=List[EstudianteResponse], tags=["Estudiantes"])
def listar_estudiantes(db: Session = Depends(get_db)):
    service = EstudianteService(db)
    return service.listar()

@router.get("/estudiantes/{id_usuario}", response_model=EstudianteResponse, tags=["Estudiantes"])
def obtener_estudiante(id_usuario: int, db: Session = Depends(get_db)):
    service = EstudianteService(db)
    estudiante = service.get_by_id(id_usuario)
    if not estudiante:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estudiante no encontrado")
    return estudiante

@router.post("/estudiantes", response_model=EstudianteResponse, status_code=status.HTTP_201_CREATED, tags=["Estudiantes"])
def crear_estudiante(data: EstudianteCreate, db: Session = Depends(get_db)):
    service = EstudianteService(db)
    return service.crear(data.id_usuario, data.matricula, data.programa)

@router.put("/estudiantes/{id_usuario}", response_model=EstudianteResponse, tags=["Estudiantes"])
def actualizar_estudiante(id_usuario: int, data: EstudianteUpdate, db: Session = Depends(get_db)):
    service = EstudianteService(db)
    estudiante_actualizado = service.actualizar(id_usuario, **data.model_dump(exclude_none=True))
    if not estudiante_actualizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estudiante no encontrado")
    return estudiante_actualizado

@router.delete("/estudiantes/{id_usuario}", status_code=status.HTTP_204_NO_CONTENT, tags=["Estudiantes"])
def eliminar_estudiante(id_usuario: int, db: Session = Depends(get_db)):
    service = EstudianteService(db)
    if not service.eliminar(id_usuario):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estudiante no encontrado")

# Profesores
@router.get("/profesores", response_model=List[ProfesorResponse], tags=["Profesores"])
def listar_profesores(db: Session = Depends(get_db)):
    service = ProfesorService(db)
    return service.listar()

@router.get("/profesores/{id_usuario}", response_model=ProfesorResponse, tags=["Profesores"])
def obtener_profesor(id_usuario: int, db: Session = Depends(get_db)):
    service = ProfesorService(db)
    profesor = service.get_by_id(id_usuario)
    if not profesor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profesor no encontrado")
    return profesor

@router.post("/profesores", response_model=ProfesorResponse, status_code=status.HTTP_201_CREATED, tags=["Profesores"])
def crear_profesor(data: ProfesorCreate, db: Session = Depends(get_db)):
    service = ProfesorService(db)
    return service.crear(data.id_usuario, data.departamento)

@router.put("/profesores/{id_usuario}", response_model=ProfesorResponse, tags=["Profesores"])
def actualizar_profesor(id_usuario: int, data: ProfesorUpdate, db: Session = Depends(get_db)):
    service = ProfesorService(db)
    profesor_actualizado = service.actualizar(id_usuario, **data.model_dump(exclude_none=True))
    if not profesor_actualizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profesor no encontrado")
    return profesor_actualizado

@router.delete("/profesores/{id_usuario}", status_code=status.HTTP_204_NO_CONTENT, tags=["Profesores"])
def eliminar_profesor(id_usuario: int, db: Session = Depends(get_db)):
    service = ProfesorService(db)
    if not service.eliminar(id_usuario):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profesor no encontrado")

# Monitores
@router.get("/monitores", response_model=List[MonitorResponse], tags=["Monitores"])
def listar_monitores(db: Session = Depends(get_db)):
    service = MonitorService(db)
    return service.listar()

@router.get("/monitores/{id_usuario}", response_model=MonitorResponse, tags=["Monitores"])
def obtener_monitor(id_usuario: int, db: Session = Depends(get_db)):
    service = MonitorService(db)
    monitor = service.get_by_id(id_usuario)
    if not monitor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Monitor no encontrado")
    return monitor

@router.post("/monitores", response_model=MonitorResponse, status_code=status.HTTP_201_CREATED, tags=["Monitores"])
def crear_monitor(data: MonitorCreate, db: Session = Depends(get_db)):
    service = MonitorService(db)
    return service.crear(data.id_usuario, data.id_turno)

@router.put("/monitores/{id_usuario}", response_model=MonitorResponse, tags=["Monitores"])
def actualizar_monitor(id_usuario: int, data: MonitorUpdate, db: Session = Depends(get_db)):
    service = MonitorService(db)
    monitor_actualizado = service.actualizar(id_usuario, **data.model_dump(exclude_none=True))
    if not monitor_actualizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Monitor no encontrado")
    return monitor_actualizado

@router.delete("/monitores/{id_usuario}", status_code=status.HTTP_204_NO_CONTENT, tags=["Monitores"])
def eliminar_monitor(id_usuario: int, db: Session = Depends(get_db)):
    service = MonitorService(db)
    if not service.eliminar(id_usuario):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Monitor no encontrado")

# Recursos
@router.get("/recursos", response_model=List[RecursoResponse], tags=["Recursos"])
def listar_recursos(db: Session = Depends(get_db)):
    service = RecursoService(db)
    return service.listar()

@router.get("/recursos/{id_recurso}", response_model=RecursoResponse, tags=["Recursos"])
def obtener_recurso(id_recurso: int, db: Session = Depends(get_db)):
    service = RecursoService(db)
    recurso = service.get_by_id(id_recurso)
    if not recurso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recurso no encontrado")
    return recurso

@router.post("/recursos", response_model=RecursoResponse, status_code=status.HTTP_201_CREATED, tags=["Recursos"])
def crear_recurso(data: RecursoCreate, db: Session = Depends(get_db)):
    service = RecursoService(db)
    return service.crear(data.id_placa, data.marca, data.estado, data.tipo_recurso)

@router.put("/recursos/{id_recurso}", response_model=RecursoResponse, tags=["Recursos"])
def actualizar_recurso(id_recurso: int, data: RecursoUpdate, db: Session = Depends(get_db)):
    service = RecursoService(db)
    recurso_actualizado = service.actualizar(id_recurso, **data.model_dump(exclude_none=True))
    if not recurso_actualizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recurso no encontrado")
    return recurso_actualizado

@router.delete("/recursos/{id_recurso}", status_code=status.HTTP_204_NO_CONTENT, tags=["Recursos"])
def eliminar_recurso(id_recurso: int, db: Session = Depends(get_db)):
    service = RecursoService(db)
    if not service.eliminar(id_recurso):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recurso no encontrado")

# Equipos portatiles
@router.get("/equipos-portatiles", response_model=List[EquipoPortatilResponse], tags=["Equipos Portatiles"])
def listar_equipos_portatiles(db: Session = Depends(get_db)):
    service = EquipoPortatilService(db)
    return service.listar()

@router.get("/equipos-portatiles/{id_recurso}", response_model=EquipoPortatilResponse, tags=["Equipos Portatiles"])
def obtener_equipo_portatil(id_recurso: int, db: Session = Depends(get_db)):
    service = EquipoPortatilService(db)
    equipo = service.get_by_id(id_recurso)
    if not equipo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Equipo portatil no encontrado")
    return equipo

@router.post("/equipos-portatiles", response_model=EquipoPortatilResponse, status_code=status.HTTP_201_CREATED, tags=["Equipos Portatiles"])
def crear_equipo_portatil(data: EquipoPortatilCreate, db: Session = Depends(get_db)):
    service = EquipoPortatilService(db)
    return service.crear(data.id_recurso, data.modelo, data.sistema_operativo)

@router.put("/equipos-portatiles/{id_recurso}", response_model=EquipoPortatilResponse, tags=["Equipos Portatiles"])
def actualizar_equipo_portatil(id_recurso: int, data: EquipoPortatilUpdate, db: Session = Depends(get_db)):
    service = EquipoPortatilService(db)
    equipo_actualizado = service.actualizar(id_recurso, **data.model_dump(exclude_none=True))
    if not equipo_actualizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Equipo portatil no encontrado")
    return equipo_actualizado

@router.delete("/equipos-portatiles/{id_recurso}", status_code=status.HTTP_204_NO_CONTENT, tags=["Equipos Portatiles"])
def eliminar_equipo_portatil(id_recurso: int, db: Session = Depends(get_db)):
    service = EquipoPortatilService(db)
    if not service.eliminar(id_recurso):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Equipo portatil no encontrado")

# Laboratorios
@router.get("/laboratorios", response_model=List[LaboratorioResponse], tags=["Laboratorios"])
def listar_laboratorios(db: Session = Depends(get_db)):
    service = LaboratorioService(db)
    return service.listar()

@router.get("/laboratorios/{id_recurso}", response_model=LaboratorioResponse, tags=["Laboratorios"])
def obtener_laboratorio(id_recurso: int, db: Session = Depends(get_db)):
    service = LaboratorioService(db)
    laboratorio = service.get_by_id(id_recurso)
    if not laboratorio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Laboratorio no encontrado")
    return laboratorio

@router.post("/laboratorios", response_model=LaboratorioResponse, status_code=status.HTTP_201_CREATED, tags=["Laboratorios"])
def crear_laboratorio(data: LaboratorioCreate, db: Session = Depends(get_db)):
    service = LaboratorioService(db)
    return service.crear(data.id_recurso, data.capacidad, data.software, data.ubicacion)

@router.put("/laboratorios/{id_recurso}", response_model=LaboratorioResponse, tags=["Laboratorios"])
def actualizar_laboratorio(id_recurso: int, data: LaboratorioUpdate, db: Session = Depends(get_db)):
    service = LaboratorioService(db)
    laboratorio_actualizado = service.actualizar(id_recurso, **data.model_dump(exclude_none=True))
    if not laboratorio_actualizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Laboratorio no encontrado")
    return laboratorio_actualizado

@router.delete("/laboratorios/{id_recurso}", status_code=status.HTTP_204_NO_CONTENT, tags=["Laboratorios"])
def eliminar_laboratorio(id_recurso: int, db: Session = Depends(get_db)):
    service = LaboratorioService(db)
    if not service.eliminar(id_recurso):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Laboratorio no encontrado")

# Prestamos
@router.get("/prestamos", response_model=List[PrestamoResponse], tags=["Prestamos"])
def listar_prestamos(db: Session = Depends(get_db)):
    service = PrestamoService(db)
    return service.listar()

@router.get("/prestamos/{id_prestamo}", response_model=PrestamoResponse, tags=["Prestamos"])
def obtener_prestamo(id_prestamo: int, db: Session = Depends(get_db)):
    service = PrestamoService(db)
    prestamo = service.get_by_id(id_prestamo)
    if not prestamo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prestamo no encontrado")
    return prestamo

@router.post("/prestamos", response_model=PrestamoResponse, status_code=status.HTTP_201_CREATED, tags=["Prestamos"])
def crear_prestamo(data: PrestamoCreate, db: Session = Depends(get_db)):
    service = PrestamoService(db)
    return service.crear(
        data.id_reserva,
        data.id_monitor_entrega,
        data.hora_entrega,
        data.hora_devolucion,
        data.estado_recepcion,
    )

@router.put("/prestamos/{id_prestamo}", response_model=PrestamoResponse, tags=["Prestamos"])
def actualizar_prestamo(id_prestamo: int, data: PrestamoUpdate, db: Session = Depends(get_db)):
    service = PrestamoService(db)
    prestamo_actualizado = service.actualizar(id_prestamo, **data.model_dump(exclude_none=True))
    if not prestamo_actualizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prestamo no encontrado")
    return prestamo_actualizado

@router.delete("/prestamos/{id_prestamo}", status_code=status.HTTP_204_NO_CONTENT, tags=["Prestamos"])
def eliminar_prestamo(id_prestamo: int, db: Session = Depends(get_db)):
    service = PrestamoService(db)
    if not service.eliminar(id_prestamo):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prestamo no encontrado")

# Novedades
@router.get("/novedades", response_model=List[NovedadResponse], tags=["Novedades"])
def listar_novedades(db: Session = Depends(get_db)):
    service = NovedadService(db)
    return service.listar()

@router.get("/novedades/{id_novedad}", response_model=NovedadResponse, tags=["Novedades"])
def obtener_novedad(id_novedad: int, db: Session = Depends(get_db)):
    service = NovedadService(db)
    novedad = service.get_by_id(id_novedad)
    if not novedad:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Novedad no encontrada")
    return novedad

@router.post("/novedades", response_model=NovedadResponse, status_code=status.HTTP_201_CREATED, tags=["Novedades"])
def crear_novedad(data: NovedadCreate, db: Session = Depends(get_db)):
    service = NovedadService(db)
    return service.crear(
        data.id_recurso,
        data.id_usuario_reporta,
        data.id_prestamo,
        data.descripcion,
        data.gravedad,
        data.estado,
    )

@router.put("/novedades/{id_novedad}", response_model=NovedadResponse, tags=["Novedades"])
def actualizar_novedad(id_novedad: int, data: NovedadUpdate, db: Session = Depends(get_db)):
    service = NovedadService(db)
    novedad_actualizada = service.actualizar(id_novedad, **data.model_dump(exclude_none=True))
    if not novedad_actualizada:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Novedad no encontrada")
    return novedad_actualizada

@router.delete("/novedades/{id_novedad}", status_code=status.HTTP_204_NO_CONTENT, tags=["Novedades"])
def eliminar_novedad(id_novedad: int, db: Session = Depends(get_db)):
    service = NovedadService(db)
    if not service.eliminar(id_novedad):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Novedad no encontrada")
