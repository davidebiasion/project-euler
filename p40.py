l = 0
i = 1
num = ''
limit = 1000000

while l<limit:
	num+=str(i)
	l+=len(str(i))

	i+=1

res = int(num[0])*int(num[9])*int(num[99])*int(num[999])*int(num[9999])*int(num[99999])*int(num[999999])
print(res)
