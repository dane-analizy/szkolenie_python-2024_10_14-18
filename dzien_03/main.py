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


# .join()

# zadanie -> wynik obliczenia BMI do pliku, posortowane
