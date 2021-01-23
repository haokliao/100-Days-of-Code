print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("You\'re at a cross road. Where do you want to go? Type \"left\" or \"right\"")
left_right = input()
if left_right == "left":
  print('There\'s a crossing up ahead, it kinda looks swimmable but you\'re pretty out of shape from quarantine, you tryna risk it? Type \"swim\" or \"wait\"')

  swim_wait = input()
  if swim_wait == "wait":
    print('So far so good! Waiting seems to be the right decision, as some rinky dink hole ridden minecraft lookin\' boat decided to slowly drift towards you. You decide that waiting further is a bad idea, and to just take the plunge, seeing how far ol\' Faithful will get ya.')
    print('As you float further and further on, the SS Freedom seems to take it\'s last breaths, as it sinks to the bottom of the ocean, leaving you in awe, at how far you got with what seemed like three planks and some duct tape.')
    print('You\'ve arrived on a small island with three doors. Red, Blue, and Yellow doors. Pick your poison! Type \"red\",\"blue\",\"yellow\" for your choice of door.')

    color_door = input()
    if color_door == 'red' :
      print('red fire burn bad ouch ouch uh oh stinky. Game Over.')
    elif color_door == 'blue':
      print('oh no, uh oh stinky bad bad monster yum yum eat u. Game Over.')
    elif color_door == 'yellow' :
      print('And that\'s a BIG POGGERS IN THE CHAT for you, the door yells, as you open it to a portal, with a chest overflowing with gold. As you approach the chest, your left pocket buzzes from a call from your tax attorney. All treasures and profits from adventuring get taxed 15% from the government. But besides that, You win!')
    else: 
      print('Uh oh stinky. Game Over')
  else:
    print('That 15th bag of doritos really showed you who\'s boss. You got out of breath, halfway, and a troat floated into your mouth and you drowned. Game over.')
else:
  print('You fell into a hole you clutz. Game over')