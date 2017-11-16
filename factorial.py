def factorial(num):

    if num <= 1:
        return 1
    else:
        result = num * factorial(num - 1)
        return result

print("5! = ", factorial(5))

# recursive function: a function that calls itself
