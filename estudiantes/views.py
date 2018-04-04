from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import permission_required
from dal import autocomplete
from estudiantes.forms import StudentUpdateForm, AnteproyectoForm, ProyectoForm
from estudiantes.models import Estudiante, Anteproyecto, Proyecto
from perfiles.models import Perfil


class EstudianteFacultadListview(ListView):
    context_object_name = 'estudiantes'
    model = Estudiante
    template_name = 'estudiantes/consultar.html'

    def get_queryset(self):
        qs = Estudiante.objects.filter(facultad_id=self.kwargs['pk'])
        return qs


class EstudianteEscuelaListView(ListView):
    context_object_name = 'estudiantes'
    model = Estudiante
    template_name = 'estudiantes/consultar.html'

    def get_queryset(self):
        qs = Estudiante.objects.filter(escuela_id=self.kwargs['pk'])
        return qs


class EstudianteListView(PermissionRequiredMixin, ListView):
    permission_required = ('estudiante.view_estudiante')
    context_object_name = 'estudiantes'
    model = Estudiante
    template_name = 'estudiantes/consultar.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            qs = Estudiante.objects.all()
        elif self.request.user.perfil.escuela:
            # TODO: Manager para estudiante
            qs = Estudiante.objects.filter(escuela=self.request.user.perfil.escuela)
        return qs


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
    template_name = 'estudiantes/editar.html'

    def test_func(self):
        return True


class AnteproyectoCreateView(PermissionRequiredMixin, CreateView):
    model = Anteproyecto
    permission_required = 'estudiante.add_anteproyecto'
    template_name = 'estudiantes/anteproyecto/crear.html'
    form_class = AnteproyectoForm
    success_url = reverse_lazy('estudiante:anteproyectos-unidad')

    def form_valid(self, form):
        form.instance.registrado_por = self.request.user
        try:
            return super(AnteproyectoCreateView, self).form_valid(form)
        except IntegrityError:
            return self.form_invalid(form)


class AnteproyectoFacultadListView(ListView):
    model = Anteproyecto
    context_object_name = 'anteproyectos'
    template_name = 'estudiantes/anteproyecto/lista.html'

    def get_queryset(self):
        qs = Anteproyecto.objects.filter(facultad_id=self.kwargs['pk']).aprobados()
        return qs


class AnteproyectoEscuelaListView(ListView):
    model = Anteproyecto
    context_object_name = 'anteproyectos'
    template_name = 'estudiantes/anteproyecto/lista.html'

    def get_queryset(self):
        qs = Anteproyecto.objects.filter(escuela_id=self.kwargs['pk']).aprobados()
        return qs


class AnteproyectoPendienteEscuelaListView(ListView):
    model = Anteproyecto
    context_object_name = 'anteproyectos'
    template_name = 'estudiantes/anteproyecto/pendiente.html'

    def get_queryset(self):
        qs = Anteproyecto.objects.puede_aprobar(self.request.user)
        return qs


class AnteproyectoDetailView(PermissionRequiredMixin, DetailView):
    model = Anteproyecto
    permission_required = 'estudiante.change_anteproyecto'
    template_name = 'estudiantes/anteproyecto/detalle.html'
    context_object_name = 'anteproyecto'

    # def get_object(self, queryset=None):
    #     object = super(AnteproyectoDetailView, self).get_object()
    #     if self.request.user.perfil.escuela is not object.escuela:
    #         Http403()
    #     return object


class AnteproyectoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Anteproyecto
    permission_required = 'estudiante.change_anteproyecto'
    template_name = 'estudiantes/anteproyecto/crear.html'
    form_class = AnteproyectoForm

    def form_valid(self, form):
        form.instance.estado = 'pendiente'
        return super(AnteproyectoUpdateView, self).form_valid(form)


class ProyectoCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Proyecto
    permission_required = 'estudiante.add_proyecto'
    template_name = 'estudiantes/proyecto/crear.html'
    form_class = ProyectoForm
    success_url = reverse_lazy('core:index')
    success_message = 'Proyecto Creado'



class ProyectoFacultadListView(ListView):
    model = Proyecto
    template_name = 'estudiantes/proyecto/lista.html'
    context_object_name = 'proyectos'

    def get_queryset(self):
        qs = Proyecto.objects.filter(facultad_id=self.kwargs['pk'])
        return qs


class ProyectoEscuelaListView(ListView):
    model = Proyecto
    template_name = 'estudiantes/proyecto/lista.html'
    context_object_name = 'proyectos'

    def get_queryset(self):
        qs = Proyecto.objects.filter(escuela_id=self.kwargs['pk'])
        return qs


class ProyectoDetailView(PermissionRequiredMixin, DetailView):
    model = Proyecto
    permission_required = 'estudiante.change_proyecto'
    template_name = 'estudiantes/proyecto/detalle.html'
    context_object_name = 'proyecto'
    permission_required = 'proyecto:change_proyecto'


class ProyectoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'estudiantes/proyecto/crear.html'
    permission_required = 'proyecto:change_proyecto'


@permission_required('estudiante.change_anteproyecto')
def aprobar_anteproyecto(request, pk):
    if request.method == 'POST':
        anteproyecto = Anteproyecto.objects.get(pk=pk)
        anteproyecto.aprobar()
    return redirect('estudiante:anteproyecto-detalle', pk=pk)


@permission_required('estudiante.change_anteproyecto')
def rechazar_anteproyecto(request, pk):
    if request.method == 'POST':
        anteproyecto = Anteproyecto.objects.get(pk=pk)
        anteproyecto.estado = 'rechazado'
        anteproyecto.save()
    return redirect('estudiante:anteproyecto-detalle', pk=pk)


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
        anteproyectos = Anteproyecto.objects.aprobados()
    elif user.has_perms('estudiantes.add_anteproyecto'):
        anteproyectos = Anteproyecto.objects.aprobados().escuela(usuario=user)
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
    if request.user.is_superuser:
        qs = Anteproyecto.objects.aprobados()
    elif request.user.perfil.escuela:
        # TODO: Manager para anteproyectos
        qs = Anteproyecto.objects.aprobados().filter(escuela=request.user.perfil.escuela)
    else:
        qs = None
    return render(request, 'estudiantes/proyecto/lista.html', {'proyectos': qs})


@permission_required('estudiante.view_estudiante')
def reporte_estudiante(request, pk):
    pass
