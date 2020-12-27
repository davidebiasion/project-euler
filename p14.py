def collatz_sequence_len(n):
	i = n
	l = 1
	while i!=1:
		if i%2 == 0:
			i = i//2
		else:
			i = 3*i+1

		l+=1

	return l


n = 1
max_n = 0
max_l = 0

while n < 1000000:
	l = collatz_sequence_len(n)
	
	if l > max_l:
		max_l = l
		max_n = n 

	n+=1


print("max_n: "+str(max_n)+" max_l: "+str(max_l))