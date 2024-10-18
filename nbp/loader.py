## Aplikacja, która kopiuje z API NBP kursy walut do bazy danych
# 1. Wczytanie konfiguracji
# 2. Utworzenie tabelki na kursy w bazie - jeśli nie istnieje
# """
# CREATE TABLE IF NOT EXISTS waluty (
#     data VARCHAR(12),
#     waluta VARCHAR(4),
#     kurs FLOAT
# )
# """
# 3. Pobranie danych z NBP
# 4. Zapisanie danych do tabeli


from sqlalchemy import text
from utils.db import connect_db
from utils.nbp import get_nbp_rates
from utils.utils import load_config

# CONFIG_FILE = "db_config.yaml"
CONFIG_FILE = "db_config_lukasz.yaml"

lista_lat = [2024]
lista_miesiecy = [9]
lista_walut = ["EUR", "USD"]


def main():
    # 1. wczytanie konfiguracji
    config = load_config(CONFIG_FILE)

    print("Konfiguracja wczytana")

    # 3. pobranie danych z nbp
    pelne_notowania = []
    for r in lista_lat:
        for m in lista_miesiecy:
            for d in range(1, 32):
                notowanie_z_dnia = get_nbp_rates(
                    waluty=lista_walut, rok=r, miesiac=m, dzien=d
                )
                if notowanie_z_dnia:
                    for notowanie in notowanie_z_dnia:
                        pelne_notowania.append(notowanie)
    print("Dane pobrane")

    # tutaj będzie zapis do bazy danych
    # 2. utworzenie tabel
    engine = connect_db(config)
    conn = engine.connect()
    conn.execute(
        text("""CREATE TABLE IF NOT EXISTS waluty (
                data VARCHAR(12),
                waluta VARCHAR(4),
                kurs FLOAT
                )""")
    )
    conn.commit()
    print("Tabela utworzona")

    # 4. zapis danych do bazy
    conn.execute(
        text("INSERT INTO waluty (data, waluta, kurs) VALUES (:data, :waluta, :kurs)"),
        pelne_notowania,
    )
    conn.commit()
    print("Dane zapisane do bazy")

    conn.close()


if __name__ == "__main__":
    main()
