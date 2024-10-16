# sortowanie z key
# lista = [[4, 9], [6, 2], [7, 4], [2, 3], [1, 1]]
# print(sorted(lista))

# C - A - B
# A - C - B
# A - B - C

# print(sorted(lista, key=lambda x: x[1]))

# lista = ["B", "A", "c", "C", "b"]
# print(sorted(lista, key=lambda znak: znak.upper()))

# def funkcja(element):
#     return element**3

# lista = [-10, 10, -4, 3, 0, 1, -2]
# print(sorted(lista, key=funkcja))


# lista = [
#     ["Zofia", 25, 180],
#     ["Kamil", 20, 180],
#     ["Marek", 30, 160],
#     ["Beata", 20, 160],
#     ["Anna", 25, 180],
# ]
# posortowana_lista = sorted(lista, key=lambda x: (x[1], x[2], x[0]), reverse=True)
# for osoba in posortowana_lista:
#     print(osoba)


#### ZADANIE 22

# Wczytaj dane z pliku zawodnicy.csv. Posortuj je po wadze i wyświetl na konsoli, od najcięższego zawodnika

# nazwa_pliku = "zawodnicy.csv"
# sep = ";"
# enc = "utf-8"

# # dane = []
# # for linia in open(nazwa_pliku, "r", encoding=enc).readlines():
# #     dane.append(linia.strip())

# dane = [linia.strip() for linia in open(nazwa_pliku, "r", encoding=enc).readlines()]
# dane = [rekord.split(sep) for rekord in dane]
# dane = [[r[0], r[1], float(r[2]), float(r[3])] for r in dane]
# print(dane)

# posortowane_dane = sorted(dane, key=lambda r: r[3], reverse=True)
# print(posortowane_dane)


# .join()

# napis = "ala ma\nkota\ta kot ma ale"
# print(napis.split())

# lista = ["ala", "ma", "kota", "a", "kot", "ma", "ale", 1]
# print(lista)

# sklejone = ""
# for i, el in enumerate(lista):
#     if i == 0:
#         sklejone = el
#     else:
#         sklejone = sklejone + "+" + str(el)
# print(sklejone)


# wynik = " ".join([str(el) for el in lista])
# print(wynik)


# zadanie -> wynik obliczenia BMI do pliku, posortowane


#### ZADANIE 23

# Napisz program, który pobierze dane z pliku zawodnicy.csv i wyliczy dla każdego z zawodników
# jego BMI. Wynik - imie, nazwisko, bmi - zapisz do nowego pliku.

# BMI = waga (w kg) / wzrost**2 (w m)

# nazwa_pliku = "zawodnicy.csv"
# sep = ";"
# enc = "utf-8"

# dane = [linia.strip() for linia in open(nazwa_pliku, "r", encoding=enc).readlines()]
# dane = [rekord.split(sep) for rekord in dane]
# dane = [[r[0], r[1], float(r[2]), float(r[3])] for r in dane]
# print(dane)

# # wynik printa:
# # [
# #     ['Jan', 'Nowak', 180.0, 80.0],
# #     ['Zdzisław', 'Kręcina', 160.0, 100.0],
# #     ['Marian', 'Koniuszko', 190.0, 60.0],
# #     ['Bogdan', 'Kowalski', 170.0, 90.0]
# # ]

# for rekord in dane:
#     bmi = rekord[3] / (rekord[2] / 100) ** 2
#     rekord.append(bmi)

# # teraz dane wyglądają tak:
# # [
# #     ["Jan", "Nowak", 180.0, 80.0, 24.691358024691358],
# #     ["Zdzisław", "Kręcina", 160.0, 100.0, 39.06249999999999],
# #     ["Marian", "Koniuszko", 190.0, 60.0, 16.62049861495845],
# #     ["Bogdan", "Kowalski", 170.0, 90.0, 31.14186851211073],
# # ]

# # "Jan;Nowak;24.691358024691358"

# # wersja 1 budowania linii wynikowej:
# # dane_do_zapisu = []
# # for r in dane :
# #     linia = f"{r[0]};{r[1]};{str(r[4])}\n"
# #     dane_do_zapisu.append(linia)

# # wersja 2 budowania linii wynikowej:
# dane_do_zapisu = [f"{r[0]};{r[1]};{str(r[4])}\n" for r in dane]


# print(dane_do_zapisu)
# # wynik:
# # [
# #     "Jan;Nowak;24.691358024691358",
# #     "Zdzisław;Kręcina;39.06249999999999",
# #     "Marian;Koniuszko;16.62049861495845",
# #     "Bogdan;Kowalski;31.14186851211073",
# # ]

# nazwa_pliku_wyjsciowego = "zawodnicy_bmi.csv"
# f = open(nazwa_pliku_wyjsciowego, "w", encoding=enc)
# f.writelines(dane_do_zapisu)
# f.close()


## Krotki - tuple

# lista = [ 1, 2, 3]
# krotka = (1, "2", 3.14, [123, 124, 15])
# print(lista)
# print(krotka)

# lista = list( [1,2,3] )
# krotka = tuple([1, 2, 3])
# print(lista)
# print(krotka)


# print(krotka[2])
# krotka[2] = "abc"
# print(krotka[2])

# krotka = ( 1, "abc", 3.14)
# lista = list(krotka)
# print(lista)
# print(krotka)


# krotka = (1, "abc", 3.14)
# for e in krotka:
#     print(e)


# krotka = tuple( [i for i in range(10)]  )
# print(krotka)

# krotki można dodawać
# k1 = (1, 2, 3)
# k2 = (4, 5, 6)
# print(k1 + k2)


##### ZADANIE 24

# Stwórz dwie krotki. Jedna ma zawierać 10 losowych liczb zakresu 1-10, druga 10 losowych liczb zakresu 11-20.
# Stwórz trzecią krotkę która ma zawierać dane z obu krotek. Trzecią krotkę wypisz na konsoli.


# import random

# ls1 = [random.randint( 1, 10) for _ in range(10)]
# kr1 = tuple(ls1)

# kr2 = tuple([random.randint(11, 20) for _ in range(10)])

# kr3 = kr1 + kr2
# print(kr3)


# lista plików

import os

for element in os.walk("."):
    sciezka = element[0]
    lista_katalogow = element[1]
    lista_plikow = element[2]

    # gdzie jestem?
    print(f"Jestem na poziomie {sciezka}")

    # katalogi
    print("Lista katalogów:")
    for k in lista_katalogow:
        print(f"\t- {k}")

    # pliki
    print("Lista plików:")
    for p in lista_plikow:
        print(f"\t- {p}")

    print("="*40)