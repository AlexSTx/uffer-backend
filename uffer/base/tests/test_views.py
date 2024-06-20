from django.test import TestCase

from base.models import Local, Motorista, Usuario, Veiculo

class TestCases(TestCase):

    def testUsuario(self):
        self.assertEqual(Usuario.objects.all(),True)

    def testMotorista(self):
        self.assertEqual(Motorista.objects.all(),True)

    def testVeiculos(self):
        self.assertEqual(Veiculo.objects.all(),True)

    def testLocais(self):
        self.assertEqual(Local.objects.all(),True)
    
testes = TestCases()

testes.testUsuario()
testes.testMotorista()
testes.testVeiculos()
testes.testLocais()