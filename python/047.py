# Distinct primes factors
# Project Euler - Problem 47
# Sean Malloy
from functools import lru_cache

MAX_NUM = 10**6
primes = [True for _ in range(MAX_NUM+1)]
primes[0] = primes[1] = False
inc = 2
while inc * inc < len(primes):
    if primes[inc]:
        for i in range(inc * inc, len(primes), inc):
            primes[i] = False
    inc += 1 if inc == 2 else 2

def prime_factors(num):
    factors = set()
    f = 2
    inc = 1
    while num > 1:
        while not primes[f]:
            f += 2
        if num % f == 0:
            factors.add(f)
            while num % f == 0:
                num //= f
        f = 3 if f == 2 else f+2
    return factors

seen_factors = {
    2: len(prime_factors(2)),
    3: len(prime_factors(3)),
    4: len(prime_factors(4))
}

FACTOR_COUNT = 4
n = 2
while True:
    found = True
    for i in range(FACTOR_COUNT):
        if n+i not in seen_factors:
            seen_factors[n+i] = len(prime_factors(n+i))
        if seen_factors[n+i] < FACTOR_COUNT:
            found = False
            n += i+1
            break
    if found:
        print(n)
        break
