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
from ubicacion.models import DepartamentoInstancia, FacultadInstancia

# IN USE
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

# In Use
class ActivityDetailView(PermissionRequiredMixin, DetailView):
    context_object_name = 'actividad'
    permission_required = ('actividad.add_actividad', 'ubicacion.ver_actividades_departamento', 'ubicacion.ver_actividades_facultad')

    def get_object(self, **kwargs):
        object = super(ActivityDetailView, self).get_object(**kwargs)
        usuario = self.request.user
        if usuario is object.usuario:
            return object
        elif usuario.perfil.departamento is object.departamento:
            return object
        elif usuario.perfil.facultad is object.facultad:
            return object
        elif usuario.is_superuser:
            return object
        else:
            raise PermissionDenied
        


#IN USE
class ActivityUpdateView(PermissionRequiredMixin, UpdateView):
    context_object_name = 'actividad'
    permission_required = 'actividades.change_actividad'

    def get_object(self, queryset=None):
        object = super(ActivityUpdateView, self).get_object()
        usuario = self.request.user
        if usuario is object.usuario:
            if object.estado == 'rechazado':
                object.espera()
            return object
        else:
            raise PermissionDenied

    def get_success_url(self):
        return self.object.get_absolute_url()

# IN USE
class ActividadListView(ListView):
    model = Actividad
    context_object_name = 'actividades'
    template_name = 'actividades/lista.html'

# IN USE
class ActividadesPropias(ListView):
    model = Actividad
    context_object_name = 'actividades'
    template_name = 'actividades/propias.html'

    def get_queryset(self):
        usuario = self.request.user
        qs = Actividad.objects.filter(usuario=usuario)
        return qs

# IN USE
class ActividadFacultadListView(ListView):
    model = Actividad
    context_object_name = 'actividades'
    permission_required = 'ubicacion.ver_actividades_facultad'
    template_name = 'actividades/lista.html'

    def get_queryset(self):
        facultad = FacultadInstancia.objects.get(pk=self.kwargs['pk'])
        if self.request.user.perfil.facultad is not facultad:
            raise PermissionDenied
        else:
            qs = Actividad.objects.en_espera().filter(facultad=facultad)
        return qs

# IN USE
class ActividadDepartamentoListview(ListView):
    model = Actividad
    context_object_name = 'actividades'
    permission_required = 'actividades.ver_actividades_departamento'
    template_name = 'actividades/lista.html'

    def get_queryset(self):
        departamento = DepartamentoInstancia.objects.get(pk=self.kwargs['pk'])
        if self.request.user.perfil.departamento is not departamento:
            raise PermissionDenied
        else:
            qs = Actividad.objects.en_espera().filter(departamento=departamento)
        return qs

# IN USE
class ActividadDepartamentoPendienteListView(ListView):
    model = Actividad
    context_object_name = 'actividades'
    permission_required = 'actividades.aprobar_actividad'
    template_name = 'actividades/admin/pendientes.html'

    def get_queryset(self):
        departamento = DepartamentoInstancia.objects.get(pk=self.kwargs['pk'])
        if self.request.user.perfil.departamento is not departamento:
            raise PermissionDenied
        else:
            qs = Actividad.objects.en_espera().filter(departamento=departamento)
        return qs


# IN USE
@permission_required('actividad.aprobar_actividad')
def aprobar_actividad(request, pk):
    if request.method == 'POST':
        perfil = Perfil.objects.get(usuario=request.user)
        if request.user.perfil.departamento is not actividad.departamento:
            raise PermissionDenied
        actividad = Actividad.objects.get(pk=pk)
        if request.user.is_superuser or perfil.departamento == actividad.departamento:
            actividad.aprobar()
        return redirect(reverse('actividad:pendientes'))

# IN USE
@permission_required('actividad.aprobar_actividad')
def rechazar_actividad(request, pk):
    actividad = Actividad.objects.get(pk=pk)
    if request.user.perfil.departamento is not actividad.departamento:
        raise PermissionDenied
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
