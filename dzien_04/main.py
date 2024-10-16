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


### pakiety -> zobacz katalog pakiet_bmi, zwróć uwagę na plik __init__.py !

# from pakiet_bmi.obliczenia import bmi
# from pakiet_bmi.plik import clear_data, load_file, split_lines


# def wczytaj_zawodnikow(nazwa_pliku):
#     zawartosc_pliku = load_file(nazwa_pliku)
#     dane = split_lines(zawartosc_pliku)
#     dane_oczyszczone = clear_data(dane)
#     return dane_oczyszczone


# zawodnicy = wczytaj_zawodnikow("zawodnicy.csv")
# for zawodnik in zawodnicy:
#     bmi_zawodnika = bmi(zawodnik[3], zawodnik[2])
#     print(f"{zawodnik[0]} {zawodnik[1]} ma BMI = {bmi_zawodnika}")

# from pakiet_bmi import test
# print(__name__)


# from pakiet_bmi.test import funkcja_smiec
# print(__name__)
# funkcja_smiec()

# from pakiet_bmi.test import funkcja_smiec


# def main():
#     funkcja_smiec()


# if __name__ == "__main__":
#     print("Uruchomiłeś plik main.py")
#     main()


# wyjątki

# a = 10
# b = 0

# print(a/b)
# print("przed trajem")

# try:
#     print(a/b)
# except:
#     print("nie udało się")

# print("program idzie dalej")


#### ZADANIE 33

# Wyświetl wynik dzielenia jedynki przez kolejne liczby z zakresu od -10 do 10. Obsłuż wyjątek

# lista = [-2, -1, 0, 1, 2, "ala ma kota"]
# for i in lista:
#     print("i", i)
#     try:
#         wynik = 1/i
#         print(wynik)
#     except ZeroDivisionError:
#         print("nie dziel przez zero")
#     except TypeError:
#         print(f"Ale do mnie to nie tak! Tak nie! Nie umiem dzielić 1 przez {i}")
#     except Exception as e:
#         print("nie udało się")
#         print(e, type(e))

#     print()

# raise ZeroDivisionError


# open("wgwgwgwg")

#### ZADANIE 34

# W module plik, w funkcji load_file() zabezpiecz się na przypadek kiedy plik nie istnieje, czyli
# przechwyć wyjątek o typie FileNotFoundError
# Jeśli zajdzie wyjątek - funkcja powinna zwrócić pustą listę.

# rozwiązanie w pliku plik.py


# pełna konstukcja dla try..except:

# try:
#        # Some Code....
# except:
#        # optional block
#        # Handling of exception (if required)
# else:
#        # execute if no exception
# finally:
#       # Some code .....(always executed)


# api - czytanie z usług sieciowych

# https://httpbin.org/
# https://it-tools.tech/

# pakiet - requests - do zaintalowania
# pip install requests

# import requests
# try:
#     response = requests.get("https://onetggeheh.pl")
# except requests.exceptions.ConnectionError:
#     print("Connection error")
# except Exception as e:
#     print(type(e))

# import requests

# response = requests.get("https://onet.pl/dupa")
# print(response)

# response = requests.get("https://onet.pl/")
# print(response)


# import requests

# response = requests.get("https://httpbin.org/get")
# response = requests.get("https://onet.pl")

# if response.status_code == 200:
#     print("Udało się pobrać treść")

# print(response.content)
# print(response.text)
# dane = response.json()
# print(type(dane))


# import requests

# url = "https://api.nbp.pl/api/exchangerates/tables/A/2024-10-17/?format=json"
# res = requests.get(url)
# notowania = res.json()[0]
# # print(notowania)

# print("data notowania:", notowania["effectiveDate"])
# for waluta in notowania['rates']:
#     print(waluta['code'], waluta['mid'])


#### ZADANIE 35

# Pobierz dane z https://api.nbp.pl/api/exchangerates/tables/A/2024-10-17/?format=json
# wyświetl na konsoli aktualny kurs franka (chf), euro (eur) i dolara (usd) i pole effectiveDate

