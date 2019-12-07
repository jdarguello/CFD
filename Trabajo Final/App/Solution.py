from fenics import *
import numpy as np
import matplotlib.pyplot as plt

class Sol():
    def __init__(self, datos, mesh, size=(16,10)):
        entrada, salida, muros, cilindro = self.BC(datos['Geo'])
        #
        
    
    def BC(self, Geo):
        def string(num):
            return str(round(num,3))
        numero = 2    #Divisor
        entrada = 'near(x[0], 0)'
        salida = 'near(x[0], ' + string(Geo['l [m]']) + ')'
        muros = 'near(x[1], 0) || near(x[1], ' + string(Geo['h [m]']) + ')'
        cilindro = 'on_boundary && x[0]>' + string(Geo['Ox [m]'] - Geo['D [m]']/numero) \
            + ' && x[0]<' + string(Geo['D [m]']/numero + Geo['Ox [m]']) + ' && x[1]>' \
            + string(Geo['Oy [m]'] - Geo['D [m]']/numero) \
            + ' && x[1]<' + string(Geo['D [m]']/numero + Geo['Oy [m]'])
        return entrada, salida, muros, cilindro