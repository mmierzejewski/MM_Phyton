from datetime import datetime
import math

n = 10000  # first n primes
fn = "{:,}".format(n)
print('Range of prime numbers to', fn)
tmp_n = 1
p = 3
primes = [2]

t1 = datetime.now()
print('Start:', t1)

while tmp_n < n:

    is_prime = True
    for i in range(3, int(math.sqrt(p) + 1), 2):
        # range with step 2

        if p % i == 0:
            is_prime = False

    if is_prime:
        primes += [p]
        tmp_n += 1

    p += 2

mpn = (max(primes))
fmpn = "{:,}".format(mpn)
print('Max value of first', fn, 'PN:', fmpn)
t2 = datetime.now()
print('Stop:', t2)
tpn = t2 - t1
print('Count time:', tpn)
