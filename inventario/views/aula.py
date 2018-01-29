from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.urls import reverse_lazy

from inventario.forms import AulaForm
from inventario.models import Aula
from ubicacion.models import UnidadInstancia
from django.contrib.messages.views import SuccessMessageMixin

class AulaListView(ListView):
    paginate_by = 10
    model = Aula
    template_name = 'inventario/aula/lista.html'
    context_object_name = 'aulas'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Aula.objects.all()
        elif self.request.user.is_authenticated:
            return Aula.objects.filter(ubicacion=self.request.user.perfil.unidad)
        else:
            return False


class AulaFacultadListView(ListView):
    paginate_by = 10
    model = Aula
    template_name = 'inventario/aula/lista.html'
    context_object_name = 'aulas'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            pk = self.kwargs['pk']
            try:
                u = UnidadInstancia.objects.get(pk=pk)
                aulas = u.aula_set.all()
            except:
                aulas = None
            return aulas
        else:
            return None


class AulaDetailView(DetailView):
    context_object_name = 'aula'
    model = Aula
    template_name = 'inventario/aula/detalle.html'


class AulaCreateView(SuccessMessageMixin, CreateView):
    model = Aula
    form_class = AulaForm
    template_name = 'inventario/aula/crear.html'
    success_url = reverse_lazy('inventario:lista-aulas')
    success_message = 'Aula registrada'

    def form_valid(self, form):
        form.instance.cod_sede = self.request.user.perfil.cod_sede
        form.instance.cod_unidad = self.request.user.perfil.cod_unidad
        return super(AulaCreateView, self).form_valid(form)


class AulaUpdateView(UpdateView):
    model = Aula
    template_name = 'inventario/aula/crear.html'
    form_class = AulaForm
    success_url = reverse_lazy('inventario:lista-aulas')