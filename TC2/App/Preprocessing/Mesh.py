import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML, display
from ipywidgets import interact, interactive, interact_manual
import sqlite3 as sql
try:
	from App.Preprocessing.Geometry import *
	from App.Preprocessing.DataBase import DB
except:
	from Geometry import *
	from DataBase import DB

class Element():
	"""
		Desarrolla el dibujo del elemento
	"""
	def esquemaN(self, Es, nodos, color = 'black'):
		self.nodos = nodos
		Es.scatter(nodos[:, [0]], nodos[:, [1]], c=color)
	def esquemaEL(self, Es, nodos, color = 'black'):
		for i in range(1,len(nodos)):
			Es.plot(
				[nodos[i-1][0], nodos[i][0]],
				[nodos[i-1][1], nodos[i][1]],
				color=color
<<<<<<< HEAD
			)
	def save(self, nodos, *args):
		#Guardar en base de datos
		con, cursor = args[0]
		#Nodos
		Final_nodes = []
		for nodo in nodos:
			datos = con.execute("SELECT * FROM nodes").fetchall()
			exist = False
			for data in datos:
				if data[2] == nodo[0] and data[3] == nodo[1]:
					exist = True
					Final_nodes.append(data[0])
			if not exist:
				text = 'INSERT INTO nodes (x,y) VALUES ('
				text += str(nodo[0]) + ',' + str(nodo[1]) + ')'
				cursor.execute(text)
				ID = con.execute('SELECT * FROM nodes ORDER BY NodeID DESC LIMIT 1')
				Node = ID.fetchall()
				Final_nodes.append(Node[0][0])
		#Elementos
		text = 'INSERT INTO elements ('
		text2 = ''
		for i in range(len(Final_nodes)):
			text += 'Node' + str(i+1) + ', '
			text2 += str(Final_nodes[i]) + ', '
		text2 = text2[:-2] + ')'
		text = text[:-2] + ') VALUES (' + text2
		cursor.execute(text)
		con.commit()
