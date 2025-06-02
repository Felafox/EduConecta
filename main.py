from fastapi import FastAPI
from api.endpoints.webhook import webhook_router # <-- IMPORTA EL ROUTER

app = FastAPI(
    title="EduConecta Bot Backend",
    description="Backend para gestionar las interacciones del chatbot de EduConecta en WhatsApp.",
    version="1.0.0"
)

@app.get("/", tags=["Health Check"])
def read_root():
    """
    Endpoint principal para verificar que el servicio está en línea.
    """
    return {"status": "ok", "message": "EduConecta Bot is running!"}

# Incluye el router del webhook en la aplicación principal.
# Todas las rutas definidas en webhook_router ahora serán parte de la app.
app.include_router(webhook_router)