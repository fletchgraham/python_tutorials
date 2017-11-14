age = int(input("how old are you? "))

if age <= 5:
	print("go to kindergarten or preschool")

elif (age > 5) and (age <= 17):
	grade = age - 5
	if grade == 1:
		suffix = "st"
	elif grade == 2:
		suffix = "nd"
	elif grade == 3:
		suffix = "rd"
	elif grade > 3:
		suffix = "th"
	print("go to {}{} grade ya dingus".format(grade, suffix))

else:
	print("go to college")