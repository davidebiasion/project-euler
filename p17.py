d = {}

d['1'] = 3
d['2'] = 3
d['3'] = 5
d['4'] = 4
d['5'] = 4
d['6'] = 3
d['7'] = 5
d['8'] = 5
d['9'] = 4

d['10'] = 3

d['11'] = 6
d['12'] = 6
d['13'] = 8
d['14'] = 8
d['15'] = 7
d['16'] = 7
d['17'] = 9
d['18'] = 8
d['19'] = 8

d['20'] = 6

d['30'] = 6

d['40'] = 5

d['50'] = 5

d['60'] = 5

d['70'] = 7

d['80'] = 6

d['90'] = 6

d['hundred'] = 7

d['and'] = 3



s = 0

# 1 to 9
for i in range(1, 10):
	s+=d[str(i)]

# 10 to 19
for i in range(10, 20):
	s+=d[str(i)]

# 20 to 99
for i in range(20, 100, 10):
	# decade-0
	s+=d[str(i)]

	# decade-1-9
	for j in range(1, 10):
		s+=d[str(i)]+d[str(j)]

# 100 to 999
for h in range(1, 10):
	# hundred
	i_hundred = d[str(h)]+d['hundred']
	s+=i_hundred

	i_hundred_and = i_hundred+d['and']

	# 1 to 9
	for i in range(1, 10):
		s+=i_hundred_and+d[str(i)]

	# 10 to 19
	for i in range(10, 20):
		s+=i_hundred_and+d[str(i)]

	# 20 to 99
	decade = 0
	for i in range(20, 100, 10):
		# decade-0
		decade = d[str(i)]
		s+=i_hundred_and+decade

		# decade-1-9
		for j in range(1, 10):
			s+=i_hundred_and+decade+d[str(j)]

# 1000
s+=d[str(1)]+len('thousand')

print(s)