=======
			)  
	def Guardar(self, nodos):
		text = """
				INSERT INTO nodes
>>>>>>> 9e2b2d95fe216add6e46ba223ea5ab2d90bd933f

            
class Cuad4(Element):
	"""
		Elemento cuadrangular 2D de 4 nodos.

		SE DEBE HACER UNA BASE DE DATOS DE PUNTOS:

			Núm nodo 	x	y

		Elementos

			Núm El 		Nodo1	Nodo2	Nodo3	Nodo4

	"""
	def __init__(self, tam, Es, init=[0,0], num=4, **kwargs):
		#Ubicación de nodos
		nodos = self.nodes(init,tam)
		#Esquema - nodos
		self.esquemaN(Es, nodos)
		#Esquema - Elementos
		self.esquemaEL(Es, nodos)

		#Guardar en base de datos
		self.save(nodos, kwargs['db'])

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

class Cuad8(Cuad4):
	"""
		Elemento cuadrangular 2D de 8 nodos.
	"""
	def __init__(self, tam, Es, init=[0,0], num = 8, **kwargs):
		#4 nodes
		nodos = self.nodes(init, tam)
		#8 nodes
		nodes = []
		for i in range(len(nodos)):
			nodes.append(nodos[i])
			if not i%2:
				#Arriba - abajo
				nodes.append([((nodos[i+1][j]-nodos[i][j])/2 + \
					nodos[i][j]) for j in range(2)])
			else:
				#Izquierda - derecha
				if nodos[0][1] > nodos[3][1]:
					maximo = nodos[0][1]
					minimo = nodos[3][1]
				else:
					maximo = nodos[3][1]
					minimo = nodos[0][1]
				nodes.append([nodos[i][0], minimo+(maximo-minimo)/2])
		#Esquemas
		self.esquemaN(Es, np.array(nodes))
		self.esquemaEL(Es, np.array(nodes))

		#Guardar en base de datos
		self.save(nodes, kwargs['db'])
    
class Tri3(Element):
	"""
		Elemento triangular 2D de 3 nodos.
	"""
	def __init__(self, tam, Es, init=[0,0], num = 3, **kwargs):
		pass

class Tri6(Tri3):
	"""
		Elemento triangular 2D de 6 nodos.
	"""
	def __init__(self, tam, Es, init=[0,0], num = 6, **kwargs):
		pass


class Malla(DB, Geo):
	"""
		OBJETIVO:
			Desarrolla la malla para simulación numérica y almacena la
			ínformación de los nodos y elementos en una base de datos.

		ARGUMENTOS:
			- dom 	->	Dominio o figura a mallar.
			- Eltype ->	Tipo de elemento.
			- El 	 ->	Dimensiones de los elementos estándar
			- ref	 ->	Refinamiento de curvatura
			- num 	 ->	Vector booleano para numeración de nodos y elementos
	"""
	def __init__(self, El, ref, num = [False, False],dom=False, Eltype = 'Cuad4', \
		local = False):
		#Conexión con base de datos
		super().__init__(local, Eltype)
		#Dominio General - Frontera
		if dom:
			super(DB, self).__init__(dom)
		#Dibujo de los elementos
		coord = [0,0]
		for x in range(int(dom['W']['Valor']/El[0])):
			for y in range(int(dom['H']['Valor']/El[1])):
				if Eltype == 'Cuad4':
					Cuad4(El, self.ax, coord, db=[self.con, self.cursor])
				elif Eltype == 'Cuad8':
					Cuad8(El, self.ax, coord, db=[self.con, self.cursor])
				coord[1] += El[1]
			coord[0] += El[0]
			coord[1] = 0

		#Organizar tablas
		self.organizar()

		#Texto Nodal
		if num[0]:
			self.textN()

		#Texto Elemental
		if num[1]:
			self.textE()

		#Gráfica
		plt.show()

	def textN(self):
		datos = self.con.execute("SELECT * FROM nodes ORDER BY ID ASC").fetchall()
		for dato in datos:
			plt.text(dato[2], dato[3], str(dato[1]))

	def textE(self):
		elements = self.data('elements')
		nodos = self.con.execute("SELECT * FROM nodes ORDER BY ID ASC").fetchall()
		for element in elements:
			dominio = [[0,0], [0,0]]	#Mínimos y máximos en x e y.
			for i in range(1,len(element)):
				if i == 1:
					dominio[0][0] = nodos[element[i]-1][2]
					dominio[1][0] = nodos[element[i]-1][3]
				else:
					if nodos[element[i]-1][2] > dominio[0][0]:
						dominio[0][1] = nodos[element[i]-1][2]
					if nodos[element[i]-1][3] > dominio[1][0]:
						dominio[1][1] = nodos[element[i]-1][3]
			plt.text((dominio[0][1]+dominio[0][0])/2,
						(dominio[1][0]+dominio[1][1])/2,
						str(element[0]))

	def organizar(self):
		datos = self.con.execute("SELECT * FROM nodes ORDER BY x ASC, y ASC").fetchall()
		new_ids = {}
		elements = self.data('elements')
		#Matriz booleana
		M = []
		for i in range(len(elements)):
			vec = []
			for j in range(1,len(elements[i])):
				vec.append(True)
			M.append(vec)
		#Organización de la información
		for i in range(len(datos)):
			new_ids[i+1] = datos[i][0]
			self.con.execute('UPDATE nodes SET ID=' + \
				str(i+1) + ' WHERE NodeID=' + str(new_ids[i+1]))
			for j in range(1, len(elements)):
				for k in range(1, len(elements[j])):
					if M[j-1][k-1] and elements[j-1][k] == new_ids[i+1]:
						text = 'UPDATE elements SET Node' + str(k) + '= '
						text += str(i+1) + ' WHERE ElID='
						text += str(j)
						self.con.execute(text)
						M[j-1][k-1] = False
		self.con.commit()
			

if __name__ == '__main__':
	data = {
	    'Geometría': {
	        'W': {
	            'Valor':8,
	            'Units': 'm'
	        },
	        'H': {
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
	Malla((0.5,0.5), (False, False), [True, True],  data['Geometría'], local=True, \
		Eltype='Cuad8')

