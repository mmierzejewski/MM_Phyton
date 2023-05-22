# Liczby pierwsze
pierwsze = [2]


def czy_pierwsza(liczba):
    for dzielnik in pierwsze:
        if liczba % dzielnik == 0:
            return False
        if dzielnik * dzielnik > liczba:
            return True
    return True


def wyznacz_pierwsze(liczba):
    for i in range(2, liczba):
        if czy_pierwsza(i) is True:
            pierwsze.append(i)
    return


m = 10000
wyznacz_pierwsze(m)
print(pierwsze)
print("Ilość wystąpień liczb pierwszych w zakresie do", m, ":", (len(pierwsze)))
