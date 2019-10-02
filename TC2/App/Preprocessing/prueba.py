import numpy as np
nodos = [
	[0.5, 1],
	[1,1],	#
	[1,2],
	[0.5,2]		#
]
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


print(nodes)
print(np.array(nodes))
