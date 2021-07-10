import time


def is_prime(n):
	#print("--- is_prime("+str(n)+")")

	if n==2 or n==3:
		return True

	if n%2==0 or n%3==0:
		return False

	i = 5
	while i*i <= n:
		if n%i==0 or n%(i+2)==0:
			return False
		i+=6

	return True

limit = 1000000
primes = []
for i in range(2, limit):
	if is_prime(i):
		primes.append(i)

# 2, 3, 5, 7, 11
# 2, 5, 10,17,28


prime_sum = [primes[0]]
for i in range(1, len(primes)):
	prime_sum.append(prime_sum[i-1]+primes[i])

prime_sum.insert(0, 0)
#print(prime_sum[:6])

# i: indice partenza
# j: indice di arrivo
# k: lunghezza sequenza

t_0 = time.time()

k = 2
last = -1
for i in range(1, len(primes)-k):
	# la sequenza deve essere almeno lunga k
	for j in range(i+k, len(primes)):
		s = prime_sum[j]-prime_sum[i-1]
		#print('k:', k, 'i', i, 'j:', j, 's:', s, prime_sum[j], prime_sum[i-1])

		if s>limit:
			break

		if is_prime(s):
			k = j-i+1
			last = s
			#print('k', k, 's:', s)

print('time:', time.time()-t_0)
print(last)



