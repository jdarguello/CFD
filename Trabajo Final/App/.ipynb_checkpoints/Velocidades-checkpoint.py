import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#---Perfil de velocidades---
def Perfil(datos, size=(12,5)):
    precision = 18
    fig = plt.figure(figsize=size)
    X, Y = np.meshgrid(np.linspace(0, datos['Geo']['Ox [m]'], precision), 
                       np.linspace(0, datos['Geo']['h [m]'], precision))

    U = 1.5*(datos['Fluido']['Constante del flujo de entrada']*Y*\
             (datos['Geo']['h [m]']-Y))/(datos['Geo']['h [m]']**2)
    V = X*0
    #Valores de velocidad
    Vs = []
    suma = 0
    for i in range(precision):
        Vs.append(U[i][0])

    #Gráfica
    norm = matplotlib.colors.Normalize(
        vmin = np.min(U),
        vmax = np.max(U))
    #norm.autoscale(Vs)
    cm = matplotlib.cm.copper
    sm = matplotlib.cm.ScalarMappable(cmap=cm, norm=norm)
    sm.set_array([])
    plt.quiver(X,Y,U,V)
    #plt.colorbar(sm)
    plt.show()