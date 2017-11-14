# get a string from the user

# make a list of the words

# for each word put the first word into a strin

# print thue uppercase of the string

phrase = input("give me a string to acronymify: ")

phrase_list = phrase.split()

acro = ''

for word in phrase_list:
    acro = acro + word[0].upper()

print(acro)	
