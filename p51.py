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
limit = 1000000
for i in range(limit):
	if is_prime(i):
		primes.append(i)


def has_012_rep(n):
	n = str(n)
	count_0 = 0
	count_1 = 0
	count_2 = 0

	# [count, [idxs]]
	rep_0 = [0, []]
	rep_1 = [0, []]
	rep_2 = [0, []]

	for i in range(len(n)):
		if n[i]=='0':
			rep_0[0]+=1
			rep_0[1].append(i)
		
		elif n[i]=='1':
			rep_1[0]+=1
			rep_1[1].append(i)
		
		elif n[i]=='2':
			rep_2[0]+=1
			rep_2[1].append(i)

	return rep_0, rep_1, rep_2


t_0 = time.time()
found = False
j = 0
while not found:
	p = primes[j]
	rep = has_012_rep(p)

	for k in range(3):
		family_size = 0

		if rep[k][0]>0:
			for d in range(1, 10):
				cand = str(p)
			
				for i in rep[k][1]:
					cand = cand[0:i]+str(d)+cand[i+1:]
				
				if is_prime(int(cand)):
					family_size+=1

			if family_size==8:
				print(p, rep[k])
				found = True
				break

	j+=1

print('time:', time.time()-t_0)