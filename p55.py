import time


def is_palindrome(n):
	s = str(n)
	l = len(s)

	i = 0
	while i<l//2 and s[i]==s[l-1-i]:
		i+=1

	return i==l//2


def reverse(n):
	s = str(n)
	rev = 0
	for i in range(len(s)):
		rev+=int(s[i])*(10**i)

	return rev


def is_lychrel(n):
	t = 0
	n_t = n
	while t<50:
		n_t = n_t + reverse(n_t)

		if is_palindrome(n_t):
			return False

		t+=1

	return True


t_0 = time.time()
count = 0
for i in range(10000):
	if is_lychrel(i):
		count+=1

print('time:', time.time()-t_0)
print(count)



