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


prime_sum = 0
n = 2

while n < 2000000:
	if is_prime(n):
		prime_sum+=n 

	n+=1

print(prime_sum)