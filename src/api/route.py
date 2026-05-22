#rutas de los endpoints de la Api
#aqui estan definidos los endpoint http
#es la capa mas externa de nuestro modelo, es la que interactua con el mundo exterior, 
# recibe las peticiones http, llama a los servicios para procesar la logica del negocio y 
# devuelve las respuestas http

#metodos http: 
# get= obtener recursos
#  post= crear recursos
#  put= actualizar recursos
#patch= actualizar parcialmente recursos
# delete= eliminar recursos

#codigos de estado http:
# 200= ok   
# 201= creado
#204= sin contenido delete exitoso
# 400= solicitud incorrecta
# 404= no encontrado not found 
# 500= error interno del servidor

#depends(get_db) FastApi inyecta una sesion de la base de datos en cada endpoint, 
# lo que permite a los endpoints interactuar con la base de datos a traves 
# de los servicios y repositorios

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import session 
from typing import List 
from src.infraestructure.database import get_db
from src.application.services import (RolService, UsuarioService)
from src.api.schema import (RolCreate, RolResponse, usuariosCreate, usuariosResponse, usuariosUpdate)

#Apirouter es una clase de FastAPI que permite organizar los endpoints en grupos,asigna un versionamiento de nusetra api
router = APIRouter(prefix="/api/v1")
 #rol
@router.get("/roles", response_model=List[RolResponse], tags=["Roles"])
def listar_roles(db: session = Depends(get_db)):
    service = RolService(db)
    return service.listar()

@router.get("/roles/{id_rol}", response_model=RolResponse, tags=["Roles"])
def obtener_rol(id_rol: int, db: session = Depends(get_db)):
    service = RolService(db)
    rol = service.get_rol_by_id(id_rol)
    if not rol:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rol no encontrado")
    return rol

@router.post("/roles", response_model=RolResponse, status_code=status.HTTP_201_CREATED, tags=["Roles"])

def crear_rol(data: RolCreate, db: session = Depends(get_db)):
    service = RolService(db)
    return service.crear(data)

@router.delete("/roles/{id_rol}", status_code=status.HTTP_204_NO_CONTENT, tags=["Roles"])
def eliminar_rol(id_rol: int, db: session = Depends(get_db)):    
    service = RolService(db)
    if not service.eliminar(id_rol):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rol no encontrado")
    #no hay necesidad de hacer return por que fast api retorna 204 automaticamente cuando el status code es 204

@router.get("/usuarios", response_model=List[usuariosResponse], tags=["Usuarios"])
def listar_usuarios(db: session = Depends(get_db)): 
    service = UsuarioService(db)
    return service.usuarios()

@router.get("/usuarios", response_model=usuariosResponse, tags=["Usuarios"])
def obtener_usuario(id_usuario: int, db: session = Depends(get_db)):
    service = UsuarioService(db)
    return service.obtener(id_usuario)
    usuario = service.get_usuario_by_id(id_usuario)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")      
    return usuario  

@router.post("/usuarios", response_model=usuariosResponse, status_code=status.HTTP_201_CREATED, tags=["Usuarios"])
def crear_usuario(data: usuariosCreate, db: session = Depends(get_db)):
    service = UsuarioService(db)
    return service.crear(data.id_rol, data.nombre_completo, data.correo, data.contrasena_hash)     



@router.delete("/usuarios/{id_usuario}", status_code=status.HTTP_204_NO_CONTENT, tags=["Usuarios"])
def eliminar_usuario(id_usuario: int, db: session = Depends(get_db)):
    service = UsuarioService(db)
    if not service.eliminar(id_usuario):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    #no hay necesidad de hacer return por que fast api retorna 204 automaticamente cuando el status code es 204

@router.put("/usuarios/{id_usuario}", response_model=usuariosResponse, tags=["Usuarios"])
def actualizar_usuario(id_usuario: int, data: usuariosUpdate, db: session = Depends(get_db)):
    service = UsuarioService(db)
    #cuando hace el update solo actualiza los campos modificados, por eso se usa data.model_dump(exclude_none=True) para excluir los campos que no se modificaron y asi evitar sobreescribir datos existentes con valores nulos
    usuario_actualizado = service.actualizar(id_usuario, **data.model_dump(exclude_none=True))
    if not usuario_actualizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuario_actualizado                  