#DTO de phydantic 
#son como los contratos del api, definen la estructura de los datos que se reciben y
# se envian a traves del api

from typing import Optional
from pydantic import BaseModel

#rol
class RolCreate(BaseModel):
    nombre_rol: str

class RolResponse(BaseModel):
    id_rol: int
    nombre_rol: str
    model_config = {'from_attributes': True}  

class usuariosCreate(BaseModel):
    id_rol: int
    nombre_completo: str
    correo: str
    contrasena_hash: str

class usuariosResponse(BaseModel):
    id_usuario: int
    id_rol: int
    nombre_completo: str
    correo: str

    model_config = {'from_attributes': True}

class usuariosUpdate(BaseModel):
    nombre_completo: Optional[str] = None
    correo: Optional[str] = None
    contrasena_hash: Optional[str] = None
    
    model_config = {'from_attributes': True}

  