from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.urls import reverse
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect

from actividades.forms import EstadiaForm, RechazarForm
from actividades.models import Actividad, EstadiaPostdoctoral
from perfiles.models import Perfil


# Create your views here.
class ActividadListView(UserPassesTestMixin, ListView):
    model = Actividad
    paginate_by = 25

    def test_func(self):
        return self.request.user.is_superuser


class ActivityCreateView(SuccessMessageMixin, CreateView):
    # permission_required = ''
    success_url = reverse_lazy('actividad:propias')
    context_object_name = 'form'
    success_message = 'Actividad Registrada'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        try:
            return super(ActivityCreateView, self).form_valid(form)
        except IntegrityError:
            return self.form_invalid(form)


# TODO: Dynamic model and template: https://stackoverflow.com/questions/20049067/class-based-detailview-dynamically-choose-template
class ActivityDetailView(DetailView):
    context_object_name = 'actividad'


class ActivityUpdateView(PermissionRequiredMixin, UpdateView):
    context_object_name = 'actividad'
    permission_required = 'actividades.change_actividad'
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
    template_name = 'actividades/propias.html'

    def get_queryset(self):
        usuario = self.request.user
        qs = Actividad.objects.filter(usuario=usuario)
        return qs


class ActividadesPendientes(PermissionRequiredMixin, ListView):
    model = Actividad
    context_object_name = 'actividades'
    permission_required = 'actividades.aprobar_actividad'
    template_name = 'actividades/admin/pendientes.html'
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_superuser:
            qs = Actividad.objects.filter(estado='espera')
        else:
            qs = Actividad.objects.puede_aprobar(usuario=self.request.user)
        return qs


@permission_required('actividad.aprobar_actividad')
def aprobar_actividad(request, pk):
    if request.method == 'POST':
        actividad = Actividad.objects.get(pk=pk)
        usuario = Actividad.usuario
        texto = "ha sido aprobada!"
        actividad.aprobar()
        # Notificacion.objects.create(usuario=usuario, fecha_creada=timezone.now())
        return redirect(reverse('actividad:pendientes'))


class ActividadRechazarView(SuccessMessageMixin, UpdateView):
    context_object_name = 'form'
    form_class = RechazarForm
    model = Actividad
    success_message = 'Actividad Rechazada'
    success_url = reverse_lazy('core:index')
    template_name = 'actividades/admin/rechazar.html'

    def form_valid(self, form):
        form = form.instance
        form.estado = 'rechazado'
        return super(ActividadRechazarView, self).form_valid(form)

