#Password Generator Project
#Ended up doing two versions : one with loops, one without loops.

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

easypassword = ""

for i in range(1,nr_letters +1):
	easypassword += random.choice(letters)
for i in range(1,nr_numbers +1):
	easypassword += random.choice(numbers)	
for i in range(1,nr_symbols +1):
	easypassword += random.choice(symbols)
print(f'This is your easy password: {easypassword}')

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P# hardpassword = ""

hardpassword = ""

for i in range(1,nr_letters +1):
	hardpassword += random.choice(letters)
for i in range(1,nr_numbers +1):
	hardpassword += random.choice(numbers)	
for i in range(1,nr_symbols +1):
	hardpassword += random.choice(symbols)
lists = list(hardpassword)
random.shuffle(lists)
hard_password = ''.join(lists)
print(f'This is your hard password: {hard_password}')


####Code without loops###

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

easymode = [] 

randoletters = random.choices(letters, weights=None,k = nr_letters)
randonumbers = random.choices(numbers, weights=None,k = nr_numbers)
randosymbols = random.choices(symbols, weights=None,k = nr_symbols)

easymode.extend(randoletters)
easymode.extend(randonumbers)
easymode.extend(randosymbols)
easy_password = ''.join(easymode)
print(f'This is your easy password: {easy_password}')

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hardmode = [] 
randoletters = random.choices(letters, weights=None,k = nr_letters)
randonumbers = random.choices(numbers, weights=None,k = nr_numbers)
randosymbols = random.choices(symbols, weights=None,k = nr_symbols)

hardmode.extend(randoletters)
hardmode.extend(randonumbers)
hardmode.extend(randosymbols)
random.shuffle(hardmode)
hard_password = ''.join(hardmode)
print(f'This is your hard password: {hard_password}')
