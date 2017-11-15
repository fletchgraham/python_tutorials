# multiplication table generator
def mult_table():
    # i is equal to 1
    i = 1
    # initiate table
    table = []
    # while i is less than 10
    while i < 10:
        # j is equal to 1
        j = 1
        # initiate row
        row = []
        # while j is less than 10
        while j < 10:
            # append j x i to row
            row.append(j * i)
            # increment j by 1
            j += 1
        # append row to table
        table.append(row)
        # increment i
        i += 1
    # print table
    print(table)

mult_table()


# Banas did this differently:
def banas_table():
    # he builds the whole table first:
    table = [[0] * 10 for i in range(10)]
    # then starts a for loop
    for i in range(1, 10):
        # another for loop
        for j in range(1, 10):
            # here he replaces the cells with one swanky line
            table[i][j] = i * j

    # then it gets printed in the same way
    for i in range(1, 10):
        for j in range(1, 10):
            # this is my own solution to keeping the table lined up
            if len(str(table[i][j])) == 1:
                print(table[i][j], end=",  ")
            if len(str(table[i][j])) == 2:
                print(table[i][j], end=", ")
        # this print statement makes a new line happen
        print()

banas_table()
