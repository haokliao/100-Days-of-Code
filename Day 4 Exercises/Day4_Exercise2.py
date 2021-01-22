#pick in list generator without using random.choice()

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")

import random

#create a list, add names to list, create random from 0 to the length of list (0,last)
#make that number = number in list
#print it out

x = len(names)
choice = random.randint(0,x-1)
print(choice)
y = names[choice]

print(y +  " is going to buy the meal today!")
