'''one_p = 1
two_p = 2
five_p = 5
ten_p = 10
twenty_p = 20
fifty_p = 50
one_l = 100
two_l = 200
'''
pence = [1, 2, 5, 10, 20, 50, 100, 200]
'''
	conf = []
	
	# lunghezza permutazioni
	for n in range(len(pence)):
	
	'''	

conf = []

for i in range(1, 2**8):
	to_bin = '{0:08b}'.format(i)

	c = []
	for j in range(8):
		if to_bin[j]=='1':
			c.append(pence[j])
	conf.append(c)

'''
[200], [100], [50, 200], [50, 100], [50, 100, 200]
'''

for c in conf:
	