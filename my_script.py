import random

deck = []

def new_deck():

	std_deck = [
	  # 2  3  4  5  6  7  8  9  10  J   Q   K   A
		2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
		2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
		2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
		2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
	]

	random.shuffle(std_deck)
	return std_deck[:]

def initial_hand_f(lst):
	lst.append(deck.pop(0))
	lst.append(deck.pop(0))

	return lst

def give_card(lst):
	lst.append(deck.pop(0))

	return lst

def sum_list(lst):

	return sum(lst)

deck = new_deck()
player_hand = []
dealer_hand = []

player_hand = initial_hand_f(player_hand)
dealer_hand = initial_hand_f(dealer_hand)

print("Player: " + str(player_hand))

while sum(player_hand) < 21:
	answer = input("To HIT press 'h' to STAND press 's'.")
	if answer == 'h':
		give_card(player_hand)
		print("Player: " + str(player_hand))

		for i, card in enumerate(player_hand):
			if sum_list(player_hand) > 10 and card == 11:
				player_hand[i] = 1
				print(player_hand)
		if sum_list(player_hand) > 21:
			print("Dealer: " + str(dealer_hand))
			print("Dealer win.")


	if answer == 's':
		print("Dealer: " + str(dealer_hand))
		if sum_list(dealer_hand) < 21 and sum_list(dealer_hand) < sum_list(player_hand):
			give_card(dealer_hand)
			for i, card in enumerate(dealer_hand):
				if sum_list(dealer_hand) > 10 and card == 11:
					dealer_hand[i] = 1
					print(dealer_hand)
			
			if sum_list(dealer_hand) > 21:
				print("Dealer: " + str(dealer_hand))
				print("Player win.")

				break

			
			if sum_list(dealer_hand) > sum_list(player_hand) and sum_list(dealer_hand) < 21:
				print("Dealer: " + str(dealer_hand))
				print("Dealer win.")

				break

		if sum_list(player_hand) > sum_list(dealer_hand) and sum_list(player_hand) < 21:
			print("Dealer: " + str(dealer_hand))
			print("Player win.")

			break

		if sum_list(dealer_hand) == sum_list(player_hand):
			print("It's a draw.")
			print("Dealer: " + str(dealer_hand))
			break


		elif sum_list(dealer_hand) > sum_list(player_hand):
			print("Dealer win.")
			break

		if sum_list(dealer_hand) == 21 and sum_list(player_hand) != 21:
			print("Dealer: " + str(dealer_hand))
			print("Dealer win.")
			break

		if sum_list(player_hand) == 21 and sum_list(dealer_hand) != 21:
			print("Dealer: " + str(dealer_hand))
			print("Player win.")
			break
	

if sum(player_hand) == 21:
	print("Dealer: " + str(dealer_hand))
	print("Player win.")