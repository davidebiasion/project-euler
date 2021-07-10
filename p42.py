'''
print(ord('A')-64)
print(ord('S')-64)


0.5*n*(n+1) = t_n

n*(n+1) = 2*t_n
n**2 +n -2*t_n = 0
delta = 1 -4*(-2*t_n) = 1 +8*t_n
n = (-1 +- sqrt(1 +8*t_n))/2

-1+sqrt(9) / 2 =  1
-1+sqrt(441) / 2 = 10

'''

import math

with open('p42_words.txt') as file:
	words = file.read().split(',')
	count = 0
	
	for w in words:
		t_n = 0

		for ch in w[1:-1]:
			t_n += ord(ch)-64
		
		double_n = -1 +math.sqrt(1 +8*t_n)
		#print(double_n)
		
		if double_n.is_integer() and int(double_n)%2 == 0:
			count += 1

	print(count)

