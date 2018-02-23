# Plataforma SIGIA para la Universidad de Panama

El sistema de gestion de informacion academica/administrativa (SIGIA) es una plataforma la cual 
pretende proveer un conjunto de aplicaciones para agilizar y facilitar varias de las acciones que se
realizan dentro de las unidades academicas de la universidad.

Entre las acciones que se pretenden implementar se tienen las siguientes:

### Modulo de Profesores
Entre las funcionalidades que este modulo le brinadara a los profesores se tienen las siguientes:

1. Presentarles un perfil con el cual podran mantener sus datos al dia.
1. Registro de actividades realizadas
1. Panel para aprobacion de actividades realizadas (Para los directores de departamento)
1. Imprimir reporte/hoja de vida de los profesores (disponible solo para el profesor al cual pertenece el informe)

### Modulo de Estudiantes

1. Presentar el perfil de los estudiantes y la posibilidad de actualizar los datos de los mismos
1. Registro de anteproyecto
1. Aprobacion de anteproyecto
1. Registro de trabajos de graduacion

### Modulo de Inventario

1. Registro del inventario de las facultades por salon en el que se encuentra.

### Reportes

Utilizando los datos existentes y recolectados por el sistema este proveera de reportes basicos y puntuales
de:

1. Facultades
1. Escuelas
1. Departamentos


# Requerimientos

1. PostgreSQL 9.5.2
1. Nginx
1. Python 3.5.2
1. Django 1.11.8
1. Ver archivo Pipfile

# Setup inicial
## Ejecutar los siguientes comandos administrativos (manage.py)
1. makemigrations
1. migrate
1. crear_grupos
1. createsuperuser

#### Views
1. Include list unapproved activities view.
1. Include rejected activities view.
1. Include rejected anteproyecto view.
1. Terminar las plantillas.
1. Terminar los metodos de django-autocomplete-light
1. Agregar graficas de unidades
1. Generar reportes personalizados (Utilizando la reportlab o weasyprint o wkhtmltopdf)
1. Implementar documentacion con sphinx

### Cron Jobs
Entre los cron jobs que se utilizaran para mantener actualizado los datos se utilizaran los siguientes comandos administrativos
1. cargar_ubicaciones
1. cargar_estudiantes

# To-Do - Durante pruebas
1. Restringir el acceso a vistas
1. Completar la asignacion de permisos
1. Completar la mesa de ayuda
