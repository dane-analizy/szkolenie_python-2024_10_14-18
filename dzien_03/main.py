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


# .join(   )

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

# import os

# for element in os.walk("."):
#     sciezka = element[0]
#     lista_katalogow = element[1]
#     lista_plikow = element[2]

#     # gdzie jestem?
#     print(f"Jestem na poziomie {sciezka}")

#     # katalogi
#     print("Lista katalogów:")
#     for k in lista_katalogow:
#         print(f"\t- {k}")

#     # pliki
#     print("Lista plików:")
#     for p in lista_plikow:
#         print(f"\t- {p}")

#     print("="*40)


### ZADANIE 25


# Znajdź wszystkie pliki oraz katalogi, które w nazwie mają ciąg podany przez użytkownika.
# Wyświetl ścieżkę i nazwę znalezionego pliku/katalogu oraz informację czy to plik czy katalog.
# Jeśli chcesz - wyświetl to po przesortowaniu

# if ciag in dlugi_ciag

# import os

# ciag = input("Podaj fragment nazwy pliku lub katalogu, którego ma poszukać: ")


# znalezione = []
# for element in os.walk("."):
#     sciezka = element[0]
#     lista_katalogow = element[1]
#     lista_plikow = element[2]

#     # katalogi
#     for k in lista_katalogow:
#         if ciag in k:
#             # print(f"{sciezka}: {k} (katalog)")
#             znalezione.append((sciezka, k, "katalog"))

#     # pliki
#     for p in lista_plikow:
#         if ciag in p:
#             # print(f"{sciezka}: {p} (plik)")
#             znalezione.append((sciezka, p, "plik"))

# # [
# #     (".", "plikolog2", "katalog"),
# #     (".\\katalog1", "plikolog1", "katalog"),
# #     (".\\katalog1", "plik1", "plik"),
# #     (".\\katalog1\\katalog2", "plik2", "plik"),
# #     (".\\plikolog2", "plik3", "plik"),
# # ]

# znalezione.sort(key=lambda e: (e[2], e[0], e[1]))
# for e in znalezione:
#     print(e)


### zbiory - set

# krotka = (2, 1, 3, 1, "abc", "efg", "abc")
# zbior = set(krotka)
# print(krotka)
# print(zbior)

# lista = list(zbior)
# print(lista)

# lista = list(set( lista ))

# for e in zbior:
#     print(e)


# zbiór może się składać tylko z "hashowalnych" elementów - lista taka nie jest, krotka już tak
# zbior = set( [ 1, 2, 1, 2, (3, 4), (4, 3), (3, 4) ] )
# print(zbior)


# z1 = { 1, 2, 3, 4}
# z2 = { 4, 5, 6}
# z1.add(5)
# print(z1)
# z2.add(5)
# print(z2)
# print(z1.intersection(z2))
# print(z1.union(z2))
# print(z1.difference(z2))
# print(z2.difference(z1))

# import random
# z = { random.randint(1, 10) for _ in range(100)}
# l = [random.randint(1, 10) for _ in range(100)]
# print(z)
# print(l)

# l = list(set(l)) # <- usuwanie duplikatów z listy


### słowniki - dict()

# d = {
#     "klucz1": "wartosc1",
#     "klucz2": "wartosc2",
#     "klucz3": 123,
#     "klucz4": [1, 2, 3],
#     "klucz5": ("ab", "cd"),
#     "klucz6": {"k1": 1, "k2": "b", "k3": {"klucz5": ("ab", "cd")}},
#     "klucz1": "inna wartość 1",
#     # "imie": "Janek"
# }

# print(d)

# klucze
# print(d.keys())

# wartości
# print(d.values())

# for v in d.values():
#     print(type(v), v)
#     if isinstance(v, dict):
#         print("Wartość jest słownikiem")

# iteracja po kluczu z otrzymaniem od razu wartości
# for k,v in d.items():
#     print(f"Klucz  : {k}")
#     print(f"Wartość: {v}")


# print(d['klucz3'])

# if "imie" in d.keys():
#     print(d["imie"])
# else:
#     print("Nie mam klucza 'imie'")

# print( d.get("imie")  )

# if d.get("ajfhwughwguwg"):
#     print("ten klucz istnieje")
# else:
#     print("klucz nie istnieje")


# print(d.get("imie", 0))

# d['nazwisko'] = "Kowalski"
# for k,v in d.items():
#     print(f"{k} => {v}")

# dodanie nowego klucza o wartości "wartość" o ile nie istniał
# d["klucz"] = d.get("klucz", wartosc)


# zip() -> przejście przez wiele list na raz

# l1 = [1, 2, 3, 4, 5]
# l2 = ["a", "b", "c", "d"]

# print("iterator:")
# for i in range(len(l1)):
#     print(l1[i], l2[i])

# print("enumarate() i iterator:")
# for i, el1 in enumerate(l1):
#     print(el1, l2[i])

# print("zip():")
# for el1, el2 in zip(l1, l2):
#     print(el1, el2)


# from itertools import zip_longest

# kluczem w słowniku może być np. tuple:
# d = {
#     (2024, 10, 15, 13, 30, 25, "ID123", "typwartosci"): 99,
#     (2024, 10, 15, 13, 30, 25, "ID124", "typwartosci"): 199
# }

# print(d)


# dict comprehention - słowniki składane

# klucze = ("klucz1", "klucz2", "klucz3")
# wartosci = [123, "abc", 5.67]

# d = {k: v for k, v in zip(klucze, wartosci)}
# print(d)

