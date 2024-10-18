# Flask -> zainstaluj pakiet Flask: pip install Flask
from flask import Flask

app = Flask("nazwa_aplikacja_uslugi")


@app.route("/dodaj/<b>/<a>")
def dodaj(a, b):
    # print(f"{a=}, {b=}")
    a = float(a)
    b = float(b)
    return {"suma": a + b, "a": a, "b": b}


if __name__ == "__main__":
    app.run(debug=True)


### ZADNAIE
# Zrób endpoint "mnozenie" - na postawie endpointa "dodaj"