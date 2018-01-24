from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.urls import reverse
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.urls import reverse_lazy
from django.utils import timezone
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect

from actividades.forms import EstadiaForm
from actividades.models import Actividad, EstadiaPostdoctoral
from perfiles.models import Perfil


# Create your views here.
class ActividadListView(UserPassesTestMixin, ListView):
    model = Actividad
    paginate_by = 25

    def test_func(self):
        return self.request.user.is_superuser


def crear_estadia(request):
    if request.method == 'POST':
        u = User.objects.get(pk=request.user.pk)
        print('Prueba')
        form = EstadiaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.usuario = u
            f.save()
            return redirect('perfil:ver')
        else:
            print(form.errors)
    else:
        form = EstadiaForm()
    return render(request, 'actividades/estadia_create_form.html', {'form': form})


class ActivityCreateView(SuccessMessageMixin, CreateView):
    # permission_required = ''
    success_url = reverse_lazy('perfil:ver')
    context_object_name = 'form'
    success_message = 'Actividad Registrada'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        try:
            return super(ActivityCreateView, self).form_valid(form)
        except IntegrityError:
            return self.form_invalid(form)


class EstadiaCreateView(CreateView):
    # permission_required = ''
    form_class = EstadiaForm
    model = EstadiaPostdoctoral
    success_url = reverse_lazy('perfil:ver')
    context_object_name = 'form'
    template_name = 'form.html'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        try:
            print("Formulario Valido")
            return super(EstadiaCreateView, self).form_valid(form)
        except IntegrityError:
            print("Formulario Invalido")
            return super(EstadiaCreateView, self).form_invalid(form)


class ActivityDetailView(DetailView):
    context_object_name = 'actividad'


class ActivityUpdateView(PermissionRequiredMixin, UpdateView):
    context_object_name = 'actividad'
    permission_required = 'actividad.change_actividad'
    success_url = reverse_lazy('insight:perfil')

    def get_object(self, queryset=None):
        object = super(ActivityUpdateView, self).get_object()
        usuario = self.request.user
        if usuario is object.usuario or usuario.is_superuser:
            if object.estado == 'rechazado':
                object.espera()
            return object
        else:
            raise PermissionDenied


class ActividadesPropias(ListView):
    model = Actividad
    context_object_name = 'actividades'
    template_name = 'actividad/lista.html'

    def get_queryset(self):
        usuario = self.request.user
        qs = Actividad.objects.get(usuario=usuario)
        return qs


class ActividadesPendientes(PermissionRequiredMixin, ListView):
    model = Actividad
    context_object_name = 'actividades'
    permission_required = 'aprobar_actividad'
    template_name = 'actividades/lista.html'
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_superuser:
            qs = Actividad.objects.filter(estado='espera')
        else:
            perfil = Perfil.objects.get(usuario=self.request.user)
            codigos = perfil.seccion
            qs = Actividad.objects.filter(seccion=codigos, estado='espera')
        return qs


def actividades_pendientes(request):
    cantidad_por_pagina = 3
    if request.user.is_authenticated():
        lista = Actividad.objects.filter(estado='espera')
    else:
        u = Perfil.objects.get(usuario=request.user)
        lista = Actividad.objects.filter(seccion=u.seccion, estado='espera')
    page = request.GET.get('page', 1)

    paginator = Paginator(lista, cantidad_por_pagina)
    try:
        actividades = paginator.page(page)
    except PageNotAnInteger:
        actividades = paginator.page(1)
    except EmptyPage:
        actividades = paginator.page(paginator.num_pages)
    return render(request, 'actividades/lista.html', {'actividades': actividades})


@permission_required('actividad.aprobar_actividad')
def aprobar_actividad(request, actividad_pk):
    if request.method == 'POST':
        actividad = Actividad.objects.get(pk=actividad_pk)
        usuario = Actividad.usuario
        texto = "ha sido aprobada!"
        actividad.aprobar()
        # Notificacion.objects.create(usuario=usuario, actividad=actividad, fecha_creada=timezone.now())
        return reverse('actividad:lista')


@permission_required('actividad.aprobar_actividad')
def rechazar_actividad(request, actividad_pk):
    if request.method == 'POST':
        actividad = Actividad.objects.get(pk=actividad_pk)
        actividad.aprobar()
        return reverse('actividad:lista')
