from django.http import JsonResponse
from ubicacion.models import CarreraInstancia, EscuelaInstancia, Sede, FacultadInstancia


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
        cf = profesor.cod_facultad
        facultad = FacultadInstancia.objects.get(cod_sede=cs, cod_facultad=cf)
        ubicacion = facultad.facultad.nombre
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
        nombre_facultad = FacultadInstancia.objects.get(cod_sede=cs, cod_facultad=cf).facultad.nombre.title()
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
    :return: Objeto JSON con el conteo por semestre de estudiantes en la escuela.
    """
    escuela = EscuelaInstancia.objects.get(pk=escuela_pk)
    estudiantes = escuela.estudiantes.all()
    conteo = dict()
    for estudiante in estudiantes:
        semestre = estudiante.ultimo_semestre
        if semestre in conteo:
            conteo[semestre] += 1
        else:
            conteo[semestre] = 1
    return JsonResponse(conteo)


def proyectos_semestre_escuela(request, escuela_pk):
    escuela = EscuelaInstancia.objects.get(pk=escuela_pk)
    conteo = dict()
    proyectos = escuela.proyectos.all()
    for proyecto in proyectos:
        programa = proyecto.programa
        if programa in conteo:
            conteo[programa] += 1
        else:
            conteo[programa] = 1
    return JsonResponse(conteo)


def anteproyectos_semestre_escuela(request, escuela_pk):
    escuela = EscuelaInstancia.objects.get(pk=escuela_pk)
    conteo = dict()
    conteo['aprobados'] = escuela.anteproyectos.aprobados().count()
    conteo['rechazados'] = escuela.anteproyectos.rechazados().count()
    conteo['pendientes'] = escuela.anteproyectos.pendientes().count()
    return JsonResponse(conteo)


# Departamentos
def profesores_nivel(request, departamento_pk):
    departamento = EscuelaInstancia.objects.get(pk=departamento_pk)
    profesores = departamento.personal.profesores()
    conteo = dict()
    for profesor in profesores:
        conteo = registrar_conteo(conteo, profesor.nivel_academico())
    return JsonResponse(conteo)


def actividades_tipo(request, departamento_pk):
    """
    Regresa el conteo de las actividades de un departamento por categoria
    :param request:
    :param departamento_pk: Llave primaria del departamento
    :return: Conteo de las actividades
    """
    departamento = EscuelaInstancia.objects.get(pk=departamento_pk)
    actividades = departamento.actividades.aprobado().actuales()
    conteo = dict()
    for actividad in actividades:
        conteo = registrar_conteo(conteo, actividad.clase)
    return JsonResponse(conteo)


# Carrera
def estudiantes_semestre_carrera(request, carrera_pk):
    carrera = CarreraInstancia.objects.get(pk=carrera_pk)
    estudiantes = carrera.estudiantes.all()
    conteo = dict()
    for estudiante in estudiantes:
        conteo = registrar_conteo(conteo, estudiante.ultimo_semestre)
    return JsonResponse(conteo)


def proyectos_semestre_carrera(request, carrera_pk):
    carrera = CarreraInstancia.objects.get(pk=carrera_pk)
    proyectos = carrera.proyectos.all()
    conteo = dict()
    for proyecto in proyectos:
        conteo = registrar_conteo(diccionario=conteo, clave=proyecto.programa)
    return JsonResponse(conteo)


def anteproyectos_semestre_carrera(request, carrera_pk):
    """
    Regresa un objeto JSON con el conteo por estado de los anteproyectos de una carrera
    :param request:
    :param carrera_pk: Llave primaria de la carrera
    :return: Objeto JSON con conteo por estado de anteproyecto.
    """
    carrera = CarreraInstancia.objects.get(pk=carrera_pk)
    anteproyectos = carrera.anteproyectos.all()
    conteo = dict()
    for anteproyecto in anteproyectos:
        conteo = registrar_conteo(conteo, anteproyecto.estado)
    return JsonResponse(conteo)


def registrar_conteo(diccionario, clave):
    """
    Registra el conteo de la vista.
    :param diccionario:
    :param clave:
    :return: Diccionario con el conteo deseado.
    """
    if clave in diccionario:
        diccionario[clave] += 1
    else:
        diccionario[clave] = 1
    return diccionario
