wersja_modulu = "Moduł Plik, v0.1"


def load_file(file_name, enc="utf-8"):
    file = [line.strip("\n") for line in open(file_name, "r", encoding=enc).readlines()]
    return file


def split_lines(lista, separator=";"):
    return [tuple(linia.split(separator)) for linia in lista]


def clear_data(lista):
    return [(r[0], r[1], float(r[2]) / 100, float(r[3])) for r in lista]
