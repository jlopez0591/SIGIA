import csv

from tablib import Dataset

from django.http import JsonResponse
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.urls import reverse_lazy

from inventario.forms import BulkCreateForm, CategoriaForm, FabricanteForm, ModeloForm, EquipoForm, AulaForm
from inventario.models import Aula, Categoria, Fabricante, Modelo, Equipo
from inventario.resources import CategoriaResource, FabricanteResource, EquipoResource, ModeloResource

from perfiles.models import Perfil


# Fabricante
class FabricanteListView(ListView):
    context_object_name = 'fabricantes'
    model = Fabricante
    template_name = 'inventario/fabricante/lista.html'


class FabricanteDetailView(DetailView):
    context_object_name = 'fabricante'
    model = Fabricante
    template_name = 'inventario/fabricante/detalle.html'


class FabricanteCreateView(CreateView):
    context_object_name = 'form'
    form_class = FabricanteForm
    model = Fabricante
    template_name = 'inventario/fabricante/crear.html'


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
    template_name = 'inventario/modelo/lista.html'
    queryset = Modelo.objects.all().order_by('categoria__nombre')


class ModeloDetailView(DetailView):
    context_object_name = 'modelo'
    model = Modelo
    template_name = 'inventario/modelo/detalle.html'


class ModeloCreateView(CreateView):
    context_object_name = 'form'
    form_class = ModeloForm
    model = Modelo
    template_name = 'inventario/modelo/crear.html'


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
    template_name = 'inventario/equipo/crear.html'

    def form_valid(self, form):
        usuario = Perfil.objects.get(usuario=self.request.user)
        form.instance.cod_sede = usuario.cod_sede
        form.instance.cod_unidad = usuario.cod_unidad
        try:
            return super(EquipoCreateView, self).form_valid(form)
        except:
            return self.form_invalid(form)


class AulaListView(ListView):
    paginate_by = 10
    model = Aula
    template_name = 'inventario/aula/lista.html'
    context_object_name = 'aulas'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Aula.objects.all()
        elif self.request.user.is_authenticated:
            return Aula.objects.filter(ubicacion=self.request.user.perfil.unidad)
        else:
            return False


class AulaDetailView(DetailView):
    context_object_name = 'aula'
    model = Aula
    template_name = 'inventario/aula/detalle.html'


class AulaCreateView(CreateView):
    model = Aula
    form_class = AulaForm
    template_name = 'inventario/aula/crear.html'
    success_url = reverse_lazy('inventario:lista-aulas')

    def form_valid(self, form):
        form.instance.cod_sede = self.request.user.perfil.cod_sede
        form.instance.cod_sede = self.request.user.perfil.cod_unidad
        return super(AulaCreateView, self).form_valid(form)


class AulaUpdateView(UpdateView):
    model = Aula
    template_name = 'inventario/aula/crear.html'


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
