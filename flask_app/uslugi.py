# Flask -> zainstaluj pakiet Flask: pip install Flask
from flask import Flask, request

app = Flask("nazwa_aplikacja_uslugi")


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


if __name__ == "__main__":
    app.run(debug=True)


### ZADANIE
# Zrób endpoint "mnozenie" - na postawie endpointa "dodaj"
