# Python import

# Third party
from dal import autocomplete
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Django imports
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView

from perfiles.models import Person
# My imports
from ubicacion.filters import (CarreraFilter, SeccionFilter, SedeFilter,
                               UnidadFilter)
from ubicacion.models import CarreraInstancia, SeccionInstancia, Sede, UnidadInstancia, Unidad, Seccion, Carrera


def consulta_sede(request):
    sedes = Sede.objects.all().order_by('cod_sede')
    filter = SedeFilter(request.GET, queryset=sedes)
    paginator = Paginator(filter.qs, 10)
    page = request.GET.get('page')
    try:
        sede_p = paginator.page(page)
    except PageNotAnInteger:
        sede_p = paginator.page(1)
    except EmptyPage:
        sede_p = paginator.page(paginator.num_pages)
    return render(request, 'ubicacion/consulta/sede.html', {
        'filter': filter,
        'sedes': sede_p
    })


def consulta_unidad(request):
    unidades = UnidadInstancia.objects.all()
    filter = UnidadFilter(request.GET, queryset=unidades.order_by('cod_sede','cod_unidad'))
    paginator = Paginator(filter.qs, 10)
    page = request.GET.get('page')
    try:
        unidad_p = paginator.page(page)
    except PageNotAnInteger:
        unidad_p = paginator.page(1)
    except EmptyPage:
        unidad_p = paginator.page(paginator.num_pages)
    return render(request, 'ubicacion/consulta/facultad.html', {
        'filter': filter,
        'unidades': unidad_p
    })


def consulta_seccion(request):
    secciones = SeccionInstancia.objects.all().order_by('cod_sede', 'cod_unidad', 'cod_seccion')
    filter = SeccionFilter(request.GET, queryset=secciones)
    paginator = Paginator(filter.qs, 10)
    page = request.GET.get('page')
    try:
        seccion_p = paginator.page(page)
    except PageNotAnInteger:
        seccion_p = paginator.page(1)
    except EmptyPage:
        seccion_p = paginator.page(paginator.num_pages)
    return render(request, 'ubicacion/consulta/escuela.html', {
        'filter': filter,
        'secciones': seccion_p
    })


def consulta_carrera(request):
    carreras = CarreraInstancia.objects.all().order_by('cod_sede', 'cod_unidad', 'cod_seccion', 'cod_carrera')
    filter = CarreraFilter(request.GET, queryset=carreras)
    paginator = Paginator(filter.qs, 10)
    page = request.GET.get('page')
    try:
        carrera_p = paginator.page(page)
    except PageNotAnInteger:
        carrera_p = paginator.page(1)
    except EmptyPage:
        carrera_p = paginator.page(paginator.num_pages)
    return render(request, 'ubicacion/consulta/carrera.html', {
        'filter': filter,
        'carrers': carrera_p
    })


class SedeDetailView(DetailView):
    model = Sede
    context_object_name = 'sede'
    template_name = 'sede.html'

    def get_object(self, queryset=None):
        cod_sede = self.kwargs['cod_sede']
        return get_object_or_404(Sede, cod_sede=cod_sede)

    def get_context_data(self, **kwargs):
        context = super(SedeDetailView, self).get_context_data()
        context['prueba'] = [1, 2, 3]
        context['prueba2'] = {
            'facultad1': 5,
            'facultad2': 6,
            'facultad3': 7
        }
        return context


class UnidadDetailView(DetailView):
    model = UnidadInstancia
    context_object_name = 'unidad'
    template_name = 'facultad.html'

    def get_object(self, queryset=None):
        sede = self.kwargs['cod_sede']
        unidad = self.kwargs['cod_unidad']
        return get_object_or_404(UnidadInstancia, cod_sede=sede,
                                 cod_unidad=unidad)


def detalle_seccion(request, cs, cf, ce):
    """
    Peticion para los detalles de una seccion y regresa la plantilla apropiada.
    :param request:
    :param cs: Codigo de Sede
    :param cf: Codigo de Facultad
    :param ce: Codigo de Seccion
    :return:
    """
    seccion = SeccionInstancia.objects.get(cod_sede=cs, cod_unidad=cf, cod_seccion=ce)
    if seccion.seccion.tipo == 'ES':
        plantilla = 'ubicacion/escuela.html'
    else:
        plantilla = 'ubicacion/departamento.html'
    context = {'seccion': seccion}
    return render(request, plantilla, context)


class SeccionDetailView(DetailView):
    model = SeccionInstancia
    context_object_name = 'seccion'
    template_name = 'ubicacion/seccion/seccion.html'

    def get_object(self, queryset=None):
        sede = self.kwargs['cod_sede']
        unidad = self.kwargs['cod_unidad']
        seccion = self.kwargs['cod_seccion']
        return get_object_or_404(SeccionInstancia, cod_sede=sede, cod_unidad=unidad, cod_seccion=seccion)


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


def reporte_sede(request, pk):
    pass


class CarreraInstanciaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if self.request.user.is_superuser:
            qs = CarreraInstancia.objects.all()
        elif self.request.user.is_authenticated():
            perfil = Person.objects.get(usuario=self.request.user.pk)
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


def get_carreras(request):
    carreras = Carrera.objects.all().values()
    lista = list(carreras)
    return JsonResponse(lista, safe=False)
