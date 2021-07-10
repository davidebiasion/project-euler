import time


def binomial(n, r):
	fac = 1
	for i in range(1, n+1):
		fac*=i

		if i==r:
			r_fac = fac

		if i==n-r:
			if n-r==0:
				n_r_fac = 1
			n_r_fac = fac

	return fac//(r_fac*n_r_fac)



t_0 = time.time()
count = 0
for n in range(1, 101):
	for r in range(1, n):
		if binomial(n, r)>1000000:
			count+=1


print(count)
print('time:', time.time()-t_0)