from django.http import JsonResponse
from ubicacion.models import CarreraInstancia, EscuelaInstancia, Sede, FacultadInstancia, Facultad, Escuela, Carrera


def get_sedes(request):
    sedes = Sede.objects.all().values()
    sedes_list = list(sedes)
    return JsonResponse(sedes_list, safe=False)


def get_facultades(request):
    facultades = Facultad.objects.all().values()
    lista = list(facultades)
    return JsonResponse(lista, safe=False)


def get_escuelas(request):
    escuelas = Escuela.objects.filter(tipo='ES').values()
    lista = list(escuelas)
    return JsonResponse(lista, safe=False)


def get_departamentos(request):
    escuelas = Escuela.objects.filter(tipo='DE').values()
    lista = list(escuelas)
    return JsonResponse(lista, safe=False)


def get_carreras(request):
    carreras = Carrera.objects.all().values()
    lista = list(carreras)
    return JsonResponse(lista, safe=False)

def get_fac_ubc(request):
    fac_ubc = FacultadInstancia.objects.all().values()
    lista = list(fac_ubc)
    return JsonResponse(lista)
