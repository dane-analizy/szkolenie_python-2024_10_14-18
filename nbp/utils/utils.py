import yaml


def load_config(nazwa_pliku):
    slownik_konfig = {}
    try:
        with open(nazwa_pliku, "r", encoding="utf-8") as file:
            slownik_konfig = yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Plik {nazwa_pliku} nie został znaleziony.")

    return slownik_konfig
