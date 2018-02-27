from django.http import JsonResponse
from ubicacion.models import CarreraInstancia, SeccionInstancia, Sede, UnidadInstancia, Unidad, Seccion, Carrera


def get_sedes(request):
    sedes = Sede.objects.all().values()
    sedes_list = list(sedes)
    return JsonResponse(sedes_list, safe=False)


def get_facultades(request):
    facultades = Unidad.objects.all().values()
    lista = list(facultades)
    return JsonResponse(lista, safe=False)


def get_escuelas(request):
    escuelas = Seccion.objects.filter(tipo='ES').values()
    lista = list(escuelas)
    return JsonResponse(lista, safe=False)


def get_departamentos(request):
    escuelas = Seccion.objects.filter(tipo='DE').values()
    lista = list(escuelas)
    return JsonResponse(lista, safe=False)


def get_carreras(request):
    carreras = Carrera.objects.all().values()
    lista = list(carreras)
    return JsonResponse(lista, safe=False)

def get_fac_ubc(request):
    fac_ubc = UnidadInstancia.objects.all().values()
    lista = list(fac_ubc)
    return JsonResponse(lista)
