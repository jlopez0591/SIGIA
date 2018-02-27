from django.http import JsonResponse
from ubicacion.models import CarreraInstancia, SeccionInstancia, Sede, UnidadInstancia


def profesores_sede(request, sede_pk):
    """
    Devuelve el numero de profesores por facultad
    :param request:
    :return:
    """
    sede = Sede.objects.get(pk=sede_pk)
    profesores = sede.personal.profesores()
    conteo = {}
    for profesor in profesores:
        cs = profesor.cod_sede
        cf = profesor.cod_unidad
        facultad = UnidadInstancia.objects.get(cod_sede=cs, cod_unidad=cf)
        ubicacion = facultad.unidad.nombre
        if ubicacion in conteo:
            conteo[ubicacion] += 1
        else:
            conteo[ubicacion] = 1
    return JsonResponse(conteo)


def estudiantes_sede(request, sede_pk):
    """
    Devuelve el numero de estudiantes por facultad
    :param request:
    :return:
    """
    sede = Sede.objects.get(pk=sede_pk)
    estudiantes = sede.estudiantes.all()
    conteo = {}
    for estudiante in estudiantes:
        cs = estudiante.cod_sede
        cf = estudiante.cod_facultad  # Codigo de Facultad
        nombre_facultad = UnidadInstancia.objects.get(cod_sede=cs, cod_unidad=cf).unidad.nombre.title()
        if nombre_facultad in conteo:
            conteo[nombre_facultad] += 1
        else:
            conteo[nombre_facultad] = 1
    return JsonResponse(conteo)


# Unidades

# Escuelas
def estudiantes_semestre_escuela(request, escuela_pk):
    """
    Regresa el numero de estudiantes en la escuela separados por semestre
    :param request:
    :param escuela_pk:
    :return:
    """
    escuela = SeccionInstancia.objects.get(pk=escuela_pk)
    pass


def proyectos_semestre_escuela(request, escuela_pk):
    escuela = SeccionInstancia.objects.get(pk=escuela_pk)
    pass


def anteproyectos_semestre_escuela(request, escuela_pk):
    escuela = SeccionInstancia.objects.get(pk=escuela_pk)
    pass


# Departamentos
def profesores_nivel(request, departamento_pk):
    departamento = SeccionInstancia.objects.get(pk=departamento_pk)
    pass


def actividades_tipo(request, departamento_pk):
    departamento = SeccionInstancia.objects.get(pk=departamento_pk)
    pass


def actividades_realizadas(request, departamento_pk):
    departamento = SeccionInstancia.objects.get(pk=departamento_pk)
    pass


# Carreras
def estudiantes_semestre_carrera(request, carrera_pk):
    carrera = CarreraInstancia.objects.get(pk=carrera_pk)
    pass


def proyectos_semestre_carrera(request, carrera_pk):
    carrera = CarreraInstancia.objects.get(pk=carrera_pk)
    pass


def anteproyectos_semestre_carrera(request, carrera_pk):
    carrera = CarreraInstancia.objects.get(pk=carrera_pk)
    pass
