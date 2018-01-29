from django.http import JsonResponse
from inventario.models import Aula, Categoria, Fabricante, Modelo, Equipo


def categorias_json(request):
    categorias = Categoria.objects.all().values().order_by('pk')
    lista = list(categorias)
    return JsonResponse(lista, safe=False)


def fabricantes_json(request):
    fabricantes = Fabricante.objects.all().values().order_by('pk')
    lista = list(fabricantes)
    return JsonResponse(lista, safe=False)


def modelos_json(request):
    modelos = Modelo.objects.all().values().order_by('pk')
    lista = list(modelos)
    return JsonResponse(lista, safe=False)


def aulas_json(request):
    aulas = Aula.objects.all().values().order_by('pk')
    lista = list(aulas)
    return JsonResponse(lista, safe=False)


def equipos_json(request):
    equipos = Equipo.objects.all().values().order_by('pk')
    lista = list(equipos)
    return JsonResponse(lista, safe=False)
