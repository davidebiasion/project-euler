import math


def pandigital_produts(a, n):
	i = 1
	while i <= math.sqrt(a):
		if a%i == 0:
			#print(str(a)+" = "+str(i)+" * "+str(a//i))
			
			id_to_str = str(a)+str(i)+str(a//i)
			id_to_str = sorted(id_to_str)
			#print(id_to_str)
			
			if is_pandigital(id_to_str, n):
				return True
			#print("")

		i+=1

	return False


def is_pandigital(s, n):
	if len(s) != n:
		return False

	j = 0
	while j<len(s) and s[j]==str(j+1):
		j+=1

	return j == n


pan_prod = []
for i in range(1, 100000):
	if pandigital_produts(i, 9):
		pan_prod.append(i)

print(pan_prod)
print(sum(pan_prod))