from dal import autocomplete
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
# from ubicacion.filters import (CarreraFilter, SeccionFilter, SedeFilter,
#                                UnidadFilter)
from ubicacion.models import CarreraInstancia, SeccionInstancia, Sede, UnidadInstancia, Unidad, Seccion, Carrera


def consulta_sede(request):
    sedes = Sede.objects.activas().order_by('cod_sede')
    return render(request, 'ubicacion/consulta/sede.html', {
        'sedes': sedes
    })


def consulta_unidad(request):
    unidades = UnidadInstancia.objects.activas().order_by('cod_sede', 'cod_unidad')
    return render(request, 'ubicacion/consulta/facultad.html', {
        'unidades': unidades
    })


def consulta_seccion(request):
    secciones = SeccionInstancia.objects.activas().order_by('cod_sede', 'cod_unidad', 'cod_seccion')
    return render(request, 'ubicacion/consulta/escuela.html', {
        'secciones': secciones
    })


def consulta_carrera(request):
    carreras = CarreraInstancia.objects.activas().order_by('cod_sede', 'cod_unidad', 'cod_seccion', 'cod_carrera')
    return render(request, 'ubicacion/consulta/carrera.html', {
        'carreras': carreras
    })


class SedeDetailView(DetailView):
    model = Sede
    context_object_name = 'sede'
    template_name = 'ubicacion/sede.html'

    def get_object(self, queryset=None):
        cod_sede = self.kwargs['cod_sede']
        return get_object_or_404(Sede, cod_sede=cod_sede)


class UnidadDetailView(DetailView):
    model = UnidadInstancia
    context_object_name = 'unidad'
    template_name = 'ubicacion/facultad.html'

    def get_object(self, queryset=None):
        sede = self.kwargs['cod_sede']
        unidad = self.kwargs['cod_unidad']
        return get_object_or_404(UnidadInstancia, cod_sede=sede,
                                 cod_unidad=unidad)


def detalle_seccion(request, cod_sede, cod_facultad, cod_escuela):
    seccion = get_object_or_404(SeccionInstancia, cod_sede=cod_sede, cod_unidad=cod_facultad, cod_seccion=cod_escuela)
    if seccion.seccion.tipo == 'ES':
        plantilla = 'ubicacion/escuela.html'
    else:
        plantilla = 'ubicacion/departamento.html'
    context = {'seccion': seccion}
    return render(request, plantilla, context)


class CarreraDetailView(DetailView):
    model = CarreraInstancia
    context_object_name = 'carrera'
    template_name = 'ubicacion/carrera.html'

    def get_object(self, queryset=None):
        sede = self.kwargs['cod_sede']
        unidad = self.kwargs['cod_unidad']
        seccion = self.kwargs['cod_seccion']
        carrera = self.kwargs['cod_carrera']
        return get_object_or_404(CarreraInstancia, cod_sede=sede, cod_unidad=unidad, cod_seccion=seccion,
                                 cod_carrera=carrera)


class CarreraInstanciaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if self.request.user.is_superuser:
            qs = CarreraInstancia.objects.all()
        elif self.request.user.is_authenticated():
            qs = CarreraInstancia.objects.all()
        else:
            return CarreraInstancia.objects.none()

        if self.q:
            qs = qs.filter(nombre_proyecto__icontains=self.q)
        return qs


def get_sedes(request):
    sedes = Sede.objects.all().values()  # or simply .values() to get all fields
    sedes_list = list(sedes)  # important: convert the QuerySet to a list object
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
