'''
almeno (1, 2)
sia c il la concatenazione dei prodotti
|c| = 9 ==> a < 10000
'''


def is_pandigital(s, n):
	if len(s) != n:
		return False

	s = sorted(s)

	j = 0
	while j<len(s) and s[j]==str(j+1):
		j+=1

	return j == n


a = 9999
pan = []

while a>1:
	c = str(a)

	i = 2	
	while len(c)<9:
		p = a*i 
		c = c+str(p)

		i+=1

	if len(c)==9:
		if is_pandigital(c, 9):
			pan.append([a, int(c)])

	a-=1

#print(pan)
print(max(pan, key=lambda p: p[1]))