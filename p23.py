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
limit = 28123

abundants = []
for i in range(2, limit+1):
	if proper_divisors(i)>i:
		abundants.append(i)

can_be_wr = [False for i in range(limit+1)]
for i in range(len(abundants)):
	for j in range(i, len(abundants)):
		if abundants[i]+abundants[j]>limit:
			break
		can_be_wr[abundants[i]+abundants[j]] = True

s = 0
for i in range(1, limit+1):
	if not can_be_wr[i]:
		s+=i

print(time.time()-t_0)
print(s)


