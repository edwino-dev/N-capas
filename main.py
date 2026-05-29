#la entrada principal de nuestro proyecto, donde se ejecuta el programa
#para ejecutar desde la consola debemos ejecutar la sieguiente linea "venv\Scripts\uvicorn.exe main:app --reload" 
#la documentacion interactiva queda disponobile en http://localhost:8000/docs y http://localhost:8000/redoc

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.route import router

app = FastAPI(title="IUtede - gestion de recursos TICs", 
              description="Una API para gestion de recursos TICs de la Iutede.", 
              version="1.0.0")
#middleware cors permitir solicitudes y pruebas, pero se recomienda configurar esto de manera más restrictiva en producción.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #acepta solicitudes de cualquier origen, en producción se recomienda especificar los dominios permitidos
    allow_methods=["*"], #permite todos los métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"], #permite todos los encabezados HTTP, en producción se recomienda especificar los encabezados permitidos
)
#vamos a registrar las rutas definidas en el router, esto hace que las rutas estén disponibles para ser accedidas a través de la API
app.include_router(router)

#endpoint de salud, para verificar que la API está funcionando correctamente
@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "api": "IUtede backend", "version": "1.0.0"}