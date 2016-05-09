'''
Created on May 8, 2016

@author: Gabriel
'''
import Transaccion

class BilleteraElectronica():
    '''
    classdocs
    '''
    identificador = ""
    nombre = ""
    apellido = ""
    ci = ""
    pin = ""
    saldo = 0
    transacciones = []


    def __init__(self, identificador, nombre, apellido, ci, pin):
        '''
        Constructor
        '''
        self.identificador = identificador
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci
        self.pin = pin
        
    def recargar(self, monto,establecimiento):
        if (monto > 0):
            self.saldo = self.saldo + monto
            self.transacciones.append(Transaccion.Transaccion(monto, establecimiento, 0))
    
    def consumir(self, consumo, establecimiento, pin):
        if (self.saldo >= consumo and self.pin == pin):
            self.saldo = self.saldo - consumo
            self.transacciones.append(Transaccion.Transaccion(consumo, establecimiento, 1))
            return 0
        return -1
    
    def __str__(self): 
        tmp = "\n".join([str(t) for t in self.transacciones])
        return "Billetera electronica: {} {} \nMonto: {} \nTransacciones: \n{}".format(self.nombre, self.apellido, self.saldo, tmp)