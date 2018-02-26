from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy

from perfiles.models import Perfil
from perfiles.forms import PerfilForm, PerfilTestForm

from dal import autocomplete


# def consulta_profesor(request):
#     if request.user.is_superuser:
#         profesores = Perfil.objects.profesores()
#     elif request.user.has_perms('ubicacion:ver-profesores'):
#         profesores = Perfil.objects.profesores().filter() # TODO: Agregar filter por ubicacion.
#     filter = PerfilFilter(request.GET, queryset=profesores)
#     paginator = Paginator(filter.qs, 10)
#     page = request.GET.get('page')
#     try:
#         perfil_p = paginator.page(page)
#     except PageNotAnInteger:
#         perfil_p = paginator.page(1)
#     except EmptyPage:
#         perfil_p = paginator.page(paginator.num_pages)
#     return render(request, 'perfiles/consulta.html', {
#         'filter': filter,
#         'perfiles': perfil_p
#     })

def consulta_profesor(request):
    if request.user.is_superuser:
        profesores = Perfil.objects.profesores()
    elif request.user.perfil.unidad:
        profesores = Perfil.objects.filter(unidad=request.user.perfil.unidad)
    else:
        profesores = None
    return render(request, 'perfiles/consulta.html', {
        'perfiles': profesores
    })


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
            perfil = Perfil.objects.get(usuario=self.request.user)
        else:
            return User.objects.none()

        if self.q:
            qs = qs.filter(username__icontains=self.q)
        return qs
