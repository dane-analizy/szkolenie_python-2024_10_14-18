##### json i yaml - trzymanie konfiguracji


# json

# zapisanie słownika do pliku JSON
# import json

# d = {
#     "login": "tajnylogin",
#     "haslo": "tajnehaslo",
#     "pin": 1234,
#     "nazwa_tabeli": "tabela_z_danymi",
# }

# with open("konfiguracja.json", "w", encoding="utf-8") as f:
#     json.dump(d, f)


# import json

# l = [1, 4, "abd"]
# with open("konfiguracja_2.json", "w", encoding="utf-8") as f:
#     json.dump(l, f)


# wczytanie danych z pliku JSON
# import json

# with open("konfiguracja.json", "r", encoding="utf-8") as f:
#     dane = json.load(f)

# print(dane)
# print(type(dane))

# import json

# with open("konfiguracja_2.json", "r", encoding="utf-8") as f:
#     dane = json.load(f)
#     print(type(dane))
#     print(dane)


# import json

# with open("konfiguracja_3.json", "r", encoding="utf-8") as f:
#     dane = json.load(f)

# print(type(dane))
# for rekord in dane:
#     print(rekord)
#     print(type(rekord))
#     print(rekord['login'])


# dane[(2024, 10, 17)] = "dzisiaj"  # <- to spowoduje błąd przy zapisie

# with open("konfiguracja_3_backup.json", "w", encoding="utf-8") as f:
#     json.dump(dane, f, indent=2, sort_keys=True)


# print("działam")

# from pathlib import Path

# current_dir = Path().cwd() # <- katalog w którym jesteśmy
# print(current_dir.absolute())


# YAML
# potrzeby pakiet PyYAML
# pip install pyyaml


# przepisanie jsona na yamla
# import json
# import yaml

# with open("konfiguracja_3.json", "r", encoding="utf-8") as f:
#     dane = json.load(f)

# with open("konfiguracja_3.yaml", "w", encoding="utf-8") as f:
#     yaml.dump(dane, f)

# import yaml

# with open("konfiguracja_3.yaml", "r", encoding="utf-8") as f:
#     dane = yaml.safe_load(f)

# print(dane)


##### funkcje

# nazwa_pliku = "zawodnicy.csv"
# sep = ";"
# enc = "utf-8"

# dane = [linia.strip() for linia in open(nazwa_pliku, "r", encoding=enc).readlines()]
# dane = [rekord.split(sep) for rekord in dane]
# dane = [[r[0], r[1], float(r[2]), float(r[3])] for r in dane]


# def funkcja():
#     print("jestem w funkcji")
#     print("nadal jestem w funkcji")
#     print("i już kończę")

# print("jestem poza funkcją")
# funkcja()
# print("jestem poza funkcją")
# funkcja()
# print("jestem poza funkcją")


# zasięg zmiennych
# a = 5
# print("przed definicją funkcji", a)

# def wypisz_a():
#     a = 10
#     print("w funkcji:", a)

# def wypisz_a2():
#     print("druga funkcja", a)

# print("poza funkcja po definicji", a)
# wypisz_a()
# print("poza funkcja", a)
# wypisz_a2()


# argumenty funkcji
# a=10
# b=50
# c=100
# def dodaj(a, b):
#     print(f"Suma {a} + {b} = {a+b}, a {c=}")

# dodaj(2,4)


#  zwracanie wartości

# def odejmij(a, b):
#     wynik = a - b
#     print(f"{a} - {b} = {wynik}")
#     return wynik

# w = odejmij(10, 7)
# print("wynik uzyskany z funkcji", w)


#### ZADANIE 29

# Przygotuj funkcję, która wyliczy na podstawie wagi i wzrostu (parametry) BMI z dokładnością do 2 miejsc
# po przecinku.

# BMI = waga (kg) / wzrost**2 (m)


# isinstance(obj, (klasa2, klasa2))


