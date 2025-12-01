# BMTH Shop – Backend (Django + Railway)

Este repositorio contiene el backend del proyecto de tienda Bring Me The Horizon, desarrollado con **Django** y pensado para deploy en **Railway**.

## 📁 Estructura principal

- `manage.py` – Script principal de Django.
- `bmthshop/` – Configuración del proyecto (settings, urls, wsgi).
- `catalog/` – App principal del catálogo (productos, categorías, etc.).
- `requirements.txt` – Dependencias de Python para instalar en Railway.
- `.env.example` – Ejemplo de variables de entorno necesarias.

## 🚀 Deploy en Railway (servicio Python)

1. Creá un repositorio en GitHub con estos archivos.
2. En Railway:
   - **New Project → Deploy from GitHub → elegí este repo.**
3. Railway va a detectar que es un proyecto de **Python/Django**.

### 🔧 Build & Start commands sugeridos

En el servicio de Railway:

- **Build Command** (opcional, Railway a veces instala solo):
  ```bash
  pip install -r requirements.txt
  ```

- **Start Command**:
  ```bash
  gunicorn bmthshop.wsgi
  ```

Asegurate de que el **PORT** que usa Railway se pase automáticamente (Railway configura `PORT` en el entorno). En `settings.py` ya debería estar adaptado para leer ese puerto si usás `gunicorn` y `0.0.0.0` como host.

## 🔐 Variables de entorno

Basate en `.env.example` y en Railway agregá las siguientes variables en la sección **Environment**:

Ejemplo (puede variar según tu config real):

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG` (0 o 1)
- `DB_ENGINE`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`
- Cualquier otra que tu `settings.py` esté esperando.

> **Importante:** no subas un archivo `.env` real con credenciales a GitHub. Usá siempre `.env.example` como referencia.

## 🧪 Comandos útiles (local)

```bash
# Crear y activar entorno virtual (ejemplo en Linux/Mac)
python -m venv .venv
source .venv/bin/activate

# En Windows
# .venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Migraciones
python manage.py migrate

# Superusuario
python manage.py createsuperuser

# Correr servidor local
python manage.py runserver
```

Con esto tu backend queda listo para deployear en Railway y conectado al frontend mediante la API.