# print(dict([(1, "a"), ("b", 2), ("klucz", "wartosc")]))
# print(dict([[1, "a"], ["b", 2], ["klucz", "wartosc"]]))
# print(dict(zip(klucze, wartosci)))


# print({ p:2**p for p in range(10)})

### ZADANIE 26

# Przepisz dane z pliku zawodnicy.csv do listy słowników.
# Niech klucze będą taki: imie, nazwisko, wzrost, waga


# nazwa_pliku = "zawodnicy.csv"
# sep = ";"
# enc = "utf-8"

# dane = [linia.strip() for linia in open(nazwa_pliku, "r", encoding=enc).readlines()]
# dane = [rekord.split(sep) for rekord in dane]
# dane = [[r[0], r[1], float(r[2]), float(r[3])] for r in dane]

# nazwy_kolumn = ("imie", "nazwisko", "wzrost", "waga")
# dane_wynikowe = []
# for rekord in dane:
#     dane_wynikowe.append(dict(zip(nazwy_kolumn, rekord)))

# print(dane_wynikowe)


# pakiet zewnętrze -> https://pypi.org/
# pip install nazwa-pakietu

# Faker - sztuczne dane -> https://pypi.org/project/Faker/
# pip install Faker

# from faker import Faker


# fake = Faker("pl_PL")
# print(fake.city())
# print(fake.first_name())
# print(fake.last_name())
# print(fake.pesel())


#### ZADANIE 27

# Korzystając z pakietu Faker wygeneruj plik zawierający 10 tysięcy rekordów składających się z:
# id będące kolejną liczbą,
# imię, -> first_name()
# nazwisko, -> last_name()
# nazwa firmy, -> company()
# email, -> email()
# telefon, -> phone_number()
# miasto -> city()

# proponowane podejście:
# lista słowników z każdą z osób osobno - 1 słownik = 1 osoba
# zapis list do pliku


# f = open()
# f....
# f.close()

# context manager
# with open(...) as f:
#     f....


# from faker import Faker

# fake = Faker("pl_PL")

# lista_osob = []
# for id in range(10_000):
#     osoba = {
#         "id": str(id+1),
#         "imie": fake.first_name(),
#         "nazwisko": fake.last_name(),
#         "nazwa_firmy": fake.company(),
#         "email": fake.email(),
#         "ulica": fake.street_name(),
#         "telefon": fake.phone_number(),
#         "miasto": fake.city()
#     }
#     lista_osob.append(osoba)


# lista_osob_do_pliku = [";".join(r.values())+"\n" for r in lista_osob]
# with open("ludzie.csv", "w", encoding="utf-8") as f:
#     f.writelines(lista_osob_do_pliku)


# # sortowanie słownika po kluczu
# import random

# d = { random.randint(1,100) : random.randint(1000, 2000) for _ in range(10) }
# print("Przed sorotowaniem:", d)

# d_posostowane = dict(sorted(d.items()))
# print("Po sortowaniu:", d_posostowane)

# sortowanie słownika po wartości
# import random

# d = {random.randint(1, 100): random.randint(1000, 2000) for _ in range(10)}
# print("Przed sorotowaniem:", d)

# d_posostowane = dict(sorted(d.items(), key=lambda kv: kv[1] ))
# print("Po sortowaniu:", d_posostowane)


### ZADANIE 28

# Korzystając z tekstu Pana Tadeusza w pliku pan-tadeusz.txt policz ile razy występuje każde ze słów.


# rozwiązanie 1
# import time

# text = open("pan-tadeusz.txt","r", encoding="utf-8").read()
# text = text.lower()

# zle_znaki = ".,!?;:()-—/\\\n\t…«»"
# for znak in zle_znaki:
#     text = text.replace(znak, " ")

# slowa = text.split()

# start_time = time.perf_counter()
# licznik = {}
# for slowo in slowa:
#     if not slowo:
#         continue
#     if len(slowo) <= 4:
#         continue
#     licznik[slowo] = licznik.get(slowo, 0) + 1
# stop_time = time.perf_counter()

# licznik = dict(sorted(licznik.items(), key=lambda kv: kv[1]))
# print(licznik)


# print(licznik['tadeusz'])
# print(licznik["tadeuszu"])

# print(stop_time - start_time)


# rozwiązanie 2
# import time

# text = open("pan-tadeusz.txt", "r", encoding="utf-8").read()
# text = text.lower()

# zle_znaki = ".,!?;:()-—/\\\n\t…«»"
# for znak in zle_znaki:
#     text = text.replace(znak, " ")

# slowa = text.split()
# unikalne_slowa = set(slowa)

# start_time = time.perf_counter()
# licznik = {}
# for slowo in unikalne_slowa:
#     if not slowo:
#         continue
#     if len(slowo) <= 4:
#         continue
#     licznik[slowo] = text.count(slowo)
# stop_time = time.perf_counter()

# licznik = dict(sorted(licznik.items(), key=lambda kv: kv[1]))
# print(licznik)


# print(licznik["tadeusz"])
# print(licznik["tadeuszu"])

# print(stop_time - start_time)


# rozwiązanie 3
# import time
# from collections import Counter

# text = open("pan-tadeusz.txt", "r", encoding="utf-8").read()
# text = text.lower()

# zle_znaki = ".,!?;:()-—/\\\n\t…«»"
# for znak in zle_znaki:
#     text = text.replace(znak, " ")

# slowa = text.split()

# start_time = time.perf_counter()
# licznik = Counter(slowa)
# stop_time = time.perf_counter()

# licznik = dict(sorted(licznik.items(), key=lambda kv: kv[1]))
# print(licznik)

# print(stop_time - start_time)


# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(filter(lambda x: x % 2 == 0, lista)))

