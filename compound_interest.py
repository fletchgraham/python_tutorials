# user enters initial investment amount and their interest

amount = float(input("what is your investment amount "))
rate = float(input("what is your interest rate "))

# each year the amount increases by investment amount plus the interest rate

#print the earnings after 10 years

initial = amount

for i in range(10):
	amount = amount + amount * rate + initial
	print(amount)

print("after ten years ya got: $" + str(amount))