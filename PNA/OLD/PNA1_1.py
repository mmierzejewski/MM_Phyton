# Prime numbers algorithm
import time
from datetime import datetime

t1 = time.time()
t1a = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
print("Start", t1a)

primary = []


def if_primary(number):
    for factor in primary:
        if number % factor == 0:
            return False
        if factor * factor > number:
            return True
    return True


def mark_primary(number):
    for i in range(2, number):
        if if_primary(i) is True:
            primary.append(i)
    return


m = 1000000000
mark_primary(m)
# print(primary)
t2 = time.time()
t2a = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
print("Stop", t2a)
print("Amount of prime numbers in range from 2 to", m, ":", (len(primary)))
print("The highest prime number in that range is", (max(primary)))
print("Time of counting:", round(t2 - t1, 2), "sec")
