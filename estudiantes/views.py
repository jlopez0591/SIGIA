from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import permission_required
from dal import autocomplete
from estudiantes.forms import StudentUpdateForm, AnteproyectoForm, ProyectoForm
from estudiantes.models import Estudiante, Anteproyecto, Proyecto
from perfiles.models import Perfil


class EstudianteDetailView(PermissionRequiredMixin, UserPassesTestMixin, DetailView):
    context_object_name = 'estudiante'
    permission_required = ('estudiante.view_estudiante')
    model = Estudiante
    template_name = 'estudiantes/detalle.html'

    def test_func(self):
        return True


class EstudianteUpdateView(PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Estudiante
    permission_required = 'estudiante.change_estudiante'
    form_class = StudentUpdateForm
    template_name = 'form.html'

    def test_func(self):
        return True


class AnteproyectoCreateView(PermissionRequiredMixin, CreateView):
    model = Anteproyecto
    permission_required = 'estudiante.add_anteproyecto'
    template_name = 'form.html'
    form_class = AnteproyectoForm
    success_url = reverse_lazy('core:index')


class AnteproyectoDetailView(PermissionRequiredMixin, DetailView):
    model = Anteproyecto
    permission_required = 'estudiante.change_anteproyecto'
    template_name = 'estudiante/anteproyecto.html'
    context_object_name = 'anteproyecto'


class AnteproyectoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Anteproyecto
    permission_required = 'estudiante.change_anteproyecto'
    template_name = 'form.html'
    fields = ('__all__')


class ProyectoCreateView(PermissionRequiredMixin, CreateView):
    model = Proyecto
    permission_required = 'estudiante.add_proyecto'
    template_name = 'form.html'
    form_class = ProyectoForm
    success_url = reverse_lazy('insight:index')


class ProyectoDetailView(PermissionRequiredMixin, DetailView):
    model = Proyecto
    permission_required = 'estudiante.change_proyecto'
    template_name = 'estudiante/proyecto.html'
    context_object_name = 'proyecto'


class ProyectoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Proyecto
    form_class = ProyectoForm


@permission_required('estudiante.change_anteproyecto')
def aprobar_anteproyecto(request, pk):
    if request.method == 'POST':
        anteproyecto = Anteproyecto.objects.get(pk=pk)
        anteproyecto.estado = 'aprobado'
        anteproyecto.save()
    return redirect('insight:detalle-anteproyecto', pk=pk)


@permission_required('estudiante.change_anteproyecto')
def rechazar_anteproyecto(request, pk):
    if request.method == 'POST':
        anteproyecto = Anteproyecto.objects.get(pk=pk)
        anteproyecto.estado = 'rechazado'
        anteproyecto.save()
    return redirect('insight:detalle-anteproyecto', pk=pk)


@permission_required('estudiante.change_anteproyecto')
def anteproyectos_pendientes(request):
    if request.user.is_superuser:
        anteproyectos = Anteproyecto.objects.pendientes()
    else:
        anteproyectos = Anteproyecto.objects.puede_aprobar(usuario=request.user)
    return render(request, 'estudiantes/anteproyecto/lista.html', {
        'anteproyectos': anteproyectos
    })


def anteproyectos_facultad(request):
    user = request.user
    if user.is_superuser:
        anteproyectos = Anteproyecto.objects.all()
    elif user.has_perms('estudiantes.add_anteproyecto'):
        anteproyectos = Anteproyecto.objects.escuela(usuario=user)
    else:
        anteproyectos = None
    return render(request, 'estudiantes/anteproyecto/lista.html', {
        'anteproyectos': anteproyectos
    })


class EstudianteAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if self.request.user.is_superuser:
            print('test')
            qs = Estudiante.objects.all()
        elif self.request.user.is_authenticated():
            perfil = Perfil.objects.get(usuario=self.request.user)
            codigos = {
                'cod_sede': perfil.cod_sede,
                'cod_facultad': perfil.cod_facultad,
                'cod_escuela': perfil.cod_escuela
            }
            # # usuario = Person.objects.get(pk=self.request.user.pk)
            # carreras = perfil.seccion.carreras.all()
            # # Estudiante.objects.get(**usuario.kwargs_ubicacion())
            # q_objects = Q()
            # for carrera in carreras:
            #     q_objects |= Q(carrera=carrera)
            qs = Estudiante.objects.filter(**codigos)
        else:
            return Estudiante.objects.none()

        if self.q:
            qs = qs.filter(primer_nombre__icontains=self.q)
        return qs


class AnteproyectoAutocomplete(PermissionRequiredMixin, autocomplete.Select2QuerySetView):
    permission_required = 'estudiante.add_anteproyecto'

    def get_queryset(self):
        if self.request.user.is_superuser:
            qs = Anteproyecto.objects.all()
        elif self.request.user.is_authenticated():
            perfil = Perfil.objects.get(usuario=self.request.user)
            qs = Anteproyecto.objects.get(seccion=perfil.seccion)
        else:
            return Anteproyecto.objects.none()

        if self.q:
            qs = qs.filter(nombre_proyecto__icontains=self.q)


@permission_required('estudiante.ver_proyectos_facultad')
def proyectos_facultad(request):
    proyectos = Proyecto.objects.facultad()


@permission_required('estudiante.view_estudiante')
def reporte_estudiante(request, pk):
    pass
