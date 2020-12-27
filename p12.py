import math


def divisors(n):
	divisors = 0
	i = 1
	sqrt_n = int(math.sqrt(n))

	while i <= sqrt_n:
		if n%i == 0:
			divisors+=2

		i+=1

	if sqrt_n*sqrt_n == n:
		divisors-=1

	return divisors


t = 0
n = 1
while divisors(t) <= 500:
	t+=n
	n+=1


print(t)