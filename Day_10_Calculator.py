def add(n1,n2):
	return n1 + n2

def subtract(n1,n2):
	return n1 - n2

def multiply(n1,n2):
	return n1 * n2

def divide(n1,n2):
	return n1 / n2

operations = {
"+": add,
"-": subtract,
"*": multiply,
"/": divide
}

def calculator():
	num1 = float(input('What\'s the first number: '))
	for op in operations:
		print(op)
	operation_choice = input('Pick an operation from the line above \n')
	num2 = float(input('What\'s the second number: '))
		
	calculation = operations[operation_choice]
	answer = calculation(num1, num2,)

	print(f'{num1} {operation_choice} {num2} = {answer}')

	continue_calculating = True
	while continue_calculating:

		keepgoing = input(f'Type \'y\' to continue calculating with {answer} or type \'n\' to start a new calculation. \n')
		print("")

		if keepgoing == 'y':
			num1 = answer
			operation_choice = input('Pick an operation\n')
			num2 = float(input('What\'s the next number: '))
			calculation = operations[operation_choice]
			answer = calculation(answer, num2)

			print(f'{num1} {operation_choice} {num2} = {answer}')
		else:
			continue_calculating = False
			calculator()

calculator()