# json i yaml - trzymanie konfiguracji


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


# YAML
# potrzeby pakiet PyYAML
# pip install pyyaml

print("działam")

from pathlib import Path

current_dir = Path().cwd()
print(current_dir.absolute())
# funkcje

# wyjątki

# api - czytanie z usług sieciowych

# pytania na juniora
