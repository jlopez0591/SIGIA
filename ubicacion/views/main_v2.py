from ubicacion.models import Sede
from ubicacion.models import Facultad
from ubicacion.models import Escuela
from ubicacion.models import Departamento
from ubicacion.models import Carrera
from ubicacion.models import FacultadInstancia
from ubicacion.models import EscuelaInstancia
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
    model = Facultad
    context_object_name = 'facultades'


class FacultadDetailView(DetailView):
    model = Facultad
    context_object_name = 'facultad'


class SeccionListView(ListView):
    model = Escuela
    context_object_name = 'secciones'


class SeccionDetailView(DetailView):
    model = Escuela
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
    model = FacultadInstancia
    context_object_name = 'facultades'


class FacultadInstanciaDetailView(DetailView):
    model = FacultadInstancia
    context_object_name = 'facultad'


class EscuelaInstanciaListView(ListView):
    model = EscuelaInstancia
    context_object_name = 'escuelas'


class EscuelaInstanciaDetailView(DetailView):
    model = EscuelaInstancia
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
