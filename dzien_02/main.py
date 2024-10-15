# jak zakończyć pętlę przed czasem?

# for i in range(100):
#     print(i**2)
#     if i**2 > 8000:
#         break
# print(f"Po zakończeniu pętli {i=}")


# jak ominąć iterację?
# for i in range(-10, 10):
#     print(i)
#     if i == 0:
#         print("przechodzę dalej")
#         continue
#     print("dzielenie", 1/i)


#### ZADANIE 10

# Przejdź w pętli po liczbach od 1 do 100 i wydrukuj tylko nieparzyste. Użyj konstrukcji z continue.

# for i in range(100):
#     if i % 2 == 0:
#         continue
#     print(i)


#### ZADANIE 11

# Napisz kod, który w nieskończoność będzie pytał użytkownika o kolejne słowa.
# To co wpisze użytkownik - wypisujemy na ekranie.
# Ale jeśli użytkownika wpisze słowo "stop" - kończymy program, dziękując za współpracę.


# while True:
#     slowo = input("Podaj słowo")
#     print(slowo)
#     if slowo == "stop":
#         break

# print("Dziękuję za współpracę")


# jak sprawdzić czy pętla przeszła wszystkie iteracje?

# for i in range(10):
#     print(i)
#     if i > 50: # porównaj z wersją "if i > 5"
#         break
# else:
#     print("Else po for")

# print("Całkiem poza for")


#### STRINGI - ciągi tekstowe

# napis = "   Ala ma kota     "
# print("upper", napis.upper())
# print("lower", napis.lower())
# print("title", napis.title())
# print("strip", napis.strip())
# print("len", len(napis))
# print("len po strip", len(napis.strip()))


#### ZADANIE 11b

# Napisz kod, który w nieskończoność będzie pytał użytkownika o kolejne słowa.
# To co wpisze użytkownik - wypisujemy na ekranie, tak że wszystkie litery są powiększone.
# Ale jeśli użytkownika wpisze słowo "stop" (nie ważne jakiej wielkości liter użyje oraz czy będą białe
# znaki przed lub po słowie) - kończymy program, dziękując za współpracę.


# while True:
#     slowo = input("Podaj tekst: ")
#     print(f"Wpisałeś: '{slowo.upper()}'")
#     if slowo.strip().lower() == "stop":
#         break

# print("Dziękuję za współpracę")


# zamiana znaków w stringu

# napis = "Ala ma kotA"
# print(napis)
# napis_zmieniony = napis.replace("a", "*")
# napis_zmieniony = napis_zmieniony.replace("A", "*")
# print(napis_zmieniony)

# usunięcie znaków
# napis = "Ala ma kotA, Ale kot nie ma Ali"
# print(napis)
# napis_zmieniony = napis.replace("a", "")
# print(napis_zmieniony)

# napis_zmieniony_2 = napis.replace("Al", "BAL")
# print(napis_zmieniony_2)


### ZADANIE 12

# Napisz program, który przyjmie od użytkownika ciąg tekstowy, następnie usunie z niego znaki: ,.?!
# a następnie powiększony do dużych liter wyświetli w konsoli.

# wersja 1

# tekst = input("Podaj jakiś tekst: ")
# tekst = tekst.replace(",", "")
# tekst = tekst.replace(".", "")
# tekst = tekst.replace("?", "")
# tekst = tekst.replace("!", "")
# tekst = tekst.replace("@", "")
# tekst = tekst.replace("#", "")
# tekst = tekst.upper()
# print(tekst)


# wersja 2

# tekst = input("Podaj jakiś tekst: ")
# tekst = (
#     tekst
#     .replace(",", "")
#     .replace(".", "")
#     .replace("?", "")
#     .replace("!", "")
#     .upper()
#     )
# print(tekst)


# string to lista liter
# napis = "Ala ma kota"
# for znak in napis:
#     print(znak)


# wersja 3 - najbardziej optymalna

# tekst = input("Podaj jakiś tekst: ")
# zakazane_znaki = ".,?!" # <- tutaj dodaj kolejne zakazane znaki

# for zakazany_jeden_znak in zakazane_znaki:
#     tekst = tekst.replace(zakazany_jeden_znak, "")

# tekst = tekst.upper()
# print(tekst)


### czytane z pliku

# f = open("plik.txt", "r", encoding="utf-8")
# for linia in f:
#     print(linia.strip('\n'))


### ZADANIE 13

# Napisz program który wyświetli na konsoli niepuste linie z pliku tekstowego,
# którego nazwę poda użytkownik.

