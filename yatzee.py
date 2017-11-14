# user enters a wager

# add the wager to the pot

# five random numbers get converted to 1-6 like dice

# print the pot and print the five numbers

# do it until all the numbers are the same at which point you get yatzee
import random

pot = 0

while True:
	wager = int(input("what do you wager? "))
	pot += wager
	roll=[]
	for i in range(5):
		roll.append(int(random.random() * 6 + 1))

	print(roll) 
	ch1 = (roll[0] == roll[1])
	ch2 = (roll[1] == roll[2])
	ch3 = (roll[2] == roll[3])
	ch4 = (roll[3] == roll[4])
	
	print("pot: ${}".format(pot))

	if ch1 and ch2 and ch3 and ch4:
		print("dang, you got yatzee and won ${}".format(pot))
		break
	else:
		print("you didn't win make another wager")
