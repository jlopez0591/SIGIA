import csv

from tablib import Dataset

from django.http import JsonResponse
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.urls import reverse_lazy

from inventario.forms import FabricanteForm
from inventario.models import Fabricante
from django.contrib.messages.views import SuccessMessageMixin


# Fabricante
class FabricanteListView(ListView):
    context_object_name = 'fabricantes'
    model = Fabricante
    template_name = 'inventario/fabricante/lista.html'


class FabricanteDetailView(DetailView):
    context_object_name = 'fabricante'
    model = Fabricante
    template_name = 'inventario/fabricante/detalle.html'


class FabricanteCreateView(SuccessMessageMixin, CreateView):
    context_object_name = 'form'
    form_class = FabricanteForm
    model = Fabricante
    template_name = 'inventario/fabricante/crear.html'
