import time
import math


def proper_divisors(n):
	pd_sum = 1
	i = 2

	limit = math.sqrt(n)
	if n==limit*limit:
		limit-=1

	while i<=limit:
		if n%i==0:
			pd_sum+=i+n//i

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