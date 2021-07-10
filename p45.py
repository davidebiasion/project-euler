import math
import time


def is_triangular(t):
	# t = n(n+1)/2
	# 2t = n^2 + n
	# n^2 + n - 2t = 0
	# delta = 1 + 4*2t = 1 + 8t
	# n = (-1 + sqrt(1+8t))/2
	n = (-1 + math.sqrt(1+8*t))/2

	return n == int(n)


def is_pentagonal(p):
	# p = n(3n-1)/2
	# 2p = 3n^2 - n
	# 3n^2 - n - 2p = 0
	# delta = 1 + 4*6p = 1 + 24p
	# n = (1 + sqrt(1+24p))/6
	n = (1 + math.sqrt(1+24*p))/6

	return n == int(n)


def is_hexagonal(h):
	# h = n(2n-1)
	# h = 2n^2 - n
	# 2n^2 - n - h = 0
	# delta = 1 + 4*2h = 1 + 8h
	# n = (1 + sqrt(1+8h))/4
	n = (1 + math.sqrt(1+8*h))/4

	return n == int(n)


# gli esagonali sono un sottoinsieme dei triangolari, sono in particolare i triangolari generati da n dispari
# ogni numero esagonale è quindi anche triangolare
# ne consegue che generando numeri esagonali (che sono anche triangolari) basterà verificare che siano pentagonali


t_0 = time.time()
n = 144

while True:
	h = n*(2*n-1) 
	if is_pentagonal(h):
		break

	n += 1

print(time.time()-t_0)
print(h)
