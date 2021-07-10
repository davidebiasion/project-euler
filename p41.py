# Utility function to swap the characters in a character list
def swap(A, i, j):

	c = A[i]
	A[i] = A[j]
	A[j] = c


# Utility function to reverse a list between specified indexes
def reverse(A, i, j):

	# do till two endpoints intersect
	while i < j:
		swap(A, i, j)
		i = i + 1
		j = j - 1


# Iterative function to find permutations of a string in Python
def permutations(str, n):
	perm = []

	# sort the string in a natural order
	s = sorted(list(str))

	while True:

		# print the current permutation
		perm.append(''.join(s))
		#print(''.join(s), end=' ')

		''' The following code will rearrange the string to the next lexicographically
			ordered permutation (if any) or return if we are already at
			the highest possible permutation '''

		# Find the largest index `i` such that `s[i-1]` is less than `s[i]`
		i = n - 1
		while s[i - 1] >= s[i]:
			# if `i` is the first index of the string, we are already at the
			# last possible permutation (string is sorted in reverse order)
			i = i - 1
			if i == 0:
				return perm

		# find the highest index `j` to the right of index `i` such that
		# `s[j] > s[i-1]` (`s[i…n-1]` is sorted in reverse order)

		j = n - 1
		while j > i and s[j] <= s[i - 1]:
			j = j - 1

		# swap character at index `i-1` with index `j`
		swap(s, i - 1, j)

		# reverse substring `s[i…n-1]`
		reverse(s, i, n - 1)



def is_pandigital(s, n):
	s = sorted(s)

	j = 0
	while j<len(s) and s[j]==str(j+1):
		j+=1

	return j == n



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



for n in range(9, 1, -1):
	s = ''
	i = 1
	while len(s) < n:
		s+=str(i)

		i+=1

	print('***', s)
	perm = permutations(s, len(s))
	M = -1

	for p in perm:
		num_p = int(p)
		if is_pandigital(p, len(p)) and is_prime(num_p):
			if num_p > M:
				M = num_p

	if M != -1:
		print(M)
		break
