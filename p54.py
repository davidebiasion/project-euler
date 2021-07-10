import time

'''
High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
'''

def score(hand):
	#s = 0

	possible_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
	possible_suits = ['H', 'D', 'C', 'S']

	'''
	values = []
	for card in hand:
		if card[0]=='T':
			values.append('10')
		elif card[0]=='J':
			values.append('11')
		elif card[0]=='Q':
			values.append('12')
		elif card[0]=='K':
			values.append('13')
		elif card[0]=='A':
			values.append('14')
		else:
			values.append(card[0])
	values = sorted(values)
	'''

	sorted_hand = []
	for card in hand:
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
	sorted_hand = sorted(sorted_hand, key=lambda card: int(card[0]))

	values = []
	for card in sorted_hand:
		values.append(card[0])

	suits = []
	for card in sorted_hand:
		suits.append(card[1])

	same_suit = False
	for ps in possible_suits:
		if suits==[ps, ps, ps, ps, ps]:
			same_suit = True
			break

	consec_values = False
	for i in range(len(possible_values)):
		if values[0]==possible_values[i]:
			if i<9 and values==possible_values[i:i+5]:
				consec_values = True
				break

	three_kind_pair = (values[0]==values[1] and values[1]==values[2] and suits[0]!=suits[1] and suits[1]!=suits[2] and suits[0]!=suits[2]) and (values[3]==values[4] and suits[3]!=suits[4])
	pair_three_kind = (values[0]==values[1] and suits[0]!=suits[1]) and (values[2]==values[3] and values[3]==values[4] and suits[2]!=suits[3] and suits[3]!=suits[4] and suits[2]!=suits[4])

	four_kind_0_3 = values[0]==values[1] and values[1]==values[2] and values[2]==values[3] and suits[0]!=suits[1] and suits[1]!=suits[2] and suits[2]!=suits[3] and suits[0]!=suits[2] and suits[0]!=suits[3] and suits[1]!=suits[3]
	four_kind_1_4 = values[1]==values[2] and values[2]==values[3] and values[3]==values[4] and suits[1]!=suits[2] and suits[2]!=suits[3] and suits[3]!=suits[4] and suits[1]!=suits[3] and suits[1]!=suits[4] and suits[2]!=suits[4]

	# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
	if same_suit and values==['10', '11', '12', '13', '14']:
		return 10, values

	# Straight Flush: All cards are consecutive values of same suit.
	if consec_values and same_suit:
		return 9, values

	# Four of a Kind: Four cards of the same value.
	if four_kind_0_3 or four_kind_1_4:
		return 8, values

	# Full House: Three of a kind and a pair.
	if three_kind_pair or pair_three_kind:
		return 7, values

	# Flush: All cards of the same suit.
	elif same_suit:
		return 6, values

	# Straight: All cards are consecutive values.
	elif consec_values:
		return 5, values
	
	# Three of a Kind: Three cards of the same value.
	three_kind_0_2 = values[0]==values[1] and values[1]==values[2] and suits[0]!=suits[1] and suits[1]!=suits[2] and suits[0]!=suits[2]
	three_kind_1_3 = values[1]==values[2] and values[2]==values[3] and suits[1]!=suits[2] and suits[2]!=suits[3] and suits[1]!=suits[3]
	three_kind_2_4 = values[2]==values[3] and values[3]==values[4] and suits[2]!=suits[3] and suits[3]!=suits[4] and suits[2]!=suits[4]
	#elif (values[0]==values[1] and values[1]==values[2]) or (values[1]==values[2] and values[2]==values[3]) or (values[2]==values[3] and values[3]==values[4]):
	if three_kind_0_2 or three_kind_1_3 or three_kind_2_4:
		return 4, values
	
	
	# Two Pairs: Two different pairs.
	pair_01_23 = values[0]==values[1] and suits[0]!=suits[1] and values[2]==values[3] and suits[2]!=suits[3] and values[0]!=values[2]
	pair_01_34 = values[0]==values[1] and suits[0]!=suits[1] and values[3]==values[4] and suits[3]!=suits[4] and values[0]!=values[3]
	pair_12_34 = values[1]==values[2] and suits[1]!=suits[2] and values[3]==values[4] and suits[3]!=suits[4] and values[1]!=values[3]
	#elif (values[0]==values[1] and values[2]==values[3]) or (values[0]==values[1] and values[3]==values[4]) or (values[1]==values[2] and values[3]==values[4]):
	if (pair_01_23 or pair_01_34 or pair_12_34):
		return 3, values

	# One Pair: Two cards of the same value.
	pair_01 = values[0]==values[1] and suits[0]!=suits[1]
	pair_12 = values[1]==values[2] and suits[1]!=suits[2]
	pair_23 = values[2]==values[3] and suits[2]!=suits[3]
	pair_34 = values[3]==values[4] and suits[3]!=suits[4]
	#elif values[0]==values[1] or values[1]==values[2] or values[2]==values[3] or values[3]==values[4]:
	if pair_01 or pair_12 or pair_23 or pair_34:
		return 2, values

	# High Card: Highest value card.
	return 1, values
	

	#return s, values


