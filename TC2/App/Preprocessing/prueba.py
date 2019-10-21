M = []

n = 4
m = 5

for i in range(n):
	vec = []
	for j in range(m):
		vec.append(i-j)
	M.append(vec)

print(M)

for i in range(n):
	for j in range(m):
		if M[i][j] == -1:
			M[i].remove(-1)
			break

print(M)