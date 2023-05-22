from datetime import datetime


def pitn(n):
    result = list()
    calculated = {}

    for c in range(1, n):
        for b in range(1, c):
            for a in range(1, b):
                if a + b + c > n:
                    break
                a2, b2, c2 = a ** 2, b ** 2, c ** 2
                if a2 + b2 == c2 and not calculated.get((a, b, c), False):
                    result.append((a, b, c))
                    calculated[(a, b, c)] = True

    return result


t1 = datetime.now()
print('Start:', t1)

for n in pitn(1000):
    print(n)

t2 = datetime.now()
print('Stop:', t2)
allt = t2 - t1
print('Time of counting everything:', allt)
