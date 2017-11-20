# largest of three
# this program finds the largest of 3 provided values

# ask user for 3 values separated by commas
# assign to a, b, and c
# make function called compare which takes two values and
# returns the greater
# call compare on a and b
# call compare on the result and c

def compare(num1, num2):
    if int(num1) >= int(num2):
        return num1
    elif int(num2) >= int(num2):
        return num2

def main():
    print("this program finds the greatest of three integers")
    a, b, c = input("provide three integers separated by commas ").split(',')

    greatest = compare(compare(a, b), c)
    print("the greatest of the three integers is " + greatest)

if __name__ == '__main__':
    main()

# a better way to do this would have been sequential decisions
# store the first value and go through the list of remaining values
# storing the new value if it is greater
