import csv

from tablib import Dataset

from django.shortcuts import render, redirect, reverse
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.urls import reverse_lazy

from inventario.forms import BulkCreateForm, CategoriaForm, FabricanteForm, ModeloForm, EquipoForm
from inventario.models import Categoria, Fabricante, Modelo, Equipo
from inventario.resources import CategoriaResource, FabricanteResource, EquipoResource, ModeloResource

from perfiles.models import Perfil


# Create your views here.

# Fabricante
class FabricanteListView(ListView):
    context_object_name = 'fabricantes'
    model = Fabricante
    template_name = 'inventario/fabricantes.html'


class FabricanteDetailView(DetailView):
    context_object_name = 'fabricante'
    model = Fabricante
    template_name = 'inventario/fabricante/detalle.html'


class FabricanteCreateView(CreateView):
    context_object_name = 'form'
    form_class = FabricanteForm
    model = Fabricante
    template_name = 'form.html'


# Categorias
class CategoriaListView(ListView):
    context_object_name = 'categorias'
    model = Categoria
    template_name = 'inventario/categoria/lista.html'


class CategoriaDetailView(DetailView):
    context_object_name = 'categoria'
    model = Categoria
    template_name = 'inventario/categoria/detalle.html'


class CategoriaCreateView(CreateView):
    context_object_name = 'form'
    form_class = CategoriaForm
    model = Categoria
    template_name = 'inventario/categoria/crear.html'
    success_url = reverse_lazy('inventario:categoria-lista')


# Modelos
class ModeloListView(ListView):
    context_object_name = 'modelos'
    model = Modelo
    template_name = 'inventario/modelos.html'


class ModeloDetailView(DetailView):
    context_object_name = 'modelo'
    model = Modelo
    template_name = 'inventario/modelo.html'


class ModeloCreateView(CreateView):
    context_object_name = 'form'
    form_class = ModeloForm
    model = Modelo
    template_name = 'form.html'


# Equipos
class EquipoListView(ListView):
    context_object_name = 'equipos'
    model = Equipo
    template_name = 'inventario/equipos.html'


class EquipoDetailView(DetailView):
    context_object_name = 'equipo'
    model = Equipo
    template_name = 'inventario/equipo/equipo.html'


class EquipoUpdateView(UpdateView):
    form_class = EquipoForm
    model = Equipo
    template_name = 'form.html'


class EquipoCreateView(CreateView):
    form_class = EquipoForm
    model = Equipo
    template_name = 'form.html'

    def form_valid(self, form):
        usuario = Perfil.objects.get(usuario=self.request.user)
        form.instance.cod_sede = usuario.cod_sede
        form.instance.cod_unidad = usuario.cod_unidad
        try:
            return super(EquipoCreateView, self).form_valid(form)
        except:
            return self.form_invalid(form)


# Generico
class InfoListView(ListView):
    template_name = 'inventario/lista.html'
    nombre = ''

    def get_context_data(self, **kwargs):
        context = super(InfoListView, self).get_context_data()
        context['nombre'] = self.nombre
        return context


class InfoCreateView(CreateView):
    template_name = 'form.html'


class InfoDetailView(DetailView):
    template_name = 'form.html'


def carga_fabricantes(request):
    if request.method == 'POST':
        person_resource = FabricanteResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now
    return render(request, 'file_upload.html')


def carga_categorias(request):
    if request.method == 'POST':
        person_resource = CategoriaResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now
    return render(request, 'file_upload.html')


def carga_modelos(request):
    if request.method == 'POST':
        person_resource = ModeloResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now
    return render(request, 'file_upload.html')


def carga_equipos(request):
    if request.method == 'POST':
        person_resource = EquipoResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now
    return render(request, 'file_upload.html')


def process_csv(csv_file):
    return csv.DictReader(csv_file.read().decode('utf-8'))
