'''
Created on May 8, 2016

@author: Gabriel
'''
import datetime
class Transaccion(object):
    '''
    classdocs
    '''
    monto = 0
    fecha = datetime.datetime.today()
    id_establecimiento = ""
    tipo = 0

    def __init__(self, monto, id_establecimiento, tipo):
        '''
        Constructor
        '''
        self.monto = monto
        self.id_establecimiento = id_establecimiento
        self.tipo = tipo
        
    def __str__(self):
        tmp = "Recarga"
        if (self.tipo == 1):
            tmp = "Consumo"
        return ("[{}] :: {} en el establecimiento {} por {}".format(self.fecha, tmp, self.id_establecimiento, self.monto))
        
        