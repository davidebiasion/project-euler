'''

	|.
	|  .
  a	|     .  c
	|        .
	|___________
          b



p = a+b+c
c**2 = a**2 + b**2
a = i

p=i+b+c
c**2 = i**2+b**2
a=i

b=p-i-c
c**2=i**2+(p-i-c)**2
a=i

b=p-i-c
c**2 = i**2 + p**2 + i**2 + c**2 - 2pi + 2ic -2pc
a=i

b = p-i-c
0 = 2*i**2 + p**2 - 2pi + 2ic - 2pc --> 2c(i-p) = -2*i**2 - p**2 + 2pi --> c = 0.5*(-2*i**2 - p**2 + 2pi)/(i-p)     
a = i

b = p-i-c
c = 0.5*(-2*i**2 -p**2 +2pi)/(i-p)
a = i

'''

ps = {}

p = 1000
while p >= 3:
	ps[p] = []

	a = 1
	while a < p-2*a:
		c = 0.5*(-2*(a**2) -p**2 +2*p*a)/(a - p)
		b = p-a-c

		if c.is_integer():
			ps[p].append([a, b, c])
			#print('p', p, 'a', a, 'b', b, 'c', c)

		a+=1
	
	p-=1


max_p = -1
max_terne = -1
for p in ps:
	if len(ps[p]) > max_terne:
		max_terne = len(ps[p])
		max_p = p

print('max p:', max_p, 'max_terne:', max_terne)
#print(ps[max_p])





