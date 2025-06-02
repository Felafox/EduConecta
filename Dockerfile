# Usa una imagen base oficial de Python. La versión 'slim' es más ligera. [cite: 619]
FROM python:3.12-slim

# Establece el directorio de trabajo dentro del contenedor. [cite: 620]
WORKDIR /app

# Copia el archivo de dependencias primero para aprovechar el cacheo de Docker. [cite: 621]
COPY requirements.txt .
# Instala las dependencias de Python. [cite: 623]
# --no-cache-dir reduce el tamaño de la imagen. [cite: 623]
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación al directorio de trabajo. [cite: 624, 625]
COPY . .

# Expone el puerto en el que la aplicación se ejecutará. [cite: 650]
# Railway detectará esto, pero es una buena práctica documentarlo. [cite: 650]
EXPOSE 8080

# El comando para ejecutar la aplicación cuando el contenedor se inicie. [cite: 626]
# Uvicorn es un servidor ASGI de alto rendimiento. [cite: 651]
# --host 0.0.0.0 hace que el servidor sea accesible desde fuera del contenedor. [cite: 627, 652]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]