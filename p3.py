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



n = int(input("n: "))
factors = []
i = 2

while i*i <= n:
	print("i: "+str(i))

	if n%i==0 and is_prime(i):
		factors.append(i)

	i+=1

print(factors)



'''largestFact = 0
factors = []


numn = 600851475143


i = 2
while i*i < numn:
    if numn % i == 0: # It is a divisor
        factors.insert(0, i)
        factors.insert(1, numn / i)
 
        for k in range(2):
            isPrime = True

            j = 2
            #for j in range(2, j * j <  factors[k]):
            while j*j < factors[k]:    
                if factors[k] % j == 0:
                    isPrime = False
                    break
                j+=1
            if isPrime and factors[k] > largestFact:
                largestFact = factors[k]

    i+=1


print(largestFact)'''
