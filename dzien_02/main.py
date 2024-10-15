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
tekst = input("Podaj jakiś tekst: ")
zakazane_znaki = ".,?!" # <- tutaj dodaj kolejne zakazane znaki

for zakazany_jeden_znak in zakazane_znaki:
    tekst = tekst.replace(zakazany_jeden_znak, "")
    
tekst = tekst.upper()
print(tekst)

