from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from solicitud.models import Solicitud, Comentario
from solicitud.forms import SolicitudForm, ComentarioForm


# Create your views here.
class SolicitudListview(ListView):
    context_object_name = 'solicitudes'
    model = Solicitud
    paginate_by = 10
    queryset = Solicitud.objects.filter(resuelto=False).order_by('-fecha_creacion')
    template_name = 'solicitud/lista.html'


class SolicitudDetailView(DetailView):
    context_object_name = 'solicitud'
    model = Solicitud
    template_name = 'solicitud/detalle.html'

    def get_context_data(self, **kwargs):
        context = super(SolicitudDetailView, self).get_context_data(**kwargs)
        context['titulo'] = self.object.titulo
        context['form'] = ComentarioForm
        return context


def detalle_solicitud(request, solicitud_pk):
    solicitud = get_object_or_404(Solicitud, pk=solicitud_pk)
    qs = Comentario.objects.filter(solicitud=solicitud)
    form = ComentarioForm()
    paginator = Paginator(qs, 10)
    page = request.GET.get('page')
    try:
        comentarios = paginator.page(page)
    except PageNotAnInteger:
        comentarios = paginator.page(1)
    except EmptyPage:
        comentarios = paginator.page(paginator.num_pages)
    # TODO: Comentario Form
    return render(request, '', {
        'solicitud': solicitud,
        'comentarios': comentarios,
        'form': form
    })


class SolicitudCreateView(CreateView):
    model = Solicitud
    template_name = 'form.html'
    form_class = SolicitudForm

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(SolicitudCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SolicitudCreateView, self).get_context_data()
        context['boton'] = 'Solicitud'
        context['titulo'] = 'Crear Solicitud'
        return context


class SolicitudUpdateView(UpdateView):
    model = Solicitud
    form_class = SolicitudForm
    template_name = 'form.html'

    def form_valid(self, form):
        super(SolicitudUpdateView, self).form_valid(form)


class UserSolicitudView(ListView):
    context_object_name = 'solicitudes'
    model = Solicitud
    paginate_by = 10
    template_name = 'solicitud/lista.html'

    def get_context_data(self, **kwargs):
        context = super(UserSolicitudView, self).get_context_data()
        context['titulo'] = 'Mis solicitudes'
        return context

    def get_queryset(self):
        return Solicitud.objects.filter(usuario=self.request.user)


@login_required
def crear_comentario(request, solicitud_pk):
    solicitud = get_object_or_404(Solicitud, pk=solicitud_pk)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.solicitud = solicitud
            comentario.usuario = request.user
            comentario.save()
            solicitud_url = reverse('solicitud:detalle', kwargs={'pk': solicitud_pk})
            return redirect(solicitud_url)
    else:
        form = ComentarioForm()
    return render(request, 'form.html', {'form': form})


class ResolverSolicitudView(View):
    def dispatch(self, request, *args, **kwargs):
        super(ResolverSolicitudView, self).dispatch(request)

    def post(self, request, *args, **kwargs):
        solicitud = Solicitud.objects.get(pk=self.kwargs['pk'])
        solicitud.resolver()
        return redirect('insight:index')

    def get(self):
        # TODO: Add Error Code for 'Not allowed'.
        return redirect('insight:index')
