from django.db import IntegrityError
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from estudiantes.forms import StudentUpdateForm, TrabajoForm
from estudiantes.models import Estudiante, TrabajoGraduacion
from ubicacion.models import FacultadInstancia, EscuelaInstancia
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy


class EstudianteFacultadListview(PermissionRequiredMixin, ListView):
    context_object_name = 'estudiantes'
    model = Estudiante
    permission_required = ('ubicacion.ver_estudiantes_facultad')
    template_name = 'estudiantes/consultar.html'

    def get_queryset(self):
        facultad = FacultadInstancia.objects.get(pk=self.kwargs['pk'])
        usuario = self.request.user
        if usuario.perfil.facultad != facultad:
            raise PermissionDenied
        qs = Estudiante.objects.facultad(facultad=self.kwargs['pk'])
        return qs


#
class EstudianteEscuelaListView(ListView):
    context_object_name = 'estudiantes'
    model = Estudiante
    permission_required = ('ubicacion.ver_estudiantes_escuela')
    template_name = 'estudiantes/consultar.html'

    def get_queryset(self):
        qs = Estudiante.objects.escuela(escuela=self.kwargs['pk'])
        return qs


#
class EstudianteListView(ListView):
    context_object_name = 'estudiantes'
    model = Estudiante
    template_name = 'estudiantes/consultar.html'


#
class EstudianteDetailView(PermissionRequiredMixin, DetailView):
    context_object_name = 'estudiante'
    permission_required = 'ubicacion.ver_estudiante_escuela'
    model = Estudiante
    template_name = 'estudiantes/detalle.html'

    # def get_object(self):
    #     object = super(EstudianteDetailView, self).get_object(self)
    #     usuario = self.request.user
    #     if usuario.perfil.escuela != object.escuela:
    #         raise PermissionDenied
    #     return object


#
class EstudianteUpdateView(PermissionRequiredMixin, UpdateView):
    model = Estudiante
    permission_required = 'estudiantes.change_estudiante'
    form_class = StudentUpdateForm
    template_name = 'estudiantes/editar.html'

    # def get_object(self):
    #     object = super(EstudianteUpdateView, self).get_object(self)
    #     usuario = self.request.user
    #     if usuario.perfil.escuela != object.escuela:
    #         raise PermissionDenied
    #     return object


#
class TrabajoGraduacionCreateView(PermissionRequiredMixin, CreateView):
    model = TrabajoGraduacion
    form_class = TrabajoForm
    permission_required = 'estudiantes.add_trabajograduacion'
    template_name = 'estudiantes/trabajos/form.html'
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        form.instance.registrado_por = self.request.user
        try:
            return super(TrabajoGraduacionCreateView, self).form_valid(form)
        except IntegrityError:
            return self.form_invalid(form)

    def get_form_kwargs(self):
        kwargs = super(TrabajoGraduacionCreateView, self).get_form_kwargs()
        kwargs.update({'facultad': self.request.user.perfil.facultad})
        return kwargs


#
class TrabajoGraduacionUpdateView(PermissionRequiredMixin, UpdateView):
    model = TrabajoGraduacion
    form_class = TrabajoForm
    permission_required = 'estudiantes.change_trabajo'
    template_name = 'estudiantes/trabajos/form.html'

    def get_form_kwargs(self):
        kwargs = super(TrabajoGraduacionUpdateView, self).get_form_kwargs()
        kwargs.update({'facultad': self.request.user.perfil.facultad})
        return kwargs

    # def get_object(self):
    #     o = super(TrabajoGraduacionUpdateView, self).get_object(self)
    #     usuario = self.request.user
    #     if usuario.perfil.escuela != o.escuela:
    #         raise PermissionDenied
    #     return o


#
class TrabajoGraduacionDetailView(PermissionRequiredMixin, DetailView):
    model = TrabajoGraduacion
    context_object_name = 'trabajo'
    permission_required = ('ubicacion.ver_trabajo_escuela', 'ubicacion.ver_trabajo_facultad')
    template_name = 'estudiantes/trabajos/detalle.html'


class TrabajoGraduacionListView(PermissionRequiredMixin, ListView):
    model = TrabajoGraduacion
    context_object_name = 'trabajos'
    template_name = 'estudiantes/trabajos/lista.html'


#
class TrabajoGraduacionFacultadListView(PermissionRequiredMixin, ListView):
    model = TrabajoGraduacion
    permission_required = 'ubicacion.ver_trabajos_facultad'
    context_object_name = 'trabajos'
    template_name = 'estudiantes/trabajos/lista.html'

    def get_queryset(self):
        facultad = FacultadInstancia.objects.get(pk=self.kwargs['pk'])
        usuario = self.request.user
        if usuario.perfil.facultad != facultad or not usuario.is_superuser:
            raise PermissionDenied
        qs = TrabajoGraduacion.objects.facultad(facultad=self.kwargs['pk'])
        return qs


#
class TrabajoGraduacionEscuelaListView(PermissionRequiredMixin, ListView):
    model = TrabajoGraduacion
    permission_required = 'ubicacion.ver_trabajos_escuela'
    context_object_name = 'trabajos'
    template_name = 'estudiantes/trabajos/lista.html'

    def get_queryset(self):
        escuela = EscuelaInstancia.objects.get(pk=self.kwargs['pk'])
        usuario = self.request.user
        if usuario.perfil.escuela != escuela:
            raise PermissionDenied
        qs = TrabajoGraduacion.objects.escuela(escuela=self.kwargs['pk'])
        return qs


#
class TrabajoGraduacionPendienteListView(PermissionRequiredMixin, ListView):
    model = TrabajoGraduacion
    permission_required = 'estudiantes.change_trabajograduaction'
    context_object_name = 'trabajos'
    template_name = 'estudiantes/trabajos/pendiente.html'

    def get_queryset(self):
        escuela = EscuelaInstancia.objects.get(pk=self.kwargs['pk'])
        usuario = self.request.user
        if usuario.perfil.escuela != escuela:
            raise PermissionDenied
        qs = TrabajoGraduacion.objects.pendientes().escuela(escuela=self.kwargs['pk'])
        return qs

#
