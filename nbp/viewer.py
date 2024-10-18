# 1. wczytać konfigurację
# 2. połączyć się do bazy
# 3. użyć nowej funkcji - przyjmuje walutę i zakres dat - żeby z bazy uzyskać listę wyników
# 4. odłączyć się od bazy
# 5. wyświetlić listę wyników - np. przez for


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


def main():
    config = load_config(CONFIG_FILE)
    print("Konfiguracja wczytana")
    notowania = get_rates(config, "EUR", "2024-02-01", "2024-03-31")

    for notowanie in notowania:
        napis = ""
        for k, v in notowanie.items():
            napis = napis + f"{k} = {v} "
        print(napis)


if __name__ == "__main__":
    main()
