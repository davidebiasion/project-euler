def factorial(n):
	if n==0:
		return 1

	fac = 1
	for i in range(1, n+1):
		fac*=i

	return fac


nums = []
for i in range(3, 1000000):
	s = 0

	i_to_str = str(i)

	for ch in i_to_str:
		s+=factorial(int(ch))

	if s==i:
		nums.append(i)

print(nums)
print(sum(nums))