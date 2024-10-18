# Flask -> zainstaluj pakiet Flask: pip install Flask
from flask import Flask, render_template, request

app = Flask("nazwa_aplikacja_uslugi", template_folder="templates_uslugi")


@app.route("/dodaj/<b>/<a>")
def dodaj(a, b):
    # print(f"{a=}, {b=}")
    a = float(a)
    b = float(b)
    return {"suma": a + b, "a": a, "b": b}


@app.route("/mnozenie/<a>/<b>")
def mnozenie(a, b):
    # print(f"{a=}, {b=}")
    a = float(a)
    b = float(b)
    return {"iloczyn": a * b, "a": a, "b": b}


@app.route("/witaj")
@app.route("/witaj/<imie>")
def witaj(imie=None):
    if imie:
        return f"Witaj {imie}"
    else:
        return "Witaj człowieku"


@app.route("/params")
def params():
    return request.args


@app.route("/zmienne")
def zmienne():
    return render_template("zmienne.html", imie="Łukasz", nazwisko="Kowalski")


@app.route("/tabelka")
def tabelka():
    lista_osob = [
        {"imie": "Jan", "nazwisko": "Nowak", "wzrost": 190},
        {"imie": "Krzysztof", "nazwisko": "Kowalski", "waga": 100},
        {"imie": "Mirek", "nazwisko": "Iksiński", "wiek": 50},
    ]
    return render_template("tabelka.html", osoby=lista_osob)


if __name__ == "__main__":
    app.run(debug=True)


### ZADANIE
# Zrób endpoint "mnozenie" - na postawie endpointa "dodaj"
