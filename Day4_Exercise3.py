# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

#your output will be two numbers, column,row [0,1]
# 23
column = int(position[0])
row = int(position[1])

#choice row will look through map for the second number indicated.
#choice row now will equal the row of that second number
#choice row now prints out whichever row, 1,2,3 that you've selected
#from that row you've selected, choice row will overwrite the digit with x

choice_row = map[row-1][column-1] = "x"

print(f"{row1}\n{row2}\n{row3}")