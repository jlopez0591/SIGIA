from django.db import IntegrityError
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from estudiantes.forms import StudentUpdateForm, TrabajoForm
from estudiantes.models import Estudiante, TrabajoGraduacion

#
class EstudianteFacultadListview(PermissionRequiredMixin, ListView):
    context_object_name = 'estudiantes'
    model = Estudiante
    permission_required = ('ubicacion.ver_facultad')
    template_name = 'estudiantes/consultar.html'

    def get_queryset(self):
        qs = Estudiante.objects.facultad(facultad=self.kwargs['pk'])
        return qs

#
class EstudianteEscuelaListView(ListView):
    context_object_name = 'estudiantes'
    model = Estudiante
    permission_required = ('ubicacion.ver_facultad')
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
class EstudianteDetailView(DetailView):
    context_object_name = 'estudiante'
    model = Estudiante
    template_name = 'estudiantes/detalle.html'

#
class EstudianteUpdateView(PermissionRequiredMixin, UpdateView):
    model = Estudiante
    permission_required = 'estudiante.change_estudiante'
    form_class = StudentUpdateForm
    template_name = 'estudiantes/editar.html'

#
class TrabajoGraduacionCreateView(PermissionRequiredMixin, CreateView):
    model = TrabajoGraduacion
    form_class = TrabajoForm
    permission_required = 'estudiante.add_trabajograduaction'
    template_name = 'estudiantes/trabajos/form.html'

    def form_valid(self, form):
        form.instance.registrado_por = self.request.user
        try:
            return super(TrabajoGraduacionCreateView, self).form_valid(form)
        except IntegrityError:
            return self.form_invalid(form)


#
class TrabajoGraduacionUpdateView(PermissionRequiredMixin, UpdateView):
    model = TrabajoGraduacion
    form_class = TrabajoForm
    permission_required = 'estudiante.change_trabajo'
    template_name = 'estudiantes/trabajos/form.html'

#
class TrabajoGraduacionDetailView(DetailView):
    model = TrabajoGraduacion
    context_object_name = 'trabajo'
    template_name = 'estudiantes/trabajos/detalle.html'


class TrabajoGraduacionListView(PermissionRequiredMixin, ListView):
    model = TrabajoGraduacion
    context_object_name = 'trabajos'
    template_name = 'estudiantes/trabajos/lista.html'

#
class TrabajoGraduacionFacultadListView(PermissionRequiredMixin, ListView):
    model = TrabajoGraduacion
    permission_required = 'ubicacion.ver_facultad'
    context_object_name = 'trabajos'
    template_name = 'estudiantes/trabajos/lista.html'

    def get_queryset(self):
        qs = TrabajoGraduacion.objects.facultad(facultad=self.kwargs['pk'])
        return qs

#
class TrabajoGraduacionEscuelaListView(PermissionRequiredMixin, ListView):
    model = TrabajoGraduacion
    permission_required = 'ubicacion.ver_escuela'
    context_object_name = 'trabajos'
    template_name = 'estudiantes/trabajos/lista.html'

    def get_queryset(self):
        qs = TrabajoGraduacion.objects.escuela(escuela=self.kwargs['pk'])
        return qs

#
class TrabajoGraduacionPendienteListView(PermissionRequiredMixin, ListView):
    model = TrabajoGraduacion
    permission_required = 'estudiante.change_trabajograduaction'
    context_object_name = 'trabajos'
    template_name = 'estudiantes/trabajos/pendiente.html'

    def get_queryset(self):
        qs = TrabajoGraduacion.objects.pendientes().escuela(escuela=self.kwargs['pk'])
        return qs

#
