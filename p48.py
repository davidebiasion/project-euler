import time

t_0 = time.time()
s = 0
for n in range(1, 1001):
	p = 1
	for i in range(n):
		p*=n

	s+=p

print(time.time()-t_0)
print(str(s)[-10:])
