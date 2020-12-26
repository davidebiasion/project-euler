def is_palindrome(n):
	s = str(n)
	l = len(s)
	i = 0

	while s[i]==s[l-1-i] and i<l//2:
		i+=1

	return i==l//2


def check_digits(n):
	a = 100
	b = -1
	while a <= 999:
		if n%a==0 and len(str(n//a))==3:
			return [a, n//a]
		a+=1

	return False


a = 100
b = 100
c = 999*999
count = 0

while c >= 100*100:
	if is_palindrome(c) and check_digits(c)!=False: 
		break

	c-=1


print(c)
print(check_digits(c))
