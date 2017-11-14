# randomly generate a number

# ask user to guess the number

# while the guess doesn't equal the number

number = 4

while True:
	guess = int(input("guess a number between one and ten "))

	if guess == number:
		print("you got it")
		break

