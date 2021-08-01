import time


keys = []
'''
for a in range(97, 123):
	for b in range(97, 123):
		for c in range(97, 123):
			keys.append([a, b, c])

'''

with open('p059_cipher.txt') as file:
	message = file.read().split(',')

# compute frequencies of encrypted letters
dic = {}
for letter in message:
	if int(letter) in dic:
		dic[int(letter)]+=1
	else:
		dic[int(letter)] = 1

sorted_dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
print('FREQUENCIES:')
print(sorted_dic)

# most frequent encrypted letter is 80
# most frequent english letter is 'e' (ASCII code 101)
# let's find the key such that 80 XOR key = 101
for ch in range(97, 123):
	if 80^ch==ord('t'):
		print('found!')
		break

