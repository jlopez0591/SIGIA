from django.test import TestCase
from ubicacion.models import Sede, Facultad, FacultadInstancia


class FacultadInstanciaTestCase(TestCase):
    def setUp(self):
        Sede.objects.create(cod_sede='01', nombre='Campus')
        Facultad.objects.create(cod_facultad='24', nombre='FIEC')
        FacultadInstancia.objects.create(cod_sede='01', cod_facultad='24')
        FacultadInstancia.objects.create(cod_sede='01', cod_facultad='25') # Prueba de no asignar al faltar facultad
        FacultadInstancia.objects.create(cod_sede='X1', cod_facultad='24')

    def test_facultadinstancia_auto_ubicacion(self):
        '''
        Revisa que se asignen de manera automatica las FK a Sede y Facultad
        :return:
        '''
        s = Sede.objects.get(cod_sede='01')
        f = Facultad.objects.get(cod_facultad='24')
        fi = FacultadInstancia.objects.get(cod_sede='01', cod_facultad='24')
        self.assertEqual(fi.sede, s)
        self.assertEqual(fi.facultad, f)

    def test_facultadinstancia_auto_ubicacion_sede_fail(self):
        fi = FacultadInstancia.objects.get(cod_sede='X1', cod_facultad='24')
        self.assertEqual(fi.sede, None)

    def test_facultadinstancia_auto_ubicacion_facultad_fail(self):
        fi = FacultadInstancia.objects.get(cod_sede='01', cod_facultad='25')
        self.assertEqual(fi.facultad, None)
