import time


def digital_sum(n):
	st = str(n)
	s = 0
	for i in range(len(st)):
		s+=int(st[i])

	return s


t_0 = time.time()
max_s = -1
for a in range(1, 100):
	for b in range(1, 100):
		n = a**b
		s = digital_sum(n)

		if s>max_s:
			max_s = s

print('time:', time.time()-t_0)
print(max_s)