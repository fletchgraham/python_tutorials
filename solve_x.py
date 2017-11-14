# user inputs equation
# assume x is first and it's always addition
# split the input and store the value on the left and the value on the right
# subtract left from right
# print the result

def solve_for_x(equation):
	equation_list = equation.split()
	q = int(equation_list[2])
	p = int(equation_list[4])
	x = p - q
	return x

print("x is equal to " + str(solve_for_x(input("gimme an equation "))))