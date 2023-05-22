# Interakcja
imie = input("Jak masz na imię?\n")
print("Miło mi Cię poznać", imie)
komputer = "Laptop"
print("Mam na imię", komputer, ".")
wiek = input("Ile masz lat\n")
wiek = float(wiek)
if wiek <= 6:
    print(imie, ", jesteś za młody aby samodzielnie przeczytać książkę.")
if wiek >= 100:
    print("Jesteś już za stary na czytanie", imie, ".\nLepiej siedź w domu")
if 6 < wiek < 100:
    print("To bardzo dobry wiek. Do setki masz jeszcze", 100 - wiek,
          "lat.\nZ jakiego peronu dostaniesz się do Hogwartu?")
    peron = input()
    if peron != "9 i 3/4":
        print(imie, ", prawidłowa nazwa peronu to '9 i 3/4'.\nNie przeczytałeś książek o HP. Czas na lekturę.")
    if peron == "9 i 3/4":
        print(imie, ", to bardzo dobra odpowiedź")
print("Dziękuję za miła rozmowę.\nPozdrawiam", komputer, ".")
