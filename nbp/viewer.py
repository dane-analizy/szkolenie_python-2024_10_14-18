# 1. wczytać konfigurację
# 2. połączyć się do bazy
# 3. użyć nowej funkcji - przyjmuje walutę i zakres dat - żeby z bazy uzyskać listę wyników
# 4. odłączyć się od bazy
# 5. wyświetlić listę wyników - np. przez for


def get_rates(waluta, data_od, data_do):
    ...
    res = conn.execute(
        text("""
    SELECT data, waluta, kurs
    FROM waluty
    WHERE
    waluta = :waluta
    AND data >= :data_od
    AND data <= :data_do
    """),
        waluta=waluta,
        data_od=data_od,
        data_do=data_do,
    )
