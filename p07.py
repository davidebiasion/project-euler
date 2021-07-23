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


n = 2
i = 0

while i < 10001:
	if is_prime(n):
		i+=1
	
	n+=1

print(n-1)