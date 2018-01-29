from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy

from inventario.forms import CategoriaForm
from inventario.models import Categoria
from django.contrib.messages.views import SuccessMessageMixin


# Categorias
class CategoriaListView(ListView):
    context_object_name = 'categorias'
    model = Categoria
    template_name = 'inventario/categoria/lista.html'


class CategoriaDetailView(DetailView):
    context_object_name = 'categoria'
    model = Categoria
    template_name = 'inventario/categoria/detalle.html'


class CategoriaCreateView(SuccessMessageMixin, CreateView):
    context_object_name = 'form'
    form_class = CategoriaForm
    model = Categoria
    template_name = 'inventario/categoria/crear.html'
    success_url = reverse_lazy('inventario:categoria-lista')
