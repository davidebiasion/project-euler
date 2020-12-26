n = 20
n_max = 1
for j in range(1, 21):
	n_max*=j

while n <= n_max:
	for i in range(19, 0, -1):
		if n%i!=0:
			break
	
	if i==1:
		break
	else:
		n+=20

print(n)