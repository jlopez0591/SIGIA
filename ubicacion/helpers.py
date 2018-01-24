from ubicacion.models import Sede, Unidad, Seccion, Carrera, UnidadInstancia, SeccionInstancia, CarreraInstancia


def get_sede(cod_sede):
    return Sede.objects.get(cod_sede=cod_sede)
