from django.test import TestCase
from ubicacion.models import Sede, Facultad, Escuela, Departamento, Carrera, FacultadInstancia, EscuelaInstancia, \
    DepartamentoInstancia, CarreraInstancia


class AutoUbicacionTestCase(TestCase):
    fixtures = ['sede.json', 'facultad.json', 'escuela.json', 'departamento.json', 'carrera.json', ]

    def setUp(self):
        FacultadInstancia.objects.create(cod_sede='1', cod_facultad='24')
        FacultadInstancia.objects.create(cod_sede='01', cod_facultad='25')  # Prueba de no asignar al faltar facultad
        FacultadInstancia.objects.create(cod_sede='X1', cod_facultad='24')
        EscuelaInstancia.objects.create(cod_sede='1', cod_facultad='24', cod_escuela='2')
        DepartamentoInstancia.objects.create(cod_sede='1', cod_facultad='24', cod_departamento='D1')
        CarreraInstancia.objects.create(cod_sede='1', cod_facultad='24', cod_escuela='2', cod_carrera='1')

    def test_facultadinstancia_auto_ubicacion(self):
        '''
        Revisa que se asignen de manera automatica las FK a Sede y Facultad
        :return:
        '''
        s = Sede.objects.get(cod_sede='1')
        f = Facultad.objects.get(cod_facultad='24')
        fi = FacultadInstancia.objects.get(cod_sede='1', cod_facultad='24')
        self.assertEqual(fi.sede, s)
        self.assertEqual(fi.facultad, f)

    def test_facultadinstancia_auto_ubicacion_sede_fail(self):
        fi = FacultadInstancia.objects.get(cod_sede='X1', cod_facultad='24')
        self.assertEqual(fi.sede, None)

    def test_facultadinstancia_auto_ubicacion_facultad_fail(self):
        fi = FacultadInstancia.objects.get(cod_sede='01', cod_facultad='25')
        self.assertEqual(fi.facultad, None)

    def test_escuelainstancia_auto_ubicacion(self):
        s = Sede.objects.get(cod_sede='1')
        f = Facultad.objects.get(cod_facultad='24')
        e = Escuela.objects.get(cod_facultad='24', cod_escuela='2')
        ei = EscuelaInstancia.objects.get(cod_sede='1', cod_facultad='24', cod_escuela='2')
        self.assertEqual(ei.sede, s)
        self.assertEqual(ei.facultad, f)
        self.assertEqual(ei.escuela, e)

    def test_departamentoinstancia_auto_ubicacion(self):
        s = Sede.objects.get(cod_sede='1')
        f = Facultad.objects.get(cod_facultad='24')
        d = Departamento.objects.get(cod_facultad='24', cod_departamento='D1')
        di = DepartamentoInstancia.objects.get(cod_sede='1', cod_facultad='24', cod_departamento='D1')
        self.assertEqual(di.sede, s)
        self.assertEqual(di.facultad, f)
        self.assertEqual(di.departamento, d)

    def test_carrerainstancia_auto_ubicacion(self):
        s = Sede.objects.get(cod_sede='1')
        f = Facultad.objects.get(cod_facultad='24')
        e = Escuela.objects.get(cod_facultad='24', cod_escuela='2')
        c = Carrera.objects.get(cod_facultad='24', cod_escuela='2', cod_carrera='1')
        ci = CarreraInstancia.objects.get(cod_sede='1', cod_facultad='24', cod_escuela='2', cod_carrera='1')
        self.assertEqual(ci.sede, s)
        self.assertEqual(ci.facultad, f)
        self.assertEqual(ci.escuela, e)
        self.assertEqual(ci.carrera, c)
