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


while True:
    slowo = input("Podaj tekst: ")
    print(f"Wpisałeś: '{slowo.upper()}'")
    if slowo.strip().lower() == "stop":
        break

print("Dziękuję za współpracę")

