# Proyecto FastAPI - Envío de Contacto

Este proyecto es una API construida con FastAPI para gestionar el envío de información de contacto.

## Pasos para ejecutar el proyecto

1. Abre una terminal en la carpeta raíz del proyecto.

2. Activa el entorno virtual ejecutando:

```bash
.venv\Scripts\activate
```

3. Inicia el servidor con el siguiente comando:

```bash
uvicorn src.main:app --reload --port 8000
```

4. Abre tu navegador y accede a la siguiente URL para visualizar la documentación interactiva de la API:

```
http://127.0.0.1:8000/docs
```

5. En la interfaz de Swagger, prueba el endpoint para crear un nuevo contacto.

> ⚠️ Importante: si usas el correo `contactobloqueado`, el sistema lo reconocerá como bloqueado y no permitirá el registro.
