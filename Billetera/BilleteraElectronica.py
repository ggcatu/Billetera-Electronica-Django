'''
Created on May 8, 2016

@author: Gabriel
@author: Erick
'''

from Transaccion import Transaccion
from decimal import *

class BilleteraElectronica():
	'''
	classdocs
	'''

	def __init__(self, identificador, nombre, apellido, ci, pin):
		'''
		Constructor
		'''
		self.identificador = identificador
		self.nombre = nombre
		self.apellido = apellido
		self.ci = ci
		self.__pin = pin
		self.__saldo = Decimal('0')
		self.__consumos = []
		self.__recargas = []

		# Nos aseguramos que la precision de decimal sea suficientemente alta.
		getcontext().prec = 40


	def saldo(self):
		return Decimal(self.__saldo)
	
	def consumir(self, consumo, establecimiento, pin):
		if type(consumo) != Decimal:
			raise ValueError("Monto de consumo invalido",0)

		if establecimiento is None:
			raise ValueError("Establecimiento nulo en recarga",1)
		
		if (consumo < 0):
			raise ValueError("Valor de consumo negativo",2)

		if (pin is None or self.__pin != pin):
			raise ValueError("Pin incorrecto en consumo",3)

		if (self.__saldo < consumo):
			raise ValueError("Saldo menor al consumo",4)



		self.__saldo = self.__saldo - consumo
		self.__consumos.append(Transaccion(consumo, establecimiento, 1))
		return 1


	def recargar(self, monto,establecimiento):
		if type(monto) != Decimal:
			raise ValueError("Monto de recarga invalido",5)
		if (monto < Decimal(0)):
			raise ValueError("Monto de recarga negativo",6)
		if establecimiento is None:
			raise ValueError("Establecimiento nulo en recarga",7)


		self.__saldo = Decimal(self.__saldo) + Decimal(monto)
		self.__recargas.append(Transaccion(monto, establecimiento, 0))

	
	def __str__(self): 
		tmp = "\n".join([str(t) for t in self.__consumos + self.__recargas])
	
		return "Billetera electronica: {} {} \nMonto: {} \nTransacciones: \n{}"\
						.format(self.nombre, self.apellido, self.__saldo, tmp)
