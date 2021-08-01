import time


t_0 = time.time()
prev_n = 1
prev_d = 2
count = 0

for t in range(1, 1000):
	d_0 = prev_d
	n_0 = 2*d_0 + prev_n

	n_1 = d_0
	d_1 = n_0

	prev_n = n_1
	prev_d = d_1

	d_2 = d_1
	n_2 = d_2 + n_1

	if len(str(n_2))>len(str(d_2)):
		count+=1

print('time:', time.time()-t_0)
print(count)