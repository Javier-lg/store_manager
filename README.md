# Store Manager

Este proyecto es una aplicación de administración de tiendas creada con Django.

## Estructura del proyecto

El proyecto está organizado de la siguiente manera:

* `apps`: Esta carpeta contiene todas las aplicaciones del proyecto.
* `migrations`: Esta carpeta contiene los archivos de migración que se utilizan para realizar cambios en la base de datos del proyecto.
* `settings.py`: Este archivo contiene la configuración del proyecto, como la configuración de la base de datos, las variables de entorno y las configuraciones de seguridad.
* `urls.py`: Este archivo contiene las URL del proyecto.
* `wsgi.py`: Este archivo contiene el punto de entrada de la aplicación web.

Además de estas carpetas, el proyecto también puede contener las siguientes carpetas:

* `media`: Esta carpeta contiene los archivos multimedia del proyecto, como imágenes, videos y archivos de audio.
* `static`: Esta carpeta contiene los archivos estáticos del proyecto, como CSS, JavaScript y archivos de imágenes.
* `templates`: Esta carpeta contiene las plantillas del proyecto.

## Instalación

Para instalar el proyecto, siga estos pasos:

1. Clone el proyecto desde GitHub:

```
https://github.com/Javier-lg/store_manager.git
```

2. Crea un entorno virtual y activalo:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

3. Instala las dependencias del proyecto:

```
pip install -r requirements.txt
```

4. Migra la base de datos:

```
python store_manager/manage.py makemigrations
python store_manager/manage.py migrate
```

5. Inicia la aplicación web:

```
python store_manager/manage.py runserver
```

## Uso

Para usar la aplicación web, abra un navegador y vaya a la siguiente dirección:

```
http://localhost:8000
```

## Documentación

La documentación del proyecto se encuentra en el siguiente directorio:

```
docs/
```
```

## Autores

Este proyecto fue creado por:

* Javier-lg

## Licencia

