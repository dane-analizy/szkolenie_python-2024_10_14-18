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

# rok_urodzenia = input("Podaj rok w którym się urodziłeś/łaś: ")
# rok_urodzenia_liczba = int(rok_urodzenia)  # rzutowanie typów, inne typy: str(), float()
# print(f"Masz {2024 - rok_urodzenia_liczba} lat")

# print(f"Masz {2024 - int(rok_urodzenia)} lat")


### ZADANIE 3

# Napisz program, który pobierze od użytkownika masę (w kg) i wzrost (w cm),
# a następnie policzy BMI i wypisze wynik na konsolę.

# definicja BMI: https://pl.wikipedia.org/wiki/Wska%C5%BAnik_masy_cia%C5%82a
# BMI = masa / wzrost^2
# masa w kg
# wzrost w m

# potęgowanie w Pythonie - a do potęgi b -> a ** b
# wzrost ** 2


# masa = input("Podaj swoją masę w kg: ")
# masa = float(masa)

# wzrost = input("Podaj swój wzrost w cm: ")
# wzrost = float(wzrost)
# wzrost = wzrost / 100

# bmi = masa / wzrost**2

# # bmi = round(bmi, 2)

# print(f"Twoje BMI wynosi: {bmi:.2f}")
# print(f"A zmienna {bmi=}")


## WARUNKI - if

# operatory matematyczne

# +
# -
# *
# /
# **

# x = 10
# y = 3
# print(x // y) # ile razy y całkowicie mieści się w x
# print(x % y) # reszta z dzielenia

# czy liczba jest parzysta: jeżeli x % 2 jest równa 0 to liczba jest parzysta
# print(1 % 2)
# print(2 % 2)
# print(3 % 2)
# print(4 % 2)


# jeżeli x % 2 jest równa 0 to liczba jest parzysta
# if x % 2 equals 0 then even else odd

# x = 3
# if x % 2 == 0:
#     print("parzysta")
#     print("parzysta po raz 2")
#     print("parzysta po raz 3")
# else:
#     print("nieparzysta")
#     print("nieparzysta po raz 2")
#     print("nieparzysta po raz 3")
# print("po ifie")



#### ZADANIE 4

# Niech użytkownik poda jakąś liczbę. W odpowiedzi wyświetlamy tę liczbę i informację czy liczba
# jest dodatnia, ujemna czy też jest zerem.

