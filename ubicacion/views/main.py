from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
from ubicacion.models import CarreraInstancia, SeccionInstancia, Sede, UnidadInstancia


def consulta_sede(request):
    sedes = Sede.objects.activas().order_by('cod_sede')
    return render(request, 'ubicacion/consulta/sede.html', {
        'sedes': sedes
    })


def consulta_unidad(request):
    facultades = UnidadInstancia.objects.activas().order_by('cod_sede', 'cod_facultad')
    return render(request, 'ubicacion/consulta/facultad.html', {
        'facultades': facultades
    })


def consulta_seccion(request):
    secciones = SeccionInstancia.objects.activas().order_by('cod_sede', 'cod_facultad', 'cod_escuela')
    return render(request, 'ubicacion/consulta/escuela.html', {
        'secciones': secciones
    })


def consulta_carrera(request):
    carreras = CarreraInstancia.objects.activas().order_by('cod_sede', 'cod_facultad', 'cod_escuela', 'cod_carrera')
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
        unidad = self.kwargs['cod_facultad']
        return get_object_or_404(UnidadInstancia, cod_sede=sede,
                                 cod_facultad=unidad)


def detalle_seccion(request, cod_sede, cod_facultad, cod_escuela):
    seccion = get_object_or_404(SeccionInstancia, cod_sede=cod_sede, cod_facultad=cod_facultad, cod_escuela=cod_escuela)
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
        unidad = self.kwargs['cod_facultad']
        seccion = self.kwargs['cod_escuela']
        carrera = self.kwargs['cod_carrera']
        return get_object_or_404(CarreraInstancia, cod_sede=sede, cod_facultad=unidad, cod_escuela=seccion,
                                 cod_carrera=carrera)
