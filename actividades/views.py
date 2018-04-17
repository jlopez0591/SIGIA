from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import permission_required
from django.db import IntegrityError
from django.urls import reverse
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.http import Http404

from actividades.forms import RechazarForm
from actividades.models import Actividad
from perfiles.models import Perfil


class ActivityCreateView(SuccessMessageMixin, PermissionRequiredMixin, CreateView):
    context_object_name = 'form'
    success_message = 'Actividad Registrada'
    permission_required = 'actividades.add_actividad'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        try:
            return super(ActivityCreateView, self).form_valid(form)
        except IntegrityError:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('actividad:propias', kwargs={
            'pk': self.request.user.pk
        })

    def get_context_data(self, **kwargs):
        context = super(ActivityCreateView, self).get_context_data(**kwargs)
        context['titulo'] = self.kwargs['titulo']
        return context


class ActivityDetailView(DetailView):
    context_object_name = 'actividad'


class ActivityUpdateView(PermissionRequiredMixin, UpdateView):
    context_object_name = 'actividad'
    permission_required = 'actividades.change_actividad'

    def get_object(self, queryset=None):
        object = super(ActivityUpdateView, self).get_object()
        usuario = self.request.user
        if usuario is object.usuario or usuario.is_superuser:
            if object.estado == 'rechazado':
                object.espera()
            return object
        else:
            raise PermissionDenied

    def get_success_url(self):
        return self.object.get_absolute_url()


class ActividadesPendientes(PermissionRequiredMixin, ListView):
    model = Actividad
    context_object_name = 'actividades'
    permission_required = 'actividades.aprobar_actividad'
    template_name = 'actividades/admin/pendientes.html'
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_superuser:
            qs = Actividad.objects.en_espera()
        else:
            qs = Actividad.objects.puede_aprobar(usuario=self.request.user)
        return qs


class ActividadListView(ListView):
    model = Actividad
    context_object_name = 'actividades'
    template_name = 'actividades/lista.html'


class ActividadesPropias(ListView):
    model = Actividad
    context_object_name = 'actividades'
    template_name = 'actividades/propias.html'

    def get_queryset(self):
        usuario = self.request.user
        qs = Actividad.objects.filter(usuario=usuario)
        return qs


class ActividadFacultadListView(ListView):
    model = Actividad
    context_object_name = 'actividades'
    permission_required = 'actividades.aprobar_actividad'
    template_name = 'actividades/lista.html'

    def get_queryset(self):
        qs = Actividad.objects.aprobado().filter(facultad_id=self.kwargs['pk'])
        return qs


class ActividadDepartamentoListview(ListView):
    model = Actividad
    context_object_name = 'actividades'
    permission_required = 'actividades.aprobar_actividad'
    template_name = 'actividades/lista.html'

    def get_queryset(self):
        qs = Actividad.objects.filter(departamento_id=self.kwargs['pk'])
        return qs

class ActividadDepartamentoPendienteListView(ListView):
    model = Actividad
    context_object_name = 'actividades'
    permission_required = 'actividades.aprobar_actividad'
    template_name = 'actividades/admin/pendientes.html'

    def get_queryset(self):
        qs = Actividad.objects.en_espera().filter(departamento_id=self.kwargs['pk'])
        return qs


class ListaActividades(PermissionRequiredMixin, ListView):
    model = Actividad
    context_object_name = 'actividades'
    permission_required = 'actividades.aprobar_actividad'
    template_name = 'actividades/lista.html'
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_superuser:
            qs = Actividad.objects.aprobado()
        elif True:
            qs = Actividad.objects.aprobado().filter()  # TODO: Filter por facultad
        else:
            qs = None
        return qs


@permission_required('actividad.aprobar_actividad')
def aprobar_actividad(request, pk):
    if request.method == 'POST':
        perfil = Perfil.objects.get(usuario=request.user)
        if request.user.perfil.departamento is not actividad.departamento:
            raise Http404("No tiene permiso de ver esta ubicacion.")
        actividad = Actividad.objects.get(pk=pk)
        if request.user.is_superuser or perfil.departamento == actividad.departamento:
            actividad.aprobar()
        return redirect(reverse('actividad:pendientes'))


@permission_required('actividad.aprobar_actividad')
def rechazar_actividad(request, pk):
    actividad = Actividad.objects.get(pk=pk)
    if request.user.perfil.departamento is not actividad.departamento:
        raise Http404("No tiene permiso de ver esta ubicacion.")
    if request.method == 'POST':
        form = RechazarForm(request.POST, instance=actividad)
        if form.is_valid():
            actividad = form.save(commit=False)
            actividad.estado = 'rechazado'
            actividad.save()
            return redirect('actividad:pendientes')
    else:
        form = RechazarForm(instance=actividad)
    return render(request, 'actividades/admin/rechazar.html', {'form': form})
