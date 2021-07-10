v = 'ABC'
print(v[0]!=v[1] and v[1]!=v[2] and v[0]!=v[2])

h = ['8C', 'TS', 'KC', '9H']
values = []
for card in h:
	if card[0]=='T':
		values.append(['10', card[1]])
	elif card[0]=='J':
		values.append(['11', card[1]])
	elif card[0]=='Q':
		values.append(['12', card[1]])
	elif card[0]=='K':
		values.append(['13', card[1]])
	elif card[0]=='A':
		values.append(['14', card[1]])
	else:
		values.append([card[0], card[1]])



print(values)
print(sorted(values, key=lambda card: int(card[0])))