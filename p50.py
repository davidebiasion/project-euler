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


primes = []
first = -1
k = 0
found = False
for i in range(2, 100):
	if is_prime(i):
		primes.append(i)

		if not found and i>=1000:
			first = k
			found = True
		
		k+=1

#print(primes[first])

'''
j = first
max_len = -1
max_add = [] 
while j<len(primes):
	p = primes[j]
	found = False
	start = 0
	while primes[start]<p:
		s = 0
		add = []
		i = start
		while primes[i]<p:
			s+=primes[i]
			add.append(primes[i])
			
			if s==p:
				found = True
				if len(add)>max_len:
					max_len = len(add)
					max_add = [el for el in add]
					print('***', sum(max_add))

			i+=1

		start+=1
				
	j+=1
'''
'''

j = len(primes)-1
max_len = -1
#max_add = [] 
while j>first:
	p = primes[j]
	#print(p)
	found = False
	start = 0
	while primes[start]<p and not found:
		s = 0
		#add = []
		l = 0
		i = start
		while primes[i]<p and s<p and not found:
			s+=primes[i]
			#add.append(primes[i])
			l+=1

			if s==p:
				found = True
				#if len(add)>max_len:
				if l>max_len:
					#max_len = len(add)
					max_len = l
					#max_add = [el for el in add]
					print('***', p, max_len)

			i+=1

		start+=1
				
	j-=1



print(sum(max_add), max_add)


'''



'''

sia f(n) = somma dei primi consecutivi da 2 a n
f(2) = 2
f(3) = 2+3 = f(2)+3 = 5
f(5) = 2+3+5 = f(3)+5 = 10
...
f(n) = f(n-1)+n

'''

f = [[primes[0], primes[0]]]
for i in range(1, len(primes)):
	f.insert(i, [primes[i], f[i-1][1]+primes[i]])

#print(f)


for i in range(len(primes)):
	start = 0
	while f[start]<




































