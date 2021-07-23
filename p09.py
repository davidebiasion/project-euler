m = 2
s = 0
go = True

while go:
	for n in range(1, m):
		a = m*m - n*n
		b = 2*m*n
		c = m*m + n*n
			
		if a+b+c==1000:
			go = False
			break


	m+=1

print("a*b*c = "+str(a)+"*"+str(b)+"*"+str(c)+" = "+str(a*b*c))


'''
# BRUTE FORCE
# a < b < c
stop = False
limit = 1000

for a in range(1, limit):
	for b in range(a+1, limit):
		for c in range(b+1, limit):
			if a*a + b*b == c*c and a+b+c==1000:
				print("a*b*c = "+str(a)+"*"+str(b)+"*"+str(c)+" = "+str(a*b*c))
				stop = True
				break

			if stop:
				break
		
		if stop:
			break
'''