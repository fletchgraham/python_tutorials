# fn = fn-1 + fn-2
# where f0 = 0 and f1 = 1

def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        result = fib(num - 1) + fib(num - 2)
        return result

flirb = int(input("how far will you fibonacci? "))

i = 1
while i < flirb:
    print(fib(int(i)))
    i += 1

