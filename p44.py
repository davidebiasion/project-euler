import math
import time

def is_pentagonal(p):
	n = (1 + math.sqrt(1+24*p))/6.0

	#return n.is_integer()
	return n == int(n)


t_0 = time.time()
i = 2
found = False
D = -1

while not found:
	n = i*(3*i-1)/2

	for j in range(i-1, 0, -1):
		m = j*(3*j-1)/2 
		#print(n, m)
		
		if is_pentagonal(n-m) and is_pentagonal(n+m):
			D = n-m
			found = True 	
			break
	i += 1


print(D)
print(time.time()-t_0)