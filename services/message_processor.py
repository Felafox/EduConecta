import logging

# Configuración básica de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_whatsapp_message(payload: dict):
    """
    Analiza el payload entrante de WhatsApp y dirige el mensaje
    al manejador de lógica correspondiente.
    """
    try:
        # Extrae la información relevante del payload
        change = payload['entry'][0]['changes'][0]
        if 'messages' not in change['value']:
            logger.info("El payload no contiene mensajes (ej. es una actualización de estado).")
            return

        message_data = change['value']['messages'][0]
        wa_id = message_data['from']
        message_type = message_data['type']

        logger.info(f"Procesando mensaje de {wa_id} del tipo '{message_type}'")

        # Enrutamiento basado en el tipo de mensaje
        if message_type == 'text':
            text_content = message_data['text']['body']
            handle_text_message(wa_id, text_content)
        elif message_type == 'interactive':
            interactive_data = message_data['interactive']
            handle_interactive_message(wa_id, interactive_data)
        else:
            logger.warning(f"Tipo de mensaje '{message_type}' no soportado todavía.")

    except (KeyError, IndexError) as e:
        logger.error(f"Error al procesar el payload de WhatsApp: {e}\nPayload: {payload}")

def handle_text_message(wa_id: str, text: str):
    """
    Manejador para mensajes de texto.
    """
    logger.info(f"Texto recibido de {wa_id}: '{text}'")
    # TODO: Tarea COM-06
    # Aquí se llamará al gestor de conversación:
    # conversation_manager.handle_message(wa_id=wa_id, content=text, type='text')

def handle_interactive_message(wa_id: str, interactive_data: dict):
    """
    Manejador para mensajes interactivos (botones, listas).
    """
    interaction_type = interactive_data.get('type')
    if interaction_type == 'button_reply':
        button_id = interactive_data['button_reply']['id']
        logger.info(f"Botón presionado por {wa_id}: '{button_id}'")
        # TODO: Tarea COM-06
        # conversation_manager.handle_message(wa_id=wa_id, content=button_id, type='button')
    elif interaction_type == 'list_reply':
        list_reply_id = interactive_data['list_reply']['id']
        logger.info(f"Opción de lista seleccionada por {wa_id}: '{list_reply_id}'")
        # TODO: Tarea COM-06
        # conversation_manager.handle_message(wa_id=wa_id, content=list_reply_id, type='list')
    else:
        logger.warning(f"Tipo de interacción no soportada: {interaction_type}")