# Prime numbers algorithm
import math
from datetime import datetime

t1 = datetime.now()
print('Start:', t1)

primary = []


def if_primary(a):
    if a < 2:
        return False
    for i in (range(2, int(math.sqrt(a)))):
        if a % i == 0:
            return False
    return True


def mark_primary(a):
    for i in range(2, a):
        if if_primary(i) is True:
            primary.append(i)
    return


m = 1000000

mark_primary(m)
# print(primary)
# print ("Amount of prime numbers in range from 2 to", m, ":", (len(primary)))
t2 = datetime.now()
print('Stop:', t2)
n = t2 - t1
print("Time of counting:", n)
print("The highest prime number in that range to", m, "is", (max(primary)))
