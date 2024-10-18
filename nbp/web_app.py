from flask import Flask, redirect, render_template
from sqlalchemy import text
from utils.db import connect_db
from utils.utils import load_config

# CONFIG_FILE = "db_config.yaml"
CONFIG_FILE = "db_config_lukasz.yaml"


def get_rates(config, waluta, data_od, data_do):
    engine = connect_db(config)
    conn = engine.connect()
    res = conn.execute(
        text("""
    SELECT
        data, waluta, kurs
    FROM
        waluty
    WHERE
        waluta = :waluta
        AND data >= :data_od
        AND data <= :data_do
    ORDER BY data ASC
    """),
        {"waluta": waluta, "data_od": data_od, "data_do": data_do},
    )
    conn.close()

    columns = list(res.keys())
    notowania = [{columns[0]: r[0], columns[1]: r[1], columns[2]: r[2]} for r in res]
    return notowania


config = load_config(CONFIG_FILE)

app = Flask("waluty")


@app.route("/")
def hp():
    return redirect("/kurs/EUR")


@app.route("/kurs/<waluta>")
@app.route("/kurs/<waluta>/<data_od>/<data_do>")
def kurs(waluta, data_od=None, data_do=None):
    if data_od and data_do:
        kursy = get_rates(config, waluta, data_od, data_do)
    else:
        kursy = get_rates(config, waluta, "2024-09-01", "2024-12-31")

    return render_template(
        "kurs.html",
        parametry={
            "waluta": waluta,
            "data_od": data_od,
            "data_do": data_do,
            "notowanie": kursy,
        },
    )


if __name__ == "__main__":
    app.run()
