import logging
from fastapi import APIRouter, Request, Header, Query, HTTPException, Response

# Importamos la instancia de configuración centralizada
from core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Se eliminó la variable VERIFY_TOKEN de aquí

webhook_router = APIRouter()

@webhook_router.get("/webhook", tags=["WhatsApp"])
def verify_webhook(
    mode: str = Query(..., alias="hub.mode"),
    token: str = Query(..., alias="hub.verify_token"),
    challenge: str = Query(..., alias="hub.challenge"),
):
    """
    Verifica el webhook con la API de WhatsApp.
    Usa el VERIFY_TOKEN desde la configuración centralizada.
    """
    logger.info(f"Verificación de Webhook recibida: mode={mode}")
    # Ahora usamos settings.VERIFY_TOKEN en lugar de la variable local
    if mode == "subscribe" and token == settings.VERIFY_TOKEN:
        logger.info("Verificación de Webhook exitosa.")
        return Response(content=challenge, media_type="text/plain", status_code=200)
    else:
        logger.error("Fallo en la verificación del Webhook. Tokens no coinciden.")
        raise HTTPException(status_code=403, detail="Error de verificación de token")

@webhook_router.post("/webhook", tags=["WhatsApp"])
async def receive_message(request: Request):
    """
    Recibe notificaciones de mensajes entrantes desde WhatsApp.
    """
    payload = await request.json()
    logger.info(f"Mensaje recibido: {payload}")

    # TODO: Llamada al procesador de mensajes (Tarea COM-05)

    return Response(status_code=200)