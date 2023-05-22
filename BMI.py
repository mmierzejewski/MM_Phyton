# Obliczanie BMI
# Stopnie otyłości
# * mniej niż 16 - wygłodzenie
# * 16 - 16.99 - wychudzenie
# * 17 - 18.49 - niedowaga
# * 18.5 - 24.99 - wartość prawidłowa
# * 25 - 29.99 - nadwaga
# * 30 - 34.99 - I stopień otyłości
# * 35 - 39.99 - II stopień otyłości
# * powyżej 40 - otyłość skrajna
imie = input("Jak masz na imię?\n")
print("Miło mi Cię poznać", imie)
waga = input("Podaj swoją wagę w kg\n")
waga = float(waga)
wzrost = input("Podaj swój wzrost w cm\n")
wzrost = int(wzrost)
BMI = waga / ((wzrost/100) ** 2)
Low = round((((18.5/BMI)-1)*100), 2)
High = round(((BMI/24.99)-1)*100, 2)
if BMI < 18.49:
    print("Twoje MBI to:", round(BMI, 2), ". Masz niedowagę", imie, ". Niedobrze... Prawidłowe BMI jest w zakresie od "
                                                                    "18.5 do 24.99. Za mało o", Low, "%")
if 18.5 < BMI < 24.99:
    print("Twoje MBI to:", round(BMI, 2), ". Waga prawidłowa", imie, "!"" Gratulacje!")
if BMI > 25:
    print("Twoje MBI to:", round(BMI, 2), ". Masz nadwagę", imie, ". Niedobrze... Prawidłowe BMI jest w zakresie od "
                                                                  "18.5 do 24.99. Za dużo o", High, "%")
