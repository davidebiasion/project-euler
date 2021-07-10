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


def factorial(n):
	f = n
	for i in range(1, n):
		f *= n-i

	return f


def permutations(s):
	perm = []
	perm.append(s)
	n_perm = factorial(len(perm[0]))
	while len(perm) < n_perm:
		s = list(perm[-1])

		# find the rightmost character which is smaller than the one to its right
		j = len(s)-2
		while s[j] > s[j+1]:
			j -= 1

		# find the smallest element to its right which is greater than it
		i = len(s)-1
		while s[i] < s[j]:
			i -= 1

		# swap the two elements
		s_i = s[i]
		s[i] = s[j]
		s[j] = s_i

		# reverse the characters to the right of the first element position
		rev = []
		for k in range(len(s)-1, j, -1):
			rev.append(s[k])

		new_perm = s[:j+1] + rev
		'''
		str_new_perm = ''.join(new_perm)
		if str_new_perm not in perm:
			print('here')
			count+=1
			perm.append(str_new_perm)
		'''
		perm.append(''.join(new_perm))

	no_duplicates = []
	for p in perm:
		if p not in no_duplicates:
			no_duplicates.append(p)

	return perm, no_duplicates


def digit_permutations(n):
	permutations = []
	l = len(str(n))
	n_perm = factorial(n)
	i = 10**(l-1)
	while len(permutations) < n_perm and i < 10**l: 
		if is_permutation(str(i), str(n)):
			permutations.append(i)

		i+=1

	return permutations


def is_permutation(p, n):
	if p == n:
		return True

	p = sorted(p)
	n = sorted(n)

	return p == n



t_0 = time.time()

four_digit_primes = []
for i in range(1488, 10000):
    if is_prime(i):
        four_digit_primes.append(i)

i = 0
found = False

while i < len(four_digit_primes) and not found:
	prime = four_digit_primes[i]
	perm = digit_permutations(prime)
	prime_perm = []
	for p in perm:
		if is_prime(p) and p > prime:
			prime_perm.append(p)

	if len(prime_perm)>=2:
		for p in prime_perm:
			diff = p-prime

			if p+diff in prime_perm:
				print(time.time()-t_0)
				print(prime, prime+diff, prime+2*diff)
				print('diff', diff)
				found = True
				break 

	i+=1
