from pydantic import BaseModel, Field
from typing import List, Dict
from uuid import uuid4
from datetime import datetime


# 🔧 Configuración por defecto
def default_database_config() -> Dict[str, str]:
    return {
        "host": "localhost",
        "port": 5432,
        "user": "admin",
    }


# 📋 Valor contextual o externo
def default_ciudad() -> str:
    return "Madrid"


# 🧩 Modelo base para configuración o API
class AppSettings(BaseModel):
    debug: bool = False
    ciudad: str = Field(default_factory=default_ciudad)
    database: Dict[str, str] = Field(default_factory=default_database_config)
    logs: List[str] = Field(default_factory=list)


# 🧪 Modelo de datos con identificadores y timestamps
class Evento(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    metadata: Dict[str, str] = Field(default_factory=dict)


# ⚙️ Modelo mutable de estado
class Tarea(BaseModel):
    nombre: str
    estado: Dict[str, bool] = Field(default_factory=lambda: {"creado": True})


# ✅ Ejemplo de uso
if __name__ == "__main__":
    config = AppSettings()
    print(config.model_dump())

    evento = Evento()
    print(evento.model_dump())

    tarea = Tarea(nombre="Actualizar dependencias")
    print(tarea.model_dump())
