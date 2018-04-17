from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.urls import reverse_lazy

from inventario.forms import AulaForm
from inventario.models import Aula
from ubicacion.models import FacultadInstancia
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import get_list_or_404
from django.core.exceptions import PermissionDenied


class AulaListView(ListView):
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


class AulaFacultadListView(ListView):
    model = Aula
    template_name = 'inventario/aula/lista.html'
    context_object_name = 'aulas'

    def get_queryset(self):
        qs = None
        unidad = FacultadInstancia.objects.get(pk=self.kwargs['pk'])
        usuario = self.request.user
        if usuario.is_authenticated:
            if usuario.perfil.facultad is not unidad:
                if not usuario.is_superuser:
                    raise PermissionDenied
            qs = Aula.objects.filter(ubicacion=self.kwargs['pk'])
        return qs


class AulaDetailView(DetailView):
    context_object_name = 'aula'
    model = Aula
    template_name = 'inventario/aula/detalle.html'

    def get_object(self):
        object = super(AulaDetailView, self).get_object()
        usuario = self.request.user
        if usuario.perfil.facultad is not object.facultad:
            raise PermissionDenied
        return object


class AulaCreateView(SuccessMessageMixin, CreateView):
    model = Aula
    form_class = AulaForm
    template_name = 'inventario/aula/crear.html'
    success_url = reverse_lazy('inventario:lista-aulas')
    success_message = 'Aula registrada'

    def form_valid(self, form):
        form.instance.cod_sede = self.request.user.perfil.cod_sede
        form.instance.cod_facultad = self.request.user.perfil.cod_facultad
        return super(AulaCreateView, self).form_valid(form)


class AulaUpdateView(UpdateView):
    model = Aula
    template_name = 'inventario/aula/crear.html'
    form_class = AulaForm
    success_url = reverse_lazy('inventario:lista-aulas')

    def get_object(self):
        object = super(AulaUpdateView, self).get_object()
        usuario = self.request.user
        if usuario.perfil.facultad is not object.facultad:
            raise PermissionDenied
        return object
