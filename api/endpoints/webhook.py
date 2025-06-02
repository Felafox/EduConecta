import logging
from fastapi import APIRouter, Request, Header, Query, HTTPException, Response

# Configuración básica de logging para ver qué está pasando
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# NOTA: Este token será gestionado de forma segura en la Tarea COM-04.
# Por ahora, lo definimos aquí para que el endpoint funcione.
VERIFY_TOKEN = "una_clave_secreta_para_educonecta" 

webhook_router = APIRouter()

@webhook_router.get("/webhook", tags=["WhatsApp"])
def verify_webhook(
    mode: str = Query(..., alias="hub.mode"),
    token: str = Query(..., alias="hub.verify_token"),
    challenge: str = Query(..., alias="hub.challenge"),
):
    """
    Verifica el webhook con la API de WhatsApp.
    Meta envía una petición GET a esta URL para confirmar su autenticidad.
    """
    logger.info(f"Verificación de Webhook recibida: mode={mode}, token={token}")
    if mode == "subscribe" and token == VERIFY_TOKEN:
        logger.info("Verificación de Webhook exitosa.")
        return Response(content=challenge, media_type="text/plain", status_code=200)
    else:
        logger.error("Fallo en la verificación del Webhook. Tokens no coinciden.")
        raise HTTPException(status_code=403, detail="Error de verificación de token")

@webhook_router.post("/webhook", tags=["WhatsApp"])
async def receive_message(request: Request):
    """
    Recibe notificaciones de mensajes entrantes desde WhatsApp.
    Esta función pasará el payload al procesador de mensajes (COM-05).
    """
    payload = await request.json()
    logger.info(f"Mensaje recibido: {payload}")

    # TODO: Aquí irá la llamada al procesador de mensajes (Tarea COM-05)

    # Responde inmediatamente con un 200 OK a WhatsApp para confirmar la recepción.
    return Response(status_code=200)