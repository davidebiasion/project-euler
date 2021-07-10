import time


t_0 = time.time()
found = False
x = 2
while not found:
	x2 = sorted(str(2*x))
	x3 = sorted(str(3*x))
	x4 = sorted(str(4*x))
	x5 = sorted(str(5*x))
	x6 = sorted(str(6*x))

	if x2==x3 and x3==x4 and x4==x5 and x5==x6:
		print(x)
		break

	x+=1

print('time:', time.time()-t_0)
