# DataGovRD - Módulo de API

Este módulo implementa la API utilizando FastApi para el proyecto DataGovRD.

## Requisitos

- Python 3.x
- Entorno virtual (virtualenv)
- Paquetes requeridos (ver `requirements.txt`)

## Instalación

1. Clonar el repositorio de datagovrd:

   ```shell
   git clone git@github.com:Open-CD/datagovrd.git
   ```

2. Crear un entorno virtual:

   ```shell
   python -m venv venv
   ```

3. Activar entorno virtual:

   - Para macOS
     ```shell
     source venv/bin/activate
     ```
   - Para windows
     ```shell
     venv/Scripts/activate
     ```

4. Instalar los paquetes requeridos:

   ```shell
   pip install -r requirements.txt
   ```

## Ejecutar el proyecto

Ejecutar el servidor de desarrollo:

```shell
uvicorn main:app --reload
```

La API estará accesible en `http://localhost:8000/`.

## Documentación de la API

Puedes consultar la documentación de la API en `http://localhost:8000/docs`:

## Estructura de archivos y directorios del módulo

- `app/`: Directorio que contiene el código de la API y configuraciones necesarias.
  - `api/`: Módulos relacionados con la definición de la API.
  - `controllers/`: Controladores que manejan la lógica de la aplicación.
  - `services/`: Servicios que realizan operaciones específicas.
  - `utils/`: Utilidades y funciones auxiliares.
- `notebooks/`: Directorio para cuadernos de Jupyter u otros documentos relacionados.
- `.env`: Archivo de configuración del entorno.
- `.env.example`: Ejemplo de archivo de configuración del entorno.
- `.gitignore`: Archivo para especificar archivos y carpetas ignorados por Git.
- `main.py`: Punto de entrada principal de la aplicación.
- `README.MD`: Documentación principal del proyecto.
- `requirements.txt`: Lista de paquetes Python requeridos por el proyecto.

## Tecnologías Utilizadas

Este proyecto utiliza FastApi, un marco web rápido para construir API con Python 3. Además, se emplea Python 3.x y un entorno virtual para gestionar las dependencias del proyecto.

## Contacto

Si tienes alguna pregunta o sugerencia con respecto al módulo de API de DataGovRD, no dudes en ponerte en contacto con nosotros:

- Nombre: [OpenCD]
- Correo electrónico: [opencdfree@gmail.com]
