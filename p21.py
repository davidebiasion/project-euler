import time
import math


def proper_divisors(n):
	pd_sum = 1
	sqrt = int(math.sqrt(n))

	if sqrt*sqrt==n:
		pd_sum+=sqrt
		sqrt-=1	

	i = 2
	while i<=sqrt:
		if n%i==0:
			pd_sum = pd_sum+i+n//i

		i+=1

	return pd_sum


t_0 = time.time()
amicable_sum = 0
limit = 10000
for a in range(limit):
	d_a = proper_divisors(a)
	if d_a>a and d_a<limit:
		d_b = proper_divisors(d_a)
		if d_b==a:
			amicable_sum+=a+d_a


print('time:', time.time()-t_0)
print(amicable_sum)