with open('p054_poker.txt') as f:
	hands = f.readlines()
	winning_hands_1 = 0
	winning_hands_2 = 0

	for hand in hands:
		h1 = hand[:14].split()
		h2 = hand[15:-1].split()
			
		s1, v1 = score(h1)
		s2, v2 = score(h2)

		if s1>s2:
			winning_hands_1+=1
		elif s2>s1:
			winning_hands_2+=1
		else: # s1==s2
			# Straight Flush: All cards are consecutive values of same suit.
			if s1==9:
				if v1[0]>v2[0]:
					winning_hands_1+=1
				elif v1[0]<v2[0]:
					winning_hands_2+=1

			# Four of a Kind: Four cards of the same value.
			if s1==8:
				# xxxxy
				# xxxxy

				# xxxxy
				# yxxxx
				if v1[0]==v1[1]:
					if v2[0]==v2[1]:
						if v1[0]>v2[0]:
							winning_hands_1+=1
						elif v1[0]<v2[0]:
							winning_hands_2+=1
						elif v1[4]>v2[4]:
							winning_hands_1+=1
						elif v1[4]<v2[4]:
							winning_hands_2+=1
					else:
						if v1[0]>v2[1]:
							winning_hands_1+=1
						elif v1[0]<v2[1]:
							winning_hands_2+=1
						elif v1[4]>v2[0]:
							winning_hands_1+=1
						elif v1[4]<v2[0]:
							winning_hands_2+=1

				# yxxxx
				# yxxxx

				# yxxxx
				# xxxxy
				else:
					if v2[0]!=v2[1]:
						if v1[1]>v2[1]:
							winning_hands_1+=1
						elif v1[1]<v2[1]:
							winning_hands_2+=1
						elif v1[0]>v2[0]:
							winning_hands_1+=1
						elif v1[0]<v2[0]:
							winning_hands_2+=1
					else:
						if v1[1]>v2[0]:
							winning_hands_1+=1
						elif v1[1]<v2[0]:
							winning_hands_2+=1
						elif v1[0]>v2[4]:
							winning_hands_1+=1
						elif v1[0]<v2[4]:
							winning_hands_2+=1

			# Full House: Three of a kind and a pair.
			if s1==7:
				# xxxyy
				# xxxyy

				# xxxyy
				# yyxxx
				if v1[0]==v1[2]:
					if v2[0]==v2[2]:
						if v1[0]>v2[0]:
							winning_hands_1+=1
						elif v1[0]<v2[0]:
							winning_hands_2+=1
						elif v1[3]>v2[3]:
							winning_hands_1+=1
						elif v1[3]<v2[3]:
							winning_hands_2+=1
					else:
						if v1[0]>v2[2]:
							winning_hands_1+=1
						elif v1[0]<v2[2]:
							winning_hands_2+=1
						elif v1[3]>v2[0]:
							winning_hands_1+=1
						elif v1[3]<v2[0]:
							winning_hands_2+=1						
				# yyxxx
				# yyxxx

				# yyxxx
				# xxxyy
				else:
					if v2[0]==v2[1]:
						if v1[2]>v2[2]:
							winning_hands_1+=1
						elif v1[2]<v2[2]:
							winning_hands_2+=1	
						elif v1[0]>v2[0]:
							winning_hands_1+=1
						elif v1[0]<v2[0]:
							winning_hands_2+=1	
					else:
						if v1[2]>v2[0]:
							winning_hands_1+=1			
						elif v1[2]<v2[0]:
							winning_hands_2+=1
						elif v1[0]>v2[3]:
							winning_hands_1+=1
						elif v1[0]<v2[3]:
							winning_hands_2+=1

			# Flush: All cards of the same suit. 
			# Straight: All cards are consecutive values.
			if s1==6 or s1==5:
				for i in range(4, -1, -1):
					if v1[i]>v2[i]:
						winning_hands_1+=1
						break
					elif v1[i]<v2[i]:
						winning_hands_2+=1
						break	

			# Three of a Kind: Three cards of the same value.
			if s1==4:
				three_kind_start_1 = -1
				three_kind_start_2 = -1
				for i in range(3):
					if v1[i]==v1[i+2]:
						three_kind_start_1 = i
						break
				for i in range(3):
					if v2[i]==v2[i+2]:
						three_kind_start_2 = i
						break
				if v1[three_kind_start_1]>v2[three_kind_start_2]:
					winning_hands_1+=1
				elif v1[three_kind_start_1]<v2[three_kind_start_2]:
					winning_hands_2+=1
				else:
					idxs_1 = [idx for idx in list(range(5)) if idx not in list(range(three_kind_start_1, three_kind_start_1+3))]
					idxs_2 = [idx for idx in list(range(5)) if idx not in list(range(three_kind_start_2, three_kind_start_2+3))]
					
					for i in range(1, -1, -1):
						if v1[idxs_1[i]]>v2[idxs_2[i]]:
							winning_hands_1+=1
							break
						elif v1[idxs_1[i]]<v2[idxs_2[i]]:
							winning_hands_2+=1
							break

			# Two Pairs: Two different pairs.
			if s1==3:
				high_pair_start_1 = -1
				high_pair_start_2 = -1
				for i in range(4, 2, -1):
					if v1[i]==v1[i-1]:
						high_pair_start_1 = i-1
						break
				for i in range(4, 2, -1):
					if v2[i]==v2[i-1]:
						high_pair_start_2 = i-1
						break
				low_pair_start_1 = -1
				low_pair_start_2 = -1
				for i in range(2):
					if v1[i]==v1[i+1]:
						low_pair_start_1 = i
						break
				for i in range(2):
					if v2[i]==v2[i+1]:
						low_pair_start_2 = i
						break

				rem_idx_1 = [idx for idx in list(range(5)) if idx not in [low_pair_start_1, low_pair_start_1+1, high_pair_start_1, high_pair_start_1+1]]
				rem_idx_2 = [idx for idx in list(range(5)) if idx not in [low_pair_start_2, low_pair_start_2+1, high_pair_start_2, high_pair_start_2+1]]				

				if v1[high_pair_start_1]>v2[high_pair_start_2]:
					winning_hands_1+=1
				elif v1[high_pair_start_1]<v2[high_pair_start_2]:
					winning_hands_2+=1
				elif v1[low_pair_start_1]>v2[low_pair_start_2]:
					winning_hands_1+=1
				elif v1[low_pair_start_1]<v2[low_pair_start_2]:
					winning_hands_2+=1
				elif v1[rem_idx_1]>v2[rem_idx_2]:
					winning_hands_1+=1
				elif v1[rem_idx_1]<v2[rem_idx_2]:
					winning_hands_2+=1

			# One Pair: Two cards of the same value.
			if s1==2:
				pair_start_1 = -1
				pair_start_2 = -1
				for i in range(4):
					if v1[i]==v1[i+1]:
						pair_start_1 = i	
						break
				for i in range(4):
					if v2[i]==v2[i+1]:
						pair_start_2 = i	
						break

				rem_idxs_1 = [idx for idx in list(range(5)) if idx not in [pair_start_1, pair_start_1+1]]
				rem_idxs_2 = [idx for idx in list(range(5)) if idx not in [pair_start_2, pair_start_2+1]]

				if v1[pair_start_1]>v2[pair_start_2]:
					winning_hands_1+=1

				elif v1[pair_start_1]<v2[pair_start_2]:
					winning_hands_2+=1

				else:
					for i in range(2, -1, -1):
						if v1[rem_idxs_1[i]]>v2[rem_idxs_2[i]]:
							winning_hands_1+=1
							break
						elif v1[rem_idxs_1[i]]<v2[rem_idxs_2[i]]:
							winning_hands_2+=1
							break


			# High Card: Highest value card.
			if s1==1:
				for i in range(4, -1, -1):
					if v1[i]>v2[i]:
						winning_hands_1+=1
						break
					elif v1[i]<v2[i]:
						winning_hands_2+=1
						break

	# devono essere 376
	print('winning_hands_1:', winning_hands_1) 
	print('winning_hands_2:', winning_hands_2)



