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


def contains_2_or_5(s):
	for ch in s:
		if ch=='2' or ch=='5':
			return True

	return False


primes = []
for i in range(2, 1000000):
	if is_prime(i):
		primes.append(i)


circ_primes = []
for p in primes:
	num = str(p)
	l = len(num)
	circ = list(num)
	curr = [ch for ch in circ]
	is_circular = True

	for t in range(l):
		for i in range(l):	
			circ[(i+1)%l] = curr[i]

		candidate = ''
		for ch in circ:
			candidate+=ch

		if l>1 and contains_2_or_5(candidate):
			is_circular = False
			break

		if not is_prime(int(candidate)):
			is_circular = False
			break

		curr = [ch for ch in circ]
		#print(circ)

	if is_circular:
		circ_primes.append(p)
		#print(p)


print(circ_primes)
print(len(circ_primes))
