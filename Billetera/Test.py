from BilleteraElectronica import BilleteraElectronica
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
		self.me.recargar(50402,31)
		self.assertEqual(self.me.saldo(),50402)

	def testRecargarMontoValido(self):
		self.me.recargar(50,31)
		self.assertEqual(self.me.saldo(), 50)
	
	def testConsumirValido(self):
		self.me.recargar(50,21)
		self.me.consumir(25,32,"1343")
		self.assertEqual(self.me.saldo(),25)


	#Casos Maliciosos

	def testRecargarMontoIgualACero(self):
		saldoInicial = self.me.saldo()
		self.me.recargar(0, -1)
		self.assertEqual(self.me.saldo(), saldoInicial)

	def testConsumirMontoIgualACero(self):
		saldoInicial = self.me.saldo()
		self.me.consumir(0,10,"1343")
		self.assertEqual(saldoInicial,self.me.saldo())

	def testConsumirPinVacio(self):
		saldoInicial = self.me.saldo()
		with self.assertRaises(ValueError):
			self.me.consumir(0,0, "")
		self.assertEqual(saldoInicial,self.me.saldo())

	#Casos Borde
	
	def testRecargarMontoNegativo(self):
		saldoInicial = self.me.saldo()
		with self.assertRaises(ValueError) as cm:
			self.me.recargar(-10,31)

		self.assertEqual(cm.exception.args[1],3)
		self.assertEqual(self.me.saldo(),saldoInicial)

	def testConsumirMontoNegativo(self):
		self.me.recargar(50,3)
		with self.assertRaises(ValueError) as cm:
			self.me.consumir(-1, 31, "1343")
		self.assertEqual(cm.exception.args[1], 0)
		self.assertEqual(self.me.saldo(),50)

	
	def testConsumirPinErroneo(self):
		self.me.recargar(50,3)
		with self.assertRaises(ValueError) as cm:
			self.me.consumir(50, 31, "0000")
		self.assertEqual(cm.exception.args[1], 1)
		self.assertEqual(self.me.saldo(),50)

	
	def testConsumirSaldoInsuficiente(self):
		self.me.recargar(50,3)
		with self.assertRaises(ValueError) as cm:
			self.me.consumir(100, 31, "1343")
		self.assertEqual(cm.exception.args[1], 2)
		self.assertEqual(self.me.saldo(),50)

	#Casos Esquina

	def testConsumirPinErroneoMontoNegativo(self):
		self.me.recargar(50,3)
		with self.assertRaises(ValueError) as cm:
			self.me.consumir(-1, 31, "0023")
		self.assertEqual(self.me.saldo(),50)

	def testConsumirSaldoInsuficientePinErroneo(self):
		with self.assertRaises(ValueError):
			self.me.consumir(50,31,"4333")


if __name__ == "__main__":
	unittest.main()
		

