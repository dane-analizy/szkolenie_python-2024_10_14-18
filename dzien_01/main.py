# komentarz - od znaku # do końca linii

# wypisanie tekstu na ekranie
# print("jakiś tekst")
# print("inny tekst")


# w Java byłoby to tak:
# class Napis {
#     public static void main(String[] arg) {
#         System.out.println("jakiś tekst");
#     }
# }


# standard PEP 8
# https://analityk.edu.pl/jak-pisac-kod-w-python-aby-byl-czytelny-pep8/


### ZMIENNE
# zmienna = 123
# print("zmienna") # wyświetla napis "zmienna"
# print(zmienna) # wyświetla wartość zmiennej o nazwie zmienna
# print(type(zmienna)) # wyświetla typ zmiennej

# zmienna = "Ala ma kota"
# print(zmienna)
# print(type(zmienna))

# zmienna = 3.1415926
# print(zmienna)
# print(type(zmienna))

# zmienna_int = 1
# zmienna_float = 2.3
# zmienna_str = "abc"

# print(zmienna_int + zmienna_float) # to się uda
# print(zmienna_int + zmienna_str) # to się nei uda

# print(zmienna_int * 5)
# print(zmienna_float * 5)
# print(zmienna_str * 5) # ciekawostka - można mnożyć stringi


## wypisanie różnych zmiennych i tekstów razem

# miasto = "Warszawa"
# temperatura = 10
# print(miasto, "jest teraz", temperatura, "stopni")


# tresc_od_uzytkownika = input("Podaj mi jakiś tekst: ")
# print(tresc_od_uzytkownika)


### ZADANIE 1

# Napisz program, który pobierze od użytkownika imię i nazwisko,
# a potem wypisze w konsoli pozdrowienie "Witaj IMIĘ NAZWISKO!"

# imie = input("Podaj imię: ")
# nazwisko = input("Podaj nazwisko: ")
# print("Witaj", imie, nazwisko, "!")

# # f-string - sposób na sklejanie tekstu ze zmiennymi
# print(f"Witaj {nazwisko} {imie}!")

# # formatowanie przez .format()
# print("Witaj {} {}!".format(imie, nazwisko))


### ZADANIE 2

# Pobierz od użytkownika jego rok urodzenia i w odpowiedzi wypisz ile ma lat.

rok_urodzenia = input()
print("masz", 2024 - rok_urodzenia, "lat")