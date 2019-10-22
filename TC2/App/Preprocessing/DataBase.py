import sqlite3 as sql
import os
class DB():
	"""
		Crea y organiza la base de datos.
	"""
	def __init__(self, local, ElType = "Cuad4"):
		#Borrar tablas existentes
		try:
			try:
				os.remove('data.db')
			except:
				os.remove('App/Preprocessing/data.db')
		except:
			pass
		#Creación de la base de datos
		if local:
			self.con = sql.connect('data.db')
		else:
			self.con = sql.connect('App/Preprocessing/data.db')
		self.cursor = self.con.cursor()
		#Crear tablas
		self.Tabla_Nodos()
		self.Tabla_Elementos(ElType)

	def data(self, tab_name):
		return self.con.execute("SELECT * FROM " + tab_name).fetchall()

	def Tabla_Nodos(self):
		self.cursor.execute("""
			CREATE TABLE nodes (
				NodeID INTEGER PRIMARY KEY,
				ID INTEGER,
				x float,
				y float
			)
			""")
		self.con.commit()

	def Tabla_Elementos(self, ElType):
		text = """CREATE TABLE elements (
				ElID INTEGER PRIMARY KEY,
				N INTEGER,
				S INTEGER,
				p INTEGER,
				E INTEGER,
				W INTEGER
			)"""

		self.cursor.execute(text)
		self.con.commit()

if __name__ == '__main__':
	DB(local=True, ElType='Cuad4')