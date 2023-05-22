# Prime numbers algorithm (by openai)
from datetime import datetime


def pna(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [x for x in range(n + 1) if primes[x]]


m = 1000000000
t1 = datetime.now()
print('Start:', t1)
print("Amount of prime numbers in range from 2 to", m, ":", len(pna(m)))
print("The highest prime number in that range to", m, "is", max(pna(m)))
t2 = datetime.now()
print('Stop:', t2)
a = t2 - t1
print("Time of counting everything:", a)