# nazwa_pliku = input("Podaj nazwę pliku: ")
# for linia in open(nazwa_pliku, "r", encoding="utf-8"):
#     # if len(linia) > 1:
#     # if linia.strip():
#     if len(linia.strip()):
#         print(linia.strip("\n"))


# ile razy ciąg występuje w innym ciągu
# napis = "Ala ma kotA, Ale kot nie ma Ali"
# print(napis.count("a"))

# tresc_pliku = open("plik.txt", "r", encoding="utf-8").read()
# print(tresc_pliku)
# print(len(tresc_pliku))


##### ZADANIE 14

# Napisz program, który zliczy ilość wystąpień małej lub dużej wersji ciągu podanego przez użytkownika
# w pliku, którego nazwa także podana jest przez użytkownika.


# plik = input("Podaj nazwę pliku: ")
# ciag = input("Czego szukamy? ")

# zawartosc_pliku = open(plik, "r", encoding="utf-8").read()
# ile_razy = zawartosc_pliku.lower().count(ciag.lower())
# print(f"'{ciag}' w pliku {plik} występuje {ile_razy}")


#### ZADANIE 15

# Napisz wyszukiwarkę plikową.
# Wyszukiwarka powinna odebrać od użytkownika poszukiwaną frazę oraz nazwę pliku.
# W wyniku działania wyszukiwarka powinna pokazać w której linii wystąpiła wyszukiwana fraza oraz całą linię.
# Wyszukiwarka powinna być nieczuła na wielkość liter.

# wersja 1
# plik = input("Podaj nazwę pliku: ")
# ciag = input("Czego szukamy? ")

# numer_linii = 0
# for linia in open(plik, "r", encoding="utf-8"):
#     numer_linii = numer_linii + 1
#     if linia.lower().strip().count(ciag.lower()):
#         print(f"{numer_linii:<6}: {linia.strip()}")


# enumerate - numerowanie w której iteracji pętli jesteśmy

# napis = "ala ma kota"
# # numer_znaku = 0
# for numer_iteracji, znak in enumerate(napis, start=1):
#     # numer_znaku += 1
#     # print(numer_znaku, i, znak)
#     print(numer_iteracji, znak)


# wersja 2

# plik = input("Podaj nazwę pliku: ")
# ciag = input("Czego szukamy? ")

# for numer_linii, linia in enumerate(open(plik, "r", encoding="utf-8")):
#     if linia.lower().strip().count(ciag.lower()):
#         print(f"{numer_linii:>6}: {linia.strip()}")


# jak sięgnąć do konkretnej litery w stringu?
# napis = "Ala ma kota"
# print(napis[4])  # -> sięgamy do elementu o indeksie 4 co oznacza 5 znak, bo indeksowanie jest od 0


#### ZADANIE 16

# Napisz program który będzie pobierał nazwę pliku z kodem w Pythonie.
# Program będzie wyświetlał wszystkie linie które **nie** są komentarzami i nie są puste,
# razem z numerem linii.

# plik = input("Podaj nazwę pliku: ")

# for nr, linia in enumerate(open(plik, "r", encoding="utf-8"), start=1):
#     if linia.strip() and linia[0] != "#":
#         linia_kodu = linia.strip("\n")
#         print(f"{nr:>5}: {linia_kodu}")


### Listy

# lista = [1, "a", 2.3, "abc", [1, 2], ["abc", "cde"]]
# print(lista)
# for element in lista:
#     print(element, type(element))


# dodawanie elementów do listy
# lista = list()  # synonim: lista = []
# print(lista)
# lista.append(1)
# print(lista)
# lista.append(1)
# print(lista)
# lista.insert(0, "abc")
# print(lista)

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(lista[0])
# print(lista[5])
# print(lista[1:4])
# print(lista[:3])
# print(lista[5:])
# print(lista[:])

# print(lista[1:100])
# # print(lista[100])
# print(lista[25:100])

# if lista[25:100]:
#     print("nie pusta")
# else:
#     print("pusta")

# print(len(lista))

# if len(lista) > 0:
#     print("nie pusta")
# else:
#     print("pusta")


# print(lista[2:7:3])
# print(lista[::2])

# print(lista[4:-2])

# print(lista[-1:0:-1])

# print(lista[::-1])


#### ZADANIE 17

# Napisz kod który umieści w liście 10 kolejnych potęg liczby 2 (od 0 potęgi).
# Następnie przeiteruj po tej liście i każdy z jej elementów wyświetl na konsoli w osobnej linii.

# lista =  []
# for p in range(10):
#     lista.append(2 ** p)

# for el in lista:
#     print(el)

# # to nie jest pythonic-style:
# for idx in range(len(lista)):
#     el = lista[idx]
#     print(el)

