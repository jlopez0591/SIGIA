from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404

from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy

from perfiles.models import Perfil, Person
from perfiles.forms import PerfilForm
from .filters import PerfilFilter

from dal import autocomplete

def consulta_profesor(request):
    profesores = Perfil.objects.profesores()
    print(request)
    filter = PerfilFilter(request.GET, queryset=profesores)
    paginator = Paginator(filter.qs, 10)
    page = request.GET.get('page')
    try:
        perfil_p = paginator.page(page)
    except PageNotAnInteger:
        perfil_p = paginator.page(1)
    except EmptyPage:
        perfil_p = paginator.page(paginator.num_pages)
    return render(request, 'perfiles/consulta.html', {
        'filter': filter,
        'perfiles': perfil_p
    })


class PerfilDetailView(DetailView):
    model = Perfil
    context_object_name = 'perfil'
    template_name = 'perfiles/privado.html'

    def get_object(self, queryset=None):
        return Perfil.objects.get_or_create(usuario=self.request.user)[0]


class PerfilPublicoView(DetailView):
    model = Perfil
    context_object_name = 'perfil'
    template_name = 'perfil/publico.html'


class PerfilUpdateView(UpdateView):
    model = Perfil
    form_class = PerfilForm
    success_url = reverse_lazy('')
    template_name = 'perfiles/editar.html'
    context_object_name = 'form'

    def get_object(self, queryset=None):
        usuario = self.request.user
        object = Perfil.objects.get_or_create(usuario=usuario)[0]
        return object

class ProfesoresAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if self.request.user.is_superuser:
            qs = Person.objects.all()
        elif self.request.user.is_authenticated():
            perfil = Perfil.objects.get(usuario=self.request.user)
            codigos = {
                'cod_sede': perfil.cod_sede,
                'cod_unidad': perfil.cod_unidad,
                'cod_seccion': perfil.cod_seccion
            }
            # # usuario = Person.objects.get(pk=self.request.user.pk)
            # carreras = perfil.seccion.carreras.all()
            # # Estudiante.objects.get(**usuario.kwargs_ubicacion())
            # q_objects = Q()
            # for carrera in carreras:
            #     q_objects |= Q(carrera=carrera)
            qs = Person.objects.filter(**codigos, groups__name__in=['foo'])
        else:
            return Person.objects.none()

        if self.q:
            qs = qs.filter(first_name__icontains=self.q)
        return qs
