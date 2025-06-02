import logging
from fastapi import APIRouter, Request, Response, BackgroundTasks

from core.config import settings
# Importamos nuestro nuevo procesador de mensajes
from services.message_processor import process_whatsapp_message

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

webhook_router = APIRouter()

# ... (El endpoint GET se mantiene igual) ...
@webhook_router.get("/webhook", tags=["WhatsApp"])
def verify_webhook(
    mode: str,
    token: str,
    challenge: str,
):
    if mode == "subscribe" and token == settings.VERIFY_TOKEN:
        return Response(content=challenge, media_type="text/plain", status_code=200)
    return Response(status_code=403)

@webhook_router.post("/webhook", tags=["WhatsApp"])
async def receive_message(request: Request, background_tasks: BackgroundTasks):
    """
    Recibe notificaciones de mensajes entrantes desde WhatsApp.
    Usa BackgroundTasks para procesar el mensaje sin bloquear la respuesta. [cite: 765]
    """
    payload = await request.json()
    logger.info(f"Payload recibido: {payload}")

    # Añadimos la tarea de procesamiento a un segundo plano.
    # Esto permite que devolvamos un 200 OK a WhatsApp inmediatamente,
    # una práctica recomendada para la robustez del webhook. [cite: 754, 766]
    background_tasks.add_task(process_whatsapp_message, payload)

    return Response(status_code=200)