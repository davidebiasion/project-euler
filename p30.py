l = []

for i in range(2, 10000000): # non un modo intelligente ... sono arrivato a 10000000 facendo delle prove
	to_str = str(i)
	s = 0

	for j in range(len(to_str)):
		s+=int(to_str[j])**5

	if s == i:
		l.append(i)

print(l)
print(sum(l))