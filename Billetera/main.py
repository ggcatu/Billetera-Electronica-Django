'''
Created on May 8, 2016

@author: Gabriel Gimenez
'''
import BilleteraElectronica
from decimal import *

if __name__ == '__main__':
    identificador = "03023424"
    nombre = "Gabriel"
    apellido = "Gimenez"
    ci = "V24313661"
    pin = "1343"
    me = BilleteraElectronica.BilleteraElectronica(identificador, nombre, apellido, ci, pin)
    me.recargar(Decimal(50), 30)
    me.recargar(Decimal(50), 35)
    me.recargar(Decimal(50), 32)
    me.consumir(Decimal(100), 32, "1343")
    print(me)
    