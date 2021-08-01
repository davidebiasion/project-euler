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


t_0 = time.time()
primes_count = 8 
corner = 49
side_len = 7

while primes_count/(side_len*2-1)>0.1:
	for i in range(4):
		corner+=side_len+1

		if is_prime(corner):
			primes_count+=1

	side_len+=2

print('time:', time.time()-t_0)
print(side_len)