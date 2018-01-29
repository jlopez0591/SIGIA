from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.urls import reverse_lazy

from inventario.forms import EquipoForm
from inventario.models import Equipo

from perfiles.models import Perfil
from django.contrib.messages.views import SuccessMessageMixin


# Equipos
class EquipoListView(ListView):
    context_object_name = 'equipos'
    model = Equipo
    template_name = 'inventario/equipo/lista.html'

    def get_queryset(self):
        if self.request.user.perfil:
            return Equipo.objects.filter(ubicacion=self.request.user.perfil.unidad)
        else:
            return None


class EquipoFacultadListView(ListView):
    context_object_name = 'equipos'
    model = Equipo
    template_name = 'inventario/equipo/lista.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Equipo.objects.filter(ubicacion=self.kwargs['pk'])
        else:
            qs = None
        return qs


class EquipoDetailView(DetailView):
    context_object_name = 'equipo'
    model = Equipo
    template_name = 'inventario/equipo/detalle.html'


class EquipoUpdateView(UpdateView):
    form_class = EquipoForm
    model = Equipo
    template_name = 'form.html'


class EquipoCreateView(SuccessMessageMixin, CreateView):
    form_class = EquipoForm
    model = Equipo
    template_name = 'inventario/equipo/crear.html'
    success_url = reverse_lazy('inventario:lista-equipo')

    def form_valid(self, form):
        usuario = Perfil.objects.get(usuario=self.request.user)
        form.instance.cod_sede = usuario.cod_sede
        form.instance.cod_unidad = usuario.cod_unidad
        try:
            return super(EquipoCreateView, self).form_valid(form)
        except:
            return self.form_invalid(form)
