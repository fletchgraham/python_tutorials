# ask user for range
my_limit = input('what is the limit? ')


def list_primes(limit):
    limit = int(limit)
    primes = []
    # append all of the primes to a list
    for i in range(1, limit):
        is_prime = False
        for j in range(1, i):
            if int(i % j) == 0 and i != j and j != 1:
                is_prime = False
                break
            else:
                is_prime = True
        if is_prime:
            primes.append(i)
    # return the list
    return primes

print(list_primes(my_limit))

# surely there is a simpler way to make a list of primes.
