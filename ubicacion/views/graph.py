from django.http import JsonResponse
from ubicacion.models import CarreraInstancia, EscuelaInstancia, Sede, FacultadInstancia, DepartamentoInstancia

# Sede
def profesores_sede(request, sede_pk):
    sede = Sede.objects.get(pk=sede_pk)
    profesores = sede.personal.profesores()
    conteo = {}
    for profesor in profesores:
        cs = profesor.cod_sede
        cf = profesor.cod_facultad
        facultad = FacultadInstancia.objects.get(cod_sede=cs, cod_facultad=cf)
        ubicacion = facultad.facultad.nombre.title()
        if ubicacion in conteo:
            conteo[ubicacion] += 1
        else:
            conteo[ubicacion] = 1
    return JsonResponse(conteo)


def estudiantes_sede(request, sede_pk):
    sede = Sede.objects.get(pk=sede_pk)
    estudiantes = sede.estudiantes.activos()
    conteo = {}
    for estudiante in estudiantes:
        cs = estudiante.cod_sede
        cf = estudiante.cod_facultad  # Codigo de Facultad
        nombre_facultad = FacultadInstancia.objects.get(
            cod_sede=cs, cod_facultad=cf).facultad.nombre.title()
        if nombre_facultad in conteo:
            conteo[nombre_facultad] += 1
        else:
            conteo[nombre_facultad] = 1
    return JsonResponse(conteo)

# Facultad
def facultad_recursos_categoria(request, facultad_pk):
    facultad = FacultadInstancia.objects.get(pk=facultad_pk)
    inventario = facultad.equipos.all()
    conteo = dict()
    for equipo in inventario:
        categoria = equipo.modelo.categoria.nombre
        if categoria in conteo:
            conteo[categoria] += 1
        else:
            conteo[categoria] = 1
    return JsonResponse(conteo)


def facultad_aulas_tipo(request, facultad_pk):
    facultad = FacultadInstancia.objects.get(pk=facultad_pk)
    aulas = facultad.aula_set.all()
    conteo = dict()
    for aula in aulas:
        tipo = aula.get_tipo_display()
        if tipo in conteo:
            conteo[tipo] += 1
        else:
            conteo[tipo] = 1
    return JsonResponse(conteo)


# Escuela
def estudiantes_semestre_escuela(request, escuela_pk):
    """
    Regresa el numero de estudiantes en la escuela separados por semestre
    :param request:
    :param escuela_pk:
    :return: Objeto JSON con el conteo por semestre de estudiantes en la escuela.
    """
    escuela = EscuelaInstancia.objects.get(pk=escuela_pk)
    estudiantes = escuela.estudiantes.activos()
    conteo = dict()
    for estudiante in estudiantes:
        semestre = estudiante.get_semestre_display()
        if semestre in conteo:
            conteo[semestre] += 1
        else:
            conteo[semestre] = 1
    return JsonResponse(conteo)


def proyectos_semestre_escuela(request, escuela_pk):
    escuela = EscuelaInstancia.objects.get(pk=escuela_pk)
    conteo = dict()
    proyectos = escuela.trabajos_graduacion.all()
    for proyecto in proyectos:
        programa = proyecto.get_estado_display()
        if programa in conteo:
            conteo[programa] += 1
        else:
            conteo[programa] = 1
    return JsonResponse(conteo)


def proyectos_finales_categoria_escuela(request, escuela_pk):
    escuela = EscuelaInstancia.objects.get(pk=escuela_pk)
    conteo = dict()
    conteo['Licenciatura'] = escuela.trabajos_graduacion.licenciatura().sustentados().count()
    conteo['Especializacion'] = escuela.trabajos_graduacion.especializacion().sustentados().count()
    conteo['Maestria'] = escuela.trabajos_graduacion.maestria().sustentados().count()
    conteo['Doctorado'] = escuela.trabajos_graduacion.doctorado().sustentados().count()
    return JsonResponse(conteo)



# Departamento
def profesores_nivel(request, departamento_pk):
    departamento = DepartamentoInstancia.objects.get(pk=departamento_pk)
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
    departamento = DepartamentoInstancia.objects.get(pk=departamento_pk)
    actividades = departamento.actividades.aprobado().actuales()
    conteo = dict()
    for actividad in actividades:
        conteo = registrar_conteo(conteo, actividad.get_clase_display())
    return JsonResponse(conteo)


def actividades_estado(request, departamento_pk):
    """
    Regresa el conteo de las actividades de un departamento por categoria
    :param request:
    :param departamento_pk: Llave primaria del departamento
    :return: Conteo de las actividades
    """
    departamento = DepartamentoInstancia.objects.get(pk=departamento_pk)
    actividades = departamento.actividades.actuales()
    conteo = dict()
    for actividad in actividades:
        conteo = registrar_conteo(conteo, actividad.get_estado_display())
    return JsonResponse(conteo)


# Carrera
def estudiantes_semestre_carrera(request, carrera_pk):
    carrera = CarreraInstancia.objects.get(pk=carrera_pk)
    estudiantes = carrera.estudiantes.activos()
    conteo = dict()
    for estudiante in estudiantes:
        conteo = registrar_conteo(conteo, estudiante.get_semestre_display())
    return JsonResponse(conteo)


def proyectos_carrera_categoria(request, carrera_pk):
    carrera = CarreraInstancia.objects.get(pk=carrera_pk)
    proyectos = carrera.trabajos_graduacion.all()
    conteo = dict()
    for proyecto in proyectos:
        conteo = registrar_conteo(diccionario=conteo, clave=proyecto.get_programa_display())
    return JsonResponse(conteo)


def proyecto_carrera_estado(request, carrera_pk):
    """
    Regresa un objeto JSON con el conteo por estado de los anteproyectos de una carrera
    :param request:
    :param carrera_pk: Llave primaria de la carrera
    :return: Objeto JSON con conteo por estado de anteproyecto.
    """
    carrera = CarreraInstancia.objects.get(pk=carrera_pk)
    anteproyectos = carrera.trabajos_graduacion.all()
    conteo = dict()
    for anteproyecto in anteproyectos:
        conteo = registrar_conteo(conteo, anteproyecto.get_estado_display())
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
