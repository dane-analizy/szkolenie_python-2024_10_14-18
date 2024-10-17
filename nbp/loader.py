from utils.nbp import get_nbp_rates

lista_lat = [2024]
lista_miesiecy = [6, 7, 8]
lista_walut = ["EUR", "USD"]


def main():
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

    # tutaj będzie zapis do bazy danych


if __name__ == "__main__":
    main()
