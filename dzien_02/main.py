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
