def dec_to_bin(n):
	if n==0:
		return '0'

	q = n
	r = -1
	resti = []

	while q!=0:
		r = q%2
		q = q//2

		resti.insert(0, r)

	s = ''
	for ch in resti:
		s+=str(ch)

	return s


def is_palindrome(s):
	l = len(s)
	i = 0

	while s[i]==s[l-1-i] and i<l//2:
		i+=1

	return i==l//2


pal = []

for i in range(1, 1000000):
	if is_palindrome(str(i)) and is_palindrome(dec_to_bin(i)):
		pal.append(i)

print(sum(pal))
