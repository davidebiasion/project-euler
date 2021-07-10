v = 'ABCD'
print(v[0]!=v[1] and v[1]!=v[2] and v[2]!=v[3] and v[0]!=v[2] and v[0]!=v[3] and v[1]!=v[3])

h = ['8C', 'TS', 'KC', '9H']
sorted_hand = []
for card in h:
	if card[0]=='T':
		sorted_hand.append(['10', card[1]])
	elif card[0]=='J':
		sorted_hand.append(['11', card[1]])
	elif card[0]=='Q':
		sorted_hand.append(['12', card[1]])
	elif card[0]=='K':
		sorted_hand.append(['13', card[1]])
	elif card[0]=='A':
		sorted_hand.append(['14', card[1]])
	else:
		sorted_hand.append([card[0], card[1]])



print(sorted_hand)
print(sorted(sorted_hand, key=lambda card: int(card[0])))



v[0]!=v[1] and v[1]!=v[2] and v[0]!=v[2]
