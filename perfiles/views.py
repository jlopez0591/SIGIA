from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from django.views.generic import DetailView, UpdateView, ListView
from django.urls import reverse_lazy

from perfiles.models import Perfil
from perfiles.forms import PerfilForm, PerfilTestForm

from dal import autocomplete


def consulta_profesor(request):
    if request.user.is_superuser:
        # profesores = Perfil.objects.profesores()
        profesores = None
    elif request.user.perfil.facultad:
        profesores = Perfil.objects.filter(facultad=request.user.perfil.facultad)
    else:
        profesores = None
    return render(request, 'perfiles/consulta.html', {
        'perfiles': Perfil.objects.all()
    })


class ProfesoresFacultadListView(ListView):
    model = Perfil
    context_object_name = 'perfiles'
    template_name = 'perfiles/consulta.html'

    def get_queryset(self):
        qs = Perfil.objects.profesores().filter(facultad_id=self.kwargs['pk'])
        return qs


class ProfesoresDepartamentoListView(ListView):
    model = Perfil
    context_object_name = 'perfiles'
    template_name = 'perfiles/consulta.html'

    def get_queryset(self):
        qs = Perfil.objects.profesores().filter(departamento_id=self.kwargs['pk'])
        return qs


class PerfilDetailView(DetailView):
    model = Perfil
    context_object_name = 'perfil'
    template_name = 'perfiles/privado_redux.html'

    def get_object(self, queryset=None):
        return Perfil.objects.get_or_create(usuario=self.request.user)[0]


class PerfilPublicoView(DetailView):
    model = Perfil
    context_object_name = 'perfil'
    template_name = 'perfiles/privado_redux.html'


class PerfilUpdateView(UpdateView):
    model = Perfil
    form_class = PerfilForm
    success_url = reverse_lazy('perfil:ver')
    template_name = 'perfiles/editar.html'
    context_object_name = 'form'

    def get_object(self, queryset=None):
        usuario = self.request.user
        object = Perfil.objects.get_or_create(usuario=usuario)[0]
        return object


class ProfesoresAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if self.request.user.is_superuser:
            qs = User.objects.all()
        elif self.request.user.is_authenticated():
            perfil = Perfil.objects.get(usuario=self.request.user)  # TODO: Arreglar busqueda
            # qs =
        else:
            return User.objects.none()

        if self.q:
            qs = qs.filter(username__icontains=self.q)
        return qs

    def get_result_label(self, item):
        return item.get_full_name()

    def get_selected_result_label(self, item):
        return item.short_name
