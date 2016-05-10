'''
Created on May 8, 2016

@author: Gabriel
'''
from Transaccion import Transaccion

class BilleteraElectronica():
	'''
	classdocs
	'''
	identificador = ""
	nombre = ""
	apellido = ""
	ci = ""
	__pin = ""
	__saldo = 0
	consumos = []
	recargas = []

	def __init__(self, identificador, nombre, apellido, ci, pin):
		'''
		Constructor
		'''
		self.identificador = identificador
		self.nombre = nombre
		self.apellido = apellido
		self.ci = ci
		self.__pin = pin
		
	def saldo(self):
		return self.__saldo
	
	def consumir(self, consumo, establecimiento, pin):
		if type(consumo) not in (int, float):
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
		self.consumos.append(Transaccion(consumo, establecimiento, 1))
		return 1


	def recargar(self, monto,establecimiento):
		if type(monto) not in (int, float):
			raise ValueError("Monto de recarga invalido",5)
		if (monto < 0):
			raise ValueError("Monto de recarga negativo",6)
		if establecimiento is None:
			raise ValueError("Establecimiento nulo en recarga",7)

	
		self.__saldo = self.__saldo + monto
		self.recargas.append(Transaccion(monto, establecimiento, 0))

	
	def __str__(self): 
		tmp = "\n".join([str(t) for t in self.consumos + self.recargas])
	
		return "Billetera electronica: {} {} \nMonto: {} \nTransacciones: \n{}"\
						.format(self.nombre, self.apellido, self.__saldo, tmp)
