#find biggest score using for loops without using max


student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

bigscore = 0

for scores in student_scores:
	if scores > bigscore:
		bigscore = scores
print(f'The highest score in the class is: {bigscore}')