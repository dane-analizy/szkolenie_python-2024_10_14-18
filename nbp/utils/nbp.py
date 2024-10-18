import time

import requests


def get_nbp_rates(waluty=["CHF", "EUR", "USD"], rok=2024, miesiac=10, dzien=17):
    """Funkcja pobiera notowania wskazanych walut na daną datę z API NBP.

    Args:
        waluty  - lista kodów walut do pobrania
        rok     - rok

    Returns:
        lista słowników z notowaniem
    """
    time.sleep(0.1)
    url = f"https://api.nbp.pl/api/exchangerates/tables/A/{rok:04d}-{miesiac:02d}-{dzien:02d}/?format=json"
    res = requests.get(url)
    if res.status_code != 200:
        return []

    notowania = res.json()[0]

    wynik = []
    for waluta in notowania["rates"]:
        if waluta["code"] in waluty:
            wynik.append(
                {
                    "waluta": waluta["code"],
                    "kurs": waluta["mid"],
                    "data": notowania["effectiveDate"],
                }
            )

    return wynik
