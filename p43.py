'''
def is_pandigital(s):
	s = sorted(str(s))
	j = 0
	while j<len(s) and s[j]==str(j):
		j+=1

	return j == len(s)
'''

def is_divisible(n):
	divisor = 2
	while divisor**2 <= n:
		if n%divisor == 0:
			return True 

		divisor += 1

	return False

'''
s = 0
for i in range(1000000000, 10000000000):
	if is_pandigital(i):
		print('*** ', i)
		num = str(i)

		for j in range(1, 8):
			sub = num[j:j+3]

			if not is_divisible(int(sub)):
				break

		if j == 7:
			s += i
			print('         yes!')

print(s)'''



def sort(s):
	l = list(s)
	for i in range(1, len(s)):
		el = l[i]
		j = i-1          
		while j >= 0 and l[j] > el:
			l[j+1] = l[j]
			j -= 1
		l[j+1] = el


	return ''.join(l)


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

		perm.append(''.join(new_perm))

	return perm


perm = permutations('0123456789')
pandigital = []
for p in perm:
	if p[0] != '0':
		pandigital.append(p)

print(len(pandigital))

s = 0
divisor = [2, 3, 5, 7, 11, 13, 17]
res = []

for pan in pandigital:
	divisible = True
	for j in range(len(divisor)):
		sub = pan[j+1:j+1+3]
		#print('***** ', divisor[j], sub, int(sub)%divisor[j])
		if int(sub)%divisor[j] != 0:
			divisible = False
			break

	if divisible:
		res.append(int(pan))
		s += int(pan)

print(res)
print(s)













































