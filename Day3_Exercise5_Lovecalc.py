print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = name1 + name2
lower_names = combined_names.lower()

T = lower_names.count("t")
R = lower_names.count("r")
U = lower_names.count("u")
E = lower_names.count("e")
true_count = (T+R+U+E)

L = lower_names.count("l")
O = lower_names.count("o")
V = lower_names.count("v")
E = lower_names.count("e")
love_count = (L+O+V+E)

love_score = int(str(true_count) +str(love_count))

if (love_score < 10) or (love_score > 90):
	print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
	print(f"Your score is {love_score}, you are alright together.")
else:
	print(f"Your score is {love_score}.")

