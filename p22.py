import time
#import re


t_0 = time.time()

with open('p022_names.txt') as file:
	name_str = file.read()
	#names = re.sub('"', '', names)
	name_list = name_str[1:-1].split('","')

name_list_s = sorted(name_list)
bias = ord('A')-1 

total_s = 0
for i in range(len(name_list_s)):
	s = 0
	for ch in name_list_s[i]:
		s+=ord(ch)-bias

	total_s+=s*(i+1)

print('time:', time.time()-t_0)
print(total_s)


	