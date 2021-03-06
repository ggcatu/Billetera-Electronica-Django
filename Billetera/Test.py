'''
Created on May 10, 2016

@author: Gabriel
@author: Erick
'''

from BilleteraElectronica import BilleteraElectronica
from decimal import *
import unittest

class BilleteraTest(unittest.TestCase):
	
	def setUp(self):
		identificador = "03023424"
		nombre = "Gabriel"
		apellido = "Gimenez"
		ci = "V24313661"
		pin = "1343"
		self.me = BilleteraElectronica(identificador, nombre, apellido, ci, pin)
	
	def tearDown(self):
		self.me = None
	
	#Casos Internos

	def testSaldo(self):
		self.me.recargar(Decimal(50402),31)
		self.assertEqual(self.me.saldo(),Decimal(50402))

	def testRecargarMontoValido(self):
		self.me.recargar(Decimal(50),31)
		self.assertEqual(self.me.saldo(),Decimal(50))
	
	def testRecargarNumerosAltos(self):
		self.me.recargar(Decimal('50323333333333333333333333333332.54232355'),4)
		self.assertEqual(self.me.saldo(),Decimal('50323333333333333333333333333332.54232355'))

	def testConsumirValido(self):
		self.me.recargar(Decimal(50),21)
		self.me.consumir(Decimal(25),32,"1343")
		self.assertEqual(self.me.saldo(),Decimal(25))

	def testConsumirNumerosAltos(self):
		self.assertEqual(self.me.saldo(),Decimal(0))
		self.me.recargar(Decimal('50000000000000000000000000000000000000000000'),32)
		self.me.consumir(Decimal('45555555553434233333333333.4323334'),42,"1343")
		self.assertEqual(self.me.saldo(), Decimal('50000000000000000000000000000000000000000000') - Decimal('45555555553434233333333333.4323334'))

	#Casos Maliciosos

	def testRecargarDecimales(self):
		self.me.recargar(Decimal('0.000001'),44)
		self.assertEqual(self.me.saldo(),Decimal('0.000001'))


	def testConsumirDecimales(self):
		self.me.recargar(Decimal('0.000001'),44)
		self.me.consumir(Decimal('0.0000001'),43,"1343")
		self.assertEqual(self.me.saldo(),Decimal('0.000001') - Decimal('0.0000001'))

	def testRecargarMontoIgualACero(self):
		saldoInicial = self.me.saldo()
		self.me.recargar(Decimal(0), -1)
		self.assertEqual(self.me.saldo(), saldoInicial)

	def testConsumirMontoIgualACero(self):
		saldoInicial = self.me.saldo()
		self.me.consumir(Decimal(0),10,"1343")
		self.assertEqual(saldoInicial,self.me.saldo())

	def testConsumirPinVacio(self):
		saldoInicial = self.me.saldo()
		with self.assertRaises(ValueError):
			self.me.consumir(Decimal(0),0, "")
		self.assertEqual(saldoInicial,self.me.saldo())

	# Casos de entrada Invalida

	def testRecargarMontoDeTipoInvalido(self):
		saldoInicial = self.me.saldo()
		with self.assertRaises(ValueError) as e:
			self.me.recargar("50",3)
		self.assertEqual(e.exception.args[1],5)
		self.assertEqual(self.me.saldo(),saldoInicial)


	def testRecargarEstablecimientoEsNone(self):
		saldoInicial = self.me.saldo()
		with self.assertRaises(ValueError) as e:
			self.me.recargar(Decimal(40),None)
		self.assertEqual(e.exception.args[1],7)
		self.assertEqual(self.me.saldo(),saldoInicial)


	def testConsumirMontoDeTipoInvalido(self):
		self.me.recargar(Decimal(50),2)
		saldoInicial = self.me.saldo()
		with self.assertRaises(ValueError) as e:
			self.me.consumir("50",3,"1343")
		self.assertEqual(e.exception.args[1],0)
		self.assertEqual(self.me.saldo(),saldoInicial)

	def testConsumirEstablicimientoEsNone(self):
		self.me.recargar(Decimal(50),2)
		saldoInicial = self.me.saldo()
		with self.assertRaises(ValueError) as e:
			self.me.consumir(Decimal(50),None,"1343")
		self.assertEqual(e.exception.args[1],1)
		self.assertEqual(self.me.saldo(),saldoInicial)

	def testConsumirPinEsNone(self):
		self.me.recargar(Decimal(50),2)
		saldoInicial = self.me.saldo()
		with self.assertRaises(ValueError) as e:
			self.me.consumir(Decimal(40),4,None)
		self.assertEqual(e.exception.args[1],3)
		self.assertEqual(self.me.saldo(),saldoInicial)

	#Casos Borde
	
	def testRecargarMontoNegativo(self):
		saldoInicial = self.me.saldo()
		with self.assertRaises(ValueError) as cm:
			self.me.recargar(Decimal(-10),31)

		self.assertEqual(cm.exception.args[1],6)
		self.assertEqual(self.me.saldo(),saldoInicial)

	def testConsumirMontoNegativo(self):
		self.me.recargar(Decimal(50),2)
		with self.assertRaises(ValueError) as cm:
			self.me.consumir(Decimal(-1), 31, "1343")
		self.assertEqual(cm.exception.args[1], 2)
		self.assertEqual(self.me.saldo(),Decimal(50))

	
	def testConsumirPinErroneo(self):
		self.me.recargar(Decimal(50),2)
		with self.assertRaises(ValueError) as cm:
			self.me.consumir(Decimal(50), 31, "0000")
		self.assertEqual(cm.exception.args[1], 3)
		self.assertEqual(self.me.saldo(),Decimal(50))

	
	def testConsumirSaldoInsuficiente(self):
		self.me.recargar(Decimal(50),3)
		with self.assertRaises(ValueError) as cm:
			self.me.consumir(Decimal(100), 31, "1343")
		self.assertEqual(cm.exception.args[1], 4)
		self.assertEqual(self.me.saldo(),Decimal(50))

	#Casos Esquina

	def testConsumirPinErroneoMontoNegativo(self):
		self.me.recargar(Decimal(50),2)
		with self.assertRaises(ValueError) as cm:
			self.me.consumir(Decimal(-1), 31, "0023")
		self.assertEqual(self.me.saldo(),Decimal(50))

	def testConsumirSaldoInsuficientePinErroneo(self):
		with self.assertRaises(ValueError):
			self.me.consumir(Decimal(50),31,"4333")


	def testRecargarNumero(self):
		self.me.recargar(Decimal(50),4)
		self.assertEqual(self.me.saldo(), Decimal(50))	


if __name__ == "__main__":
	unittest.main()
		

