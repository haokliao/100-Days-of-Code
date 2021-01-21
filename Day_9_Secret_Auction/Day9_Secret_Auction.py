from Day9_Secret_Auction_Art import logo
# from replit import clear
# uses replit's clear function!
print(logo)
auction_run = True


bids = {}
while auction_run:
	name = input('Please enter a Name \n ')
	price= input('Please enter your Bid Price \n')
	bids[name] = price
	users = input('Are there other users who want to bid? Type \'y\' or \'n\' \n')
	if users == "n":
	  auction_run = False
	  winner = max(bids,key=bids.get)
	  print(f'The winner of the auction is {winner} with the winning bid of {bids[winner]} ')
	else: 
		# clear()
		print(logo)