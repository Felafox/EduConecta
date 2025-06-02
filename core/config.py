from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Clase para gestionar la configuración de la aplicación.
    Carga las variables de entorno desde un archivo .env y del sistema.
    """
    # Configuración para pydantic-settings
    model_config = SettingsConfigDict(
        env_file=".env",          # Nombre del archivo de donde leer las variables
        env_file_encoding="utf-8", # Codificación del archivo
        case_sensitive=False,      # No distingue entre mayúsculas y minúsculas
    )

    # Variables de entorno requeridas
    WHATSAPP_API_TOKEN: str
    VERIFY_TOKEN: str

    # Variables opcionales con valores por defecto
    PROJECT_NAME: str = "EduConecta Bot"
    API_V1_STR: str = "/api/v1"

# Se crea una única instancia de la configuración que será importada
# por el resto de la aplicación.
settings = Settings()