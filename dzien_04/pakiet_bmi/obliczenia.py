def check_parameter(p):
    if not isinstance(p, (int, float)):
        return False
    if p < 0:
        return False
    return True


def bmi(waga_kg, wzrost_m):
    # sprawdzamy czy waga jest ok
    if not check_parameter(waga_kg):
        print("Waga musi być liczbą dodatnią!")
        return None

    # sprawdzamy czy wzrost jest ok
    if not check_parameter(wzrost_m):
        print("Wzrost musi być liczbą dodatnią!")
        return None

    # możemy liczyć wynik
    wynik = round(waga_kg / (wzrost_m**2), 2)
    return wynik
