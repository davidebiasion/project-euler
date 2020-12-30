n = 100

f = 1
for i in range(1, n+1):
	f*=i

s = 0
for char in str(f):
	s+=int(char)

print(s)