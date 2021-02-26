
'''
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
'''

import numpy as np


l = 1001
A = np.zeros((l, l))
i = l//2
j = l//2
radius = 1
a = 1
A[i,j] = 1

def move_right():
	global i, j, A, a
	j+=1
	a+=1
	A[i, j] = a
	#print(A)

def move_left():
	global i, j, A, a
	j-=1
	a+=1
	A[i, j] = a
	#print(A)

def move_up():
	global i, j, A, a
	i-=1
	a+=1
	A[i, j] = a
	#print(A)

def move_down():
	global i, j, A, a
	i+=1
	a+=1
	A[i, j] = a
	#print(A)


# disegno scacchiera
while radius <= l//2:
	move_right()
	#print()

	for k in range(radius*2-1):
		move_down()
		#print()
	for k in range(radius*2):
		move_left()
		#print()
	for k in range(radius*2):
		move_up()
		#print()
	for k in range(radius*2):
		move_right()
		#print()
	
	radius+=1


# conto sulle diagonali
s = 0
for i in range(l):
	for j in range(l):
		if i == j:
			s+=A[i, j]

		elif i+j==l-1:
			s+=A[i, j]

print(s)
