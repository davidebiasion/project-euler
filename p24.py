def swap(a, i, j):
	temp = a[i]
	a[i] = a[j]
	a[j] = temp


def permutation(a, start, end, history):
	if start==end:
		#print(a)
		b = [el for el in a]
		history.append(b)
		#print(history)

	for i in range(start, end+1):
		swap(a, start, i)
		permutation(a, start+1, end, history)
		swap(a, start, i)


h = []
permutation(range(0, 10), 0, 9, h)
#print(h)

h.sort()
print(h[999999])
