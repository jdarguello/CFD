import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML, display
from ipywidgets import interact, interactive, interact_manual
try:
	from App.Preprocessing.Geometry import *
except:
	from Geometry import *

class Element():
	"""
		Desarrolla el dibujo del elemento
	"""
	def esquemaN(self, Es, nodos, color = 'black'):
		Es.scatter(nodos[:, [0]], nodos[:, [1]], c=color)
	def esquemaEL(self, Es, nodos, color = 'black'):
		for i in range(1,len(nodos)):
			Es.plot(
				[nodos[i-1][0], nodos[i][0]],
				[nodos[i-1][1], nodos[i][1]],
				color=color
			)


class Cuad4(Element):
	"""
		Elemento cuadrangular 2D de 4 nodos.

		SE DEBE HACER UNA BASE DE DATOS DE PUNTOS:

			Núm nodo 	x	y

		Elementos

			Núm El 		Nodo1	Nodo2	Nodo3	Nodo4

	"""
	def __init__(self, tam, Es, init=[0,0]):
		#Ubicación de nodos
		nodos = self.nodes(init,tam)
		#Esquema - nodos
		self.esquemaN(Es, nodos)
		#Esquema - Elementos
		self.esquemaEL(Es, nodos)

	def nodes(self, init, tam):
		points = np.zeros((4,2))
		for i in range(len(points)):
			if i == 0:
				points[i][0] = init[0]
				points[i][1] = init[1]
			else:
				abajo = True
				for j in range(2):
					points[i][j] = points[i-1][j]
					if abajo and points[i-1][j] == init[j]:
						points[i][j] = init[j] + tam[j]
						abajo = False
				if abajo:
					points[i][0] = init[0]
		return points

class Cuad8():
	"""
		Elemento cuadrangular 2D de 8 nodos.
	"""
	def __init__(self, tam, num = 1, init=[0,0]):
		pass
    
class Tri3():
	"""
		Elemento triangular 2D de 3 nodos.
	"""
	def __init__(self, tam, num = 1, init=[0,0]):
		pass

class Tri6():
	"""
		Elemento triangular 2D de 6 nodos.
	"""
	def __init__(self, tam, num = 1, init=[0,0]):
		pass

class Malla(Geo):
	"""
		OBJETIVO:
			Desarrolla la malla para simulación numérica y almacena la
			ínformación de los nodos y elementos.

		ARGUMENTOS:
			- dom 	->	Dominio o figura a mallar.
			- Eltype ->	Tipo de elemento.
			- El 	 ->	Dimensiones de los elementos estándar
			- ref	 ->	Refinamiento de curvatura
			- num 	 ->	Vector booleano para numeración de nodos y elementos
	"""
	def __init__(self, El, num, ref, dom=False, Eltype = 'Cuad4'):
		#Dominio General - Frontera
		if dom:
			super().__init__(dom)
		#Dibujo de los elementos
		coord = [0,0]
		for x in range(int(dom['a']['Valor']/El[0])):
			for y in range(int(dom['h']['Valor']/El[1])):
				if Eltype == 'Cuad4':
					Cuad4(El, self.ax, coord)
				coord[1] += El[1]
			coord[0] += El[0]
			coord[1] = 0

		#Gráfica
		plt.show()



if __name__ == '__main__':
	data = {
	    'Geometría': {
	        'a': {
	            'Valor':8,
	            'Units': 'm'
	        },
	        'h': {
	            'Valor': 10,
	            'Units': 'm'
	        },
	        'r': {
	            'Valor': 2,
	            'Units': 'm'
	        }
	    },
	    'Propiedades': {
	        'E': {
	            'Valor': 200E6,
	            'Units': 'MPa'
	        },
	        'v': {
	            'Valor': 0.3,
	            'Units': ''
	        }
	    }
	}
	Malla((0.5,0.5), (False, False), 0,  data['Geometría'])

