# get a calculation from the user

calc = input("enter calculation ")

# make variables from the string

calc_split = calc.split()

num1 = float(calc_split[0])
operator = calc_split[1]
num2 = float(calc_split[2])

# perform the calculation and print

result = 0

if operator == '*':
	print("{} * {} = {}".format(num1, num2, num1 * num2))

elif operator == '/':
	print("{} / {} = {}".format(num1, num2, num1 / num2))

elif operator == '+':
	print("{} + {} = {}".format(num1, num2, num1 + num2))

elif operator == '-':
	print("{} - {} = {}".format(num1, num2, num1 - num2))

else:
	print("use + - / * next time")