# def bmi(waga_kg, wzrost_m):
#     if not isinstance(waga_kg, (int, float)):
#         print("Waga musi być liczbą!")
#         return None

#     if not isinstance(wzrost_m, (int, float)):
#         print("Wzrost musi być liczbą!")
#         return None

#     wynik = round(waga_kg / (wzrost_m**2), 2)
#     return wynik


# print(bmi(90, 1.80))
# print(bmi("alamakota", 1.80))


#### ZADANIE 30

# Do przygotowanej funkcji w poprzednim zadaniu dodaj sprawdzanie czy argumenty są odpowiednich
# typów (isinstance) oraz czy ich wartości są sensowne (dodatnie). Jeśli typy albo wartości są złe
# wypisz odpowiedni komunikat i zwróć None


# def bmi(waga_kg, wzrost_m):
#     # sprawdzamy czy waga jest ok
#     if not isinstance(waga_kg, (int, float)):
#         print("Waga musi być liczbą!")
#         return None
#     if waga_kg < 0:
#         print("Waga musi być dodatnia!")
#         return None

#     # sprawdzamy czy wzrost jest ok
#     if not isinstance(wzrost_m, (int, float)):
#         print("Wzrost musi być liczbą!")
#         return None
#     if wzrost_m < 0:
#         print("Wzrost musi być dodatni!")
#         return None

#     # możemy liczyć wynik
#     wynik = round(waga_kg / (wzrost_m**2), 2)
#     return wynik


# print(bmi(90, 1.80))
# print(bmi("alamakota", 1.80))
# print(bmi(78, -1.80))


### DRY - Don't Repeat Yourself

# def check_parameter(p):
#     if not isinstance(p, (int, float)):
#         return False
#     if p < 0:
#         return False
#     return True


# def bmi(waga_kg, wzrost_m):
#     # sprawdzamy czy waga jest ok
#     if not check_parameter(waga_kg):
#         print("Waga musi być liczbą dodatnią!")
#         return None

#     # sprawdzamy czy wzrost jest ok
#     if not check_parameter(wzrost_m):
#         print("Wzrost musi być liczbą dodatnią!")
#         return None

#     # możemy liczyć wynik
#     wynik = round(waga_kg / (wzrost_m**2), 2)
#     return wynik


# print(bmi(90, 1.80))
# print(bmi("alamakota", 1.80))
# print(bmi(78, -1.80))


# moduły funkcji

# import konkretnej funkcji z modułu
# from modul_bmi import bmi
# print(bmi(80, 1.80))

# import wszystkiego z modułu
# import modul_bmi
# print(modul_bmi.bmi(80, 1.80))


# argumenty domyślne

# def funkcja(a=10, b=20, c=50):
#     print(f"{a=}\n{b=}\n{c=}")

# funkcja(1,2,6)
# funkcja()


#### ZADANIE 31

# Napisz funkcję która zwróci pod postacią listy wierszy zawartość pliku,
# którego nazwę przekażemy przez pierwszy argument funkcji. Plik ma być otwarty
# z kodowaniem podanym jako drugi argument funkcji. Jeśli kodowanie nie zostanie
# podane ma przyjąć "utf-8".
# Funkcję tą umieść w module "plik.py" i w ramach main.py z niej skorzystaj.


# rozwiązanie -> w pliku "plik.py"
# from plik import load_file, split_lines

# text = load_file("zawodnicy.csv")
# print(text)



#### ZADANIE 32

# Do modułu "plik" dodaj funkcję split_lines(), która rozbije listę linii z pliku na listę krotek
# według podanego separatora.

# rozwiązanie w pliku plik.py

# from plik import load_file, split_lines

# text = load_file("zawodnicy.csv")
# text_splited = split_lines(text, ";")
# print(text_splited)







# wyjątki

# api - czytanie z usług sieciowych

# pytania na juniora
# pytania na juniora
