import time


def is_prime(n):
	#print("--- is_prime("+str(n)+")")
	if n==2 or n==3:
		return True

	if n==1 or n%2==0 or n%3==0:
		return False

	i = 5
	while i*i <= n:
		if n%i==0 or n%(i+2)==0:
			return False
		i+=6

	return True	


def is_truncable(n):
	s = str(n)
	n = len(s)
	trunc = True

	for i in range(1, n):
		#print(s[i:], s[:n-i])
		if not is_prime(int(s[i:])) or not is_prime(int(s[:n-i])):
			trunc = False		
			break

	return trunc


t_0 = time.time()
count = 0
s = 0
i = 11
while count<11:
	if is_prime(i):
		if is_truncable(i):
			count+=1
			s+=i

	i+=1

print('time:', time.time()-t_0)
print(s)