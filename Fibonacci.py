n = int(input("Podaj wartość n: "))

fib_prev = 0
fib_curr = 1

while fib_curr <= n:
    print(fib_curr)
    fib_next = fib_prev + fib_curr
    fib_prev = fib_curr
    fib_curr = fib_next
