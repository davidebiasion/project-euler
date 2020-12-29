import numpy as np


def routes(n, m):
	R = np.zeros((n+1, m+1))
	
	for j in range(m+1):
		R[0, j] = 1

	for i in range(n+1):
		R[i, 0] = 1

	for i in range(1, n+1):
		for j in range(1, m+1):
			R[i, j] = R[i-1, j]+R[i, j-1]

	return R[n, m]


print(routes(20, 20))