pows = []

for a in range(2, 101):
	for b in range(2, 101):
		p = a**b
		if p not in pows:
			pows.append(p)

pows.sort()
print(len(pows))