
print('Welcome to the tip calculator!')
bill = float(input('What\'s the total bill? :'))


people = int(input('How many people are in your party? :'))
tip = int(input('What % of tip are you including? :'))
tip_float = float(1 + tip /100)

total = (bill/people) * tip_float
total_float = "{:.2f}".format(total)
print(total_float)