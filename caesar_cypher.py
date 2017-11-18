# Caesar Cypher
# This program makes a copy of a text file translated
# to cyphertext using a user-provided key

# it asks the user to open a file on the system
# asks the user for the key
# opens the file for reading
# opens a new file for writing in the same directory
# converts the data to cypher text
# loads that new data to the new file
# closes both files

from tkinter.filedialog import askopenfilename
from graphics import *

# Draw everything in a window

win = GraphWin("Caesarify",500,500)
win.setCoords(0,0,10,10)
win.setBackground('white')

button = Rectangle(Point(1,4),Point(9,6))
button.setWidth(2)
button.draw(win)

instructions = Text(Point(5,5),"click to open a file to encrypt")
instructions.draw(win)

key_instructions = Text(Point(4,8),"key: ")
key_instructions.draw(win)

key = Entry(Point(5,8),4)
key.draw(win)

# Open a file and take a key from the user

while True:
    button.setFill('grey')
    instructions.setText("click to open a file to encrypt")

    win.getMouse()
    button.setFill('red')

    askopen = askopenfilename()
    if askopen == '':
        pass
    else:
        break
    
file = open(askopen, "r", encoding='utf-8')
filename = file.name.split('/')[-1]

instructions.setText("click to encrypt " + filename)

win.getMouse()
key_value = int(key.getText())

instructions.setText("encrypting")
button.setFill('blue')

# start up a cypher file for writing

cypher_directory = '/'.join(file.name.split('/')[:-1])
cypher_file = open(cypher_directory + '/' + filename[:-4] + "_caesar" +
                   filename[-4:], "w", encoding='utf-8')

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
            'o','p','q','r','s','t','u','v','w','x','y','z']

# append the cypher lines to the new file

for line in file:
    cypher_line = []
    for char in line.lower():
        if char in alphabet:
            char_index = alphabet.index(char)
            new_index = char_index + key_value
            if new_index > 25:
                new_index -= 26
            cypher_char = alphabet[new_index]
            cypher_line.append(cypher_char)

        else:
            cypher_line.append(char)
    cypher_line = ''.join(cypher_line)
    print(cypher_line, file=cypher_file, end='')
            

cypher_file.close()
file.close()

# tell user the file was encrypted

instructions.setText("file encrypted")
button.setFill('green')

# I encrypted the letters of asa gray with a key of 3











