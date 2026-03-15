class Calculator:

    @staticmethod
    def dodawanie(a, b):
        return a + b

    @staticmethod
    def odejmowanie(a, b):
        return a - b

    @staticmethod
    def mnozenie(a, b):
        return a * b

    @staticmethod
    def dzielenie(a, b):
        if b == 0:
            return False
        return a / b


# poproś o liczby
liczba1 = float(input("Podaj pierwszą liczbę: "))

liczba2 = float(input("Podaj drugą liczbę: "))

print(f"Podałeś dwie liczby: \n {liczba1} \n oraz \n {liczba2}")

# sprawdz czy druga liczba to nie 0
if liczba2 == 0:
    print("Uwaga: podałeś drugą liczbę 0, więc dzielenie nie będzie możliwe.")
    odpowiedz = input("Czy chcesz jeszcze raz podać wartość drugiej liczby? T/N: ")

    if odpowiedz == "T":
        liczba2 = float(input("Popraw wartość drugiej liczby: "))
    elif odpowiedz == "N":
        print("Pozostaje wartość 0.")
    else:
        print("Niepoprawna odpowiedź. Pozostaje wartość 0.")

# Wyniki operacji
print(f"Wyniki przeprowadzonych działań na twoich liczbach:")
print(f"Wynik dodawania: {Calculator.dodawanie(liczba1, liczba2)}")
print(f"Wynik odejmowania: {Calculator.odejmowanie(liczba1, liczba2)}")
print(f"Wynik mnożenia: {Calculator.mnozenie(liczba1, liczba2)}")

# dzielenie jeśli druga to nie 0
if liczba2 != 0:
    print(f"Wynik dzielenia: {Calculator.dzielenie(liczba1, liczba2)}")
else:
    print("Błąd: nie można dzielić przez zero.")