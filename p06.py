n = 100

sum_square = n*(n+1)*(2*n+1)//6
square_sum = (n*(n+1)//2)**2

print(square_sum-sum_square)

# brute force
'''
sum_square = 0
square_sum = 0

for i in range(1, 101):
	sum_square+=(i*i)
	square_sum+=i

print((square_sum**2)-sum_square)'''