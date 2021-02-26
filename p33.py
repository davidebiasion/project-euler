frac = []


for n in range(10, 99):
	for d in range(n+1, 100):
		n_to_str = str(n)
		d_to_str = str(d)

		#print(n_to_str+"/"+d_to_str)

		# trivial examples
		if n_to_str[1]=='0' and d_to_str[1]=='0':
			continue


		# non-trivial
		if n_to_str[1]==d_to_str[1] and d_to_str[0]!='0':
			if float(n_to_str[0])/float(d_to_str[0]) == float(n)/d:
				frac.append([n, d])
				continue

		if n_to_str[1]==d_to_str[0] and d_to_str[1]!='0':
			if float(n_to_str[0])/float(d_to_str[1]) == float(n)/d:
				frac.append([n, d])
				continue

		if n_to_str[0]==d_to_str[1] and d_to_str[0]!='0':
			if float(n_to_str[1])/float(d_to_str[0]) == float(n)/d:
				frac.append([n, d])
				continue

		if n_to_str[0]==d_to_str[0] and d_to_str[1]!='0':
			if float(n_to_str[1])/float(d_to_str[1]) == float(n)/d:
				frac.append([n, d])
				continue

		
print(frac)

res_n = 1
res_d = 1
for f in frac:
	res_n*=f[0]
	res_d*=f[1]


res = float(res_n)/res_d
den = 1

while res < 1:
	den*=10
	res*=10

print(den)