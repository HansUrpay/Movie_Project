# Pasos para deploy
## 1. Instalamos dependencias 

```bash
pip install gunicorn

pip install django-environ
```

## 2. Creamos nuestro requeriments

```bash
pip freeze > requirements.txt
```

## 3. Creamos nuestro Procfile

```bash
web: python manage.py migrate && gunicorn movie.wsgi
```

## 4. Creamos nuestra base de datos en Railway
Estamos usando mysql por defecto

[railway.app](https://railway.app)

## 5. Configuramos las variables de entorno
```python
DB_NAME=''
DB_USER=''
DB_PASSWORD=''
DB_HOST=''
DB_PORT=''
```

## 6. Configuramos nuestro dominio
Para que el proyecto pueda ser accedido desde un dominio, debemos configurar el dominio en Railway y en nuestro proyecto

```python
ALLOWED_HOST = ["domain.railway.app"]
```

## 7. Configuramos nuestros archivos estáticos
```bash

```