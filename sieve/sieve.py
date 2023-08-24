
def primes(limit):
    '''Return prime number using Erastostenes Sieve'''
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    number = 2
    while number < limit:
        for multiple in range(number + number, limit + 1, number):
            sieve[multiple] = False
        number += 1
        while not sieve[number] and number < limit:
            number += 1
        # number is prime
    return [number for number in range(2, len(sieve)) if sieve[number]]

# function of other user
def primes2(limit):
    numbers = set(range(2, limit + 1))
    marked = {m for n in numbers for m in range(2 * n, limit + 1, n)}
    return sorted(numbers - marked)

if __name__ == '__main__':
    import time
    LIMIT = 10_000
    start_time = time.time()
    primes(LIMIT)
    end_time = time.time()
    print(f"Primes  time: {end_time - start_time}")
    start_time = time.time()
    primes(LIMIT)
    end_time = time.time()
    print(f"Primes2 time: {end_time - start_time}")