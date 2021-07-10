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



t_0 = time.time()
i = 17
while True:
	odd = 2*i+1
	if not is_prime(odd):
		p = 2
		found = False
		while p <= odd-2 and not found:
			if is_prime(p):
				s = 1
				while p+2*s*s <= odd:
					if p+2*s*s == odd:
						found = True
						# print('found:', odd, p, s*s)
						break
					s+=1
			p+=1
		
		if found == False:
			print(odd)
			break
	
	i+=1

print(time.time()-t_0)