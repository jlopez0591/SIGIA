from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.urls import reverse_lazy

from inventario.forms import ModeloForm
from inventario.models import Modelo
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin


# Modelos
class ModeloListView(ListView):
    context_object_name = 'modelos'
    model = Modelo
    template_name = 'inventario/modelo/lista.html'
    queryset = Modelo.objects.all().order_by('categoria__nombre')


class ModeloDetailView(DetailView):
    context_object_name = 'modelo'
    model = Modelo
    template_name = 'inventario/modelo/detalle.html'


class ModeloCreateView(SuccessMessageMixin, CreateView):
    context_object_name = 'form'
    form_class = ModeloForm
    model = Modelo
    template_name = 'inventario/modelo/crear.html'


class ModeloUpdateView(UpdateView):
    model = Modelo
    form_class = ModeloForm
    context_object_name = 'form'
    template_name = 'inventario/modelo/crear.html'
    success_url = reverse_lazy('inventario:equipo-lista     ')