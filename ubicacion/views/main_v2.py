from ubicacion.models import Sede
from ubicacion.models import Unidad
from ubicacion.models import Seccion
from ubicacion.models import Departamento
from ubicacion.models import Carrera
from ubicacion.models import UnidadInstancia
from ubicacion.models import SeccionInstancia
from ubicacion.models import DepartamentoInstancia
from ubicacion.models import CarreraInstancia

from django.views.generic import DetailView, ListView


class SedeListView(ListView):
    model = Sede
    context_object_name = 'sedes'


class SedeDetailView(DetailView):
    model = Sede
    context_object_name = 'sede'


class FacultadListView(ListView):
    model = Unidad
    context_object_name = 'facultades'


class FacultadDetailView(DetailView):
    model = Unidad
    context_object_name = 'facultad'


class SeccionListView(ListView):
    model = Seccion
    context_object_name = 'secciones'


class SeccionDetailView(DetailView):
    model = Seccion
    context_object_name = 'seccion'


class DepartamentoListView(ListView):
    model = Departamento
    context_object_name = 'departamentoa'


class DepartamentoDetailView(DetailView):
    model = Departamento
    context_object_name = 'departamento'


class CarreraListView(ListView):
    model = Carrera
    context_object_name = 'carreras'


class CarreraDetailView(DetailView):
    model = Carrera
    context_object_name = 'carrera'


class FacultadInstanciaListView(ListView):
    model = UnidadInstancia
    context_object_name = 'facultades'


class FacultadInstanciaDetailView(DetailView):
    model = UnidadInstancia
    context_object_name = 'facultad'


class EscuelaInstanciaListView(ListView):
    model = SeccionInstancia
    context_object_name = 'escuelas'


class EscuelaInstanciaDetailView(DetailView):
    model = SeccionInstancia
    context_object_name = 'escuela'


class DepartamentoInstanciaListView(ListView):
    model = DepartamentoInstancia
    context_object_name = 'departamentos'


class DepartamentoInstanciaDetailView(DetailView):
    model = DepartamentoInstancia
    context_object_name = 'departamento'


class CarreraInstanciaListView(ListView):
    model = CarreraInstancia
    context_object_name = 'carreras'


class CarreraInstanciaDetailView(DetailView):
    model = CarreraInstancia
    context_object_name = 'carrera'
