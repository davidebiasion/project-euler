import time

'''
1/7 = 0.142857
10
30
20
60
40
50
10

1/5 = 0.2
10
0

1/4 = 0.25
10
20
0

1/8 = 0.2
10
20
'''

def reccuring_cycle(n):
	rem = [10]
	while True:
		r = (rem[-1]%n)*10
		if r==0:
			return 0
		
		for i in range(len(rem)):
			if rem[i]==r:
				return len(rem)-i

		rem.append(r)


t_0 = time.time()
max_cycle = -1
max_d = -1
for d in range(1, 1000):
	c = reccuring_cycle(d) 
	if c>max_cycle:
		max_cycle = c
		max_d = d

print('time:', time.time()-t_0)
print('d:', max_d, 'cycle:', max_cycle)