# import requests

# waluty = ["CHF", "EUR", "USD"]
# url = "https://api.nbp.pl/api/exchangerates/tables/A/2024-10-17/?format=json"

# res = requests.get(url)
# notowania = res.json()[0]

# for waluta in notowania["rates"]:
#     if waluta["code"] in waluty:
#         print(waluta["code"], waluta["mid"], notowania["effectiveDate"])


# rok = 2024
# miesiac = 10
# dzien = 17
# url = f"https://api.nbp.pl/api/exchangerates/tables/A/{rok:04d}-{miesiac:02d}-{dzien:02d}/?format=json"
# print(url)


#### ZADANIE 36

# Korzystają z kodu powstałego w zadaniu 35 przygotuj funkcję, która pobierze kursy
# podanych jako argument walut z podanej jako argument (oddzielnie rok, miesiac i dzien) daty.


# import requests


# def get_nbp_rates(waluty=["CHF", "EUR", "USD"], rok=2024, miesiac=10, dzien=17):
#     url = f"https://api.nbp.pl/api/exchangerates/tables/A/{rok:04d}-{miesiac:02d}-{dzien:02d}/?format=json"

#     res = requests.get(url)

#     if res.status_code != 200:
#         return None

#     notowania = res.json()[0]

#     for waluta in notowania["rates"]:
#         if waluta["code"] in waluty:
#             print(waluta["code"], waluta["mid"], notowania["effectiveDate"])


# get_nbp_rates(waluty=["GBP", "JPY"], rok=2023, miesiac=1, dzien=17)


# rozwijamy nasze rozwiązanie

# import requests
# import time


# def get_nbp_rates(waluty=["CHF", "EUR", "USD"], rok=2024, miesiac=10, dzien=17):
#     time.sleep(0.1)
#     url = f"https://api.nbp.pl/api/exchangerates/tables/A/{rok:04d}-{miesiac:02d}-{dzien:02d}/?format=json"
#     res = requests.get(url)
#     if res.status_code != 200:
#         return []

#     notowania = res.json()[0]

#     wynik = []
#     for waluta in notowania["rates"]:
#         if waluta["code"] in waluty:
#             wynik.append(
#                 {
#                     "kod":waluta["code"],
#                     "kurs":waluta["mid"],
#                     "data": notowania["effectiveDate"]
#                 }
#             )

#     return wynik


# w = get_nbp_rates(waluty=["GBP", "JPY"], rok=2023, miesiac=1, dzien=17)
# print(w)


##### ZADANIE 37

# Używając funkcji get_nbp_rates() pobierz notowania dla EUR i USD z całego czerwca,
# lipca i sierpnia 2024. Niech wynik będzie listą słowników.

# wykorzystujemy funkcję z poprzedniego zadania


# import json

# pelne_notowania = []
# for m in [6, 7, 8]:
#     for d in range(1, 32):
#         notowanie_z_dnia = get_nbp_rates(waluty=["EUR", "USD"], rok=2024, miesiac=m, dzien=d)
#         if notowanie_z_dnia:
#             for notowanie in notowanie_z_dnia:
#                 pelne_notowania.append(notowanie)


# with open("notowania.json", "w", encoding="utf-8") as f:
#     json.dump(pelne_notowania, f)


### konfiguracja w pliku
# import yaml

# CONFIG_FILE = "config_test.yaml"

# with open(CONFIG_FILE, "r", encoding="utf-8") as f:
#     config = yaml.safe_load(f)

# print(config)

# połącz_do_bazy(config)
# config['db_name']
# config['db_user']


# pytania na juniora
# tekst = """11111
# 222222
#                     333333
# 4444
# """

# print(tekst)

# del tekst

# print(tekst)


# a = 2
# b = 5

# c = a
# a = b
# b = c

# a, b = b, a


print("gwgwg")