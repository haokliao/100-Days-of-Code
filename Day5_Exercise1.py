#create a loop that'll find averages in a list WITHOUT USING sum/len()


###given code
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
###

total_heights = 0
for height in student_heights:
  total_heights += height

total_students =0
for students in student_heights:
  total_students += 1


print(round(total_heights/total_students))