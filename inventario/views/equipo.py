from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin


from inventario.forms import EquipoForm
from inventario.models import Equipo

from perfiles.models import Perfil
from ubicacion.models import FacultadInstancia
from django.core.exceptions import PermissionDenied
from django.contrib.messages.views import SuccessMessageMixin


# Equipos
class EquipoListView(ListView):
    context_object_name = 'equipos'
    model = Equipo
    template_name = 'inventario/equipo/lista.html'

    def get_queryset(self):
        if self.request.user.perfil:
            return Equipo.objects.filter(ubicacion=self.request.user.perfil.facultad)
        else:
            return None


class EquipoFacultadListView(PermissionRequiredMixin, ListView):
    context_object_name = 'equipos'
    model = Equipo
    permission_required = 'ubicacion.ver_equipos_facultad'
    template_name = 'inventario/equipo/lista.html'
    paginate_by = 10

    def get_queryset(self):
        facultad = FacultadInstancia.objects.get(pk=self.kwargs['pk'])
        usuario = self.request.user
        if usuario.perfil.facultad != facultad:
            raise PermissionDenied
        qs = Equipo.objects.filter(ubicacion=self.kwargs['pk'])
        return qs


class EquipoDetailView(DetailView):
    context_object_name = 'equipo'
    model = Equipo
    template_name = 'inventario/equipo/detalle.html'

    def get_object(self):
        object = super(EquipoDetailView, self).get_object()
        usuario = self.request.user
        if usuario.perfil.facultad != object.facultad:
            raise PermissionDenied
        return object


class EquipoUpdateView(UpdateView):
    form_class = EquipoForm
    model = Equipo
    template_name = 'inventario/equipo/crear.html'

    def get_object(self):
        object = super(EquipoUpdateView, self).get_object()
        usuario = self.request.user
        if usuario.perfil.facultad != object.facultad:
            raise PermissionDenied
        return object


class EquipoCreateView(SuccessMessageMixin, CreateView):
    form_class = EquipoForm
    model = Equipo
    template_name = 'inventario/equipo/crear.html'
    success_url = reverse_lazy('inventario:lista-equipo')

    def form_valid(self, form):
        usuario = Perfil.objects.get(usuario=self.request.user)
        form.instance.cod_sede = usuario.cod_sede
        form.instance.cod_facultad = usuario.cod_facultad
        try:
            return super(EquipoCreateView, self).form_valid(form)
        except:
            return self.form_invalid(form)
