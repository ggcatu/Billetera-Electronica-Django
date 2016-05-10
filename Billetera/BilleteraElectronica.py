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

    def recargar(self, monto,establecimiento):
        if (monto > 0):
            self.__saldo = self.__saldo + monto
            self.recargas.append(Transaccion(monto, establecimiento, 0))
    
    def consumir(self, consumo, establecimiento, pin):
        if (self.__saldo >= consumo and self.__pin == pin):
            self.__saldo = self.__saldo - consumo
            self.consumos.append(Transaccion(consumo, establecimiento, 1))
            return 0
        return -1
    
    def __str__(self): 
        tmp = "\n".join([str(t) for t in self.transacciones])
        return "Billetera electronica: {} {} \nMonto: {} \nTransacciones: \n{}"\
                        .format(self.nombre, self.apellido, self.__saldo, tmp)