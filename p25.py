import time


f_n_2 = 1
f_n_1 = 1

t_0 = time.time()
idx = 3
while True:
	f_idx = f_n_1+f_n_2
	
	if len(str(f_idx))==1000:
		print('found!', idx)
		break

	f_n_2 = f_n_1
	f_n_1 = f_idx
	idx+=1

print('time:', time.time()-t_0)