# l1 = [1, 2, 3]
# l2 = l1.copy()
# print("l1:", l1)
# print("l2:", l2)

# l1[2] = "abc"
# l2[0] = "xyz"

# print("l1:", l1)
# print("l2:", l2)

# l1 = [1, 1, 2, 3]
# l2 = [9, 8, 7, 1]
# l3 = l1 + l2
# print(l3)

# l3 = l1 - l2
# print(l3)

# lista = [1, 2, 3, 4, 5, 6, 7]
# zmienna = 50
# if zmienna in lista:
#     print(f"{zmienna} jest na liście")
# else:
#     print(f"{zmienna} nie ma na liście")


# lista = "ala ma kota"
# zmienna = "al"
# if zmienna in lista:
#     print(f"{zmienna} jest na liście")
# else:
#     print(f"{zmienna} nie ma na liście")

# lista = [1, 2, 3, [2, 3], 4, 5, 6, 7]
# zmienna = [2, 3]
# if zmienna in lista:
#     print(f"{zmienna} jest na liście")
# else:
#     print(f"{zmienna} nie ma na liście")


# if (2 in lista) and (3 in lista):
#     print("2 i 3 są na liście")


# import random

# print(random.randint(1, 100))


#### ZADANIE 18

# Stwórz dwie listy. Każda z list ma zawierać 10 liczb losowych z zakresu 1-100.
# Połącz te dwie listy do jednej i wyświetl na konsoli.

# import random

# l1 = []
# for p in range(10):
#     l1.append(random.randint(1, 100))

# l2 = []
# for p in range(10):
#     l2.append(random.randint(1, 100))

# l3 = l1 + l2
# print(l3)


#### ZADANIE 19

# Korzystając z pętli stwórz listę zawierającą elementy same będące listami.
# Każdy taki element ma zawierać numer potęgi (od 1 do 10) oraz wartość tej potęgi dla liczby 2.

# lista = []
# for p in range(1, 11):
#     lista.append([p, 2**p])

# print(lista)


# lista składana = list comprehention

# lista = []
# for i in range(10):
#     lista.append(i)


# lista = [i for i in range(10)]

# for i in range(10):
#     lista.append(i)


# l = [[p, 2**p] for p in range(10)]


##### ZADANIE 20

# Korzystając z list składanych zbuduj listę losowych 10 liczb z zakresu 100-200. Wyświetl całą listę.

# import random

# lista = [ random.randint(100, 200) for _ in range(10)]
# print(lista)

# tabliczka mnożenia

## wersja 1
# tabliczka = []
# for x in range(1, 11):
#     for y in range(1, 11):
#         tabliczka.append( [x, y, x*y] )

# print(tabliczka)

## wersja 2
# tabliczka = [ [x, y, x * y] for x in range(1, 11) for y in range(1, 11) ]
# print(tabliczka)


# rozbicie napisu na listę stringów względem separatora - tutaj jest nim ;
# napis = "kolumna1;kolumna2;kolumna3"
# print(napis.split(";"))

# linia = "Bogdan;Kowalski;170;90"
# linia_lista = linia.split(";")
# print(linia_lista)
# print(type(linia_lista[2]))


### ZADANIE 21

# Dla każdego wpisu w pliku zawodnicy.csv wyświetl na konsoli informację o:
# imieniu, nazwisku, wadze i wzroście oraz BMI (wcześniej je policz).

# BMI = waga (w kg) / wzrost (w metrach) ** 2

nazwa_pliku = "zawodnicy.csv"
zawartosc_pliku = open(nazwa_pliku, "r", encoding="utf-8").readlines()
for linia in zawartosc_pliku:
    rekord = linia.strip().split(";")
    bmi = float(rekord[3]) / (float(rekord[2]) / 100) ** 2

    if bmi <= 16:
        bmi_comment = "wygłodzenie"
    elif bmi <= 17:
        bmi_comment = "wychudzenie"
    elif bmi <= 18.5:
        bmi_comment = "niedowaga"
    elif bmi <= 25:
        bmi_comment = "pożądana masa ciała"
    elif bmi <= 30:
        bmi_comment = "nadwaga"
    elif bmi <= 35:
        bmi_comment = "otyłość I stopnia"
    elif bmi <= 40:
        bmi_comment = "otyłość II stopnia (duża)"
    else:
        bmi_comment = "otyłość III stopnia (chorobliwa)"

    print(
        f"{rekord[0]} {rekord[1]} ma {rekord[2]} cm wzrostu i {rekord[3]} kg wagi, co daje BMI = {bmi:.2f} ({bmi_comment})"
    )
