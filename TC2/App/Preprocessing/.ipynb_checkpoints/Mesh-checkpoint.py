import matplotlib.pyplot as plt
from ipywidgets import interact, interactive, interact_manual
from Geometry import *

class Cuad4():
	"""
		Elemento cuadrangular 2D de 4 nodos.
	"""
	def __init__(self):
		pass

class Cuad8():
	"""
		Elemento cuadrangular 2D de 8 nodos.
	"""
	def __init__(self):
		pass
    
class Tri3():
	"""
		Elemento triangular 2D de 3 nodos.
	"""
	def __init__(self):
		pass

class Tri6():
	"""
		Elemento triangular 2D de 6 nodos.
	"""
	def __init__(self):
		pass

class Malla(Geo):
	"""
		OBJETIVO:
			Desarrolla la malla para simulación numérica y almacena la
			ínformación de los nodos y elementos.

		ARGUMENTOS:
			- dom 	->	Dominio o figura a mallar.
			- Eltype ->	Tipo de elemento.
	"""
	def __init__(self, dom, Eltype = 'Cuad'):
		pass
    


if __name__ == '__main__':
	Malla()
