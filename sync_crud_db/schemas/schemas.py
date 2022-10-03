from pydantic import BaseModel
from typing import Dict, Optional, List
from datetime import datetime

### Schemas for each http method

class VariableDocumentacion(BaseModel):
    id_variable:str
    id_rutina:int
    id_tipo_catalogo:Optional[int] = None
    nombre_campo:Optional[str] = None
    nombre_estructura:Optional[str] = None
    id_catalogo:Optional[int] = None
    key_catalogo:Optional[str] = None
    valor_catalogo:Optional[str] = None
    fecha_creacion:datetime
    usuario_creacion:str
    fecha_modificacion: Optional[datetime] = None
    usuario_modificacion: Optional[str] = None
    
    class Config:
        orm_mode = True


class VariableCriterioBusqueda(BaseModel):
    id_variable: str
    id_tipo_filtro: int
    valor_filtro: str
    fecha_creacion: datetime
    usuario_creacion: str
    fecha_modificacion: Optional[datetime] = None
    usuario_modificacion: Optional[str] = None
    # estatus: Optional[str] = None
    
    class Config:
        orm_mode = True

class CatTipoFiltro(BaseModel):
    id_tipo_filtro: int
    tipo_catalogo: str
    estatus: Optional[str] = None
    fecha_creacion: datetime
    usuario_creacion: str
    fecha_modificacion: Optional[datetime] = None
    usuario_modificacion: Optional[str] = None
    
    class Config:
        orm_mode = True

class CatRutina(BaseModel):
    id_rutina: int
    rutina: str
    estatus: str
    fecha_creacion: datetime
    usuario_creacion: str
    fecha_modificacion: Optional[datetime] = None
    usuario_modificacion: Optional[str] = None
    url: Optional[str] = None
    
    class Config:
        orm_mode = True
    
class CatTipoCatalogo(BaseModel):
    id_tipo_catalogo: int
    tipo_catalogo: str
    estatus: Optional[str] = None
    fecha_creacion: datetime
    usuario_creacion: str
    fecha_modificacion: Optional[datetime] = None
    usuario_modificacion: Optional[str] = None
    
    class Config:
        orm_mode = True

### Responses schema

class SuccessResponse(BaseModel):
    codigo_ejecucion: int
    mensaje_ejecucion: str
    data: Optional[List] = []

class ErrorResponse(BaseModel):
    codigo_status: int
    error: str
    hora_incidencia: datetime
    mensaje: str
    
    