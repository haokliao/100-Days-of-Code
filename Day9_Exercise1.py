student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
#🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

     
for student in student_scores:
  score = student_scores[student]
  if score >= 91:
    student_grades[student] = 'Outstanding'
  elif 81 <= score <= 90:
    student_grades[student] = "Exceeds Expectations"
  elif 71 <= score <= 80:
    student_grades[student] = "Acceptable"
  else: 
    student_grades[student] = "Fail"
   

#🚨 Don't change the code below 👇
print(student_grades)


