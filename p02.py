fib = 1
fib_1 = 0
fib_2 = 0
even_fib_sum = 0

while fib <= 4000000:
	fib_2 = fib_1
	fib_1 = fib
	fib = fib_1+fib_2
	
	if fib%2==0:
		even_fib_sum+=fib

	print(fib)

print("even_fib_sum: "+str(even_fib_sum))