# świetny tutorial https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

# Flask -> zainstaluj pakiet Flask: pip install Flask
from flask import Flask, render_template

app = Flask("nazwa_aplikacja_jeden")


@app.route("/")
def hp():
    return render_template("test.html")


@app.route("/produkt")
def produkt():
    return render_template("produkt.html")


@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")


@app.route("/onas")
def onas():
    return render_template("onas.html")


if __name__ == "__main__":
    app.run(debug=True)


#### ZADANIE

# dodaj nową templatkę i stronę - np. "o nas"
