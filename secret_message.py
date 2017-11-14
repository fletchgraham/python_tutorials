# user inputs a string

# we convert it to unicode and print

# we convert it back and print

message = input("enter a string to hide: ")

code = ''

for char in message:
    code = code + str(ord(char)-50)

print(code)

decode = ''

for i in range(0, len(code)-1, 2):
    decode = decode + chr(int(code[i] + code[i+1]) + 50)

print(decode)