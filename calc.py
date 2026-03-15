class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def divide(a, b):
        return a / b

print(Calculator.add(1,2))
print(Calculator.divide(10,0))

# dodać pozostałe metody do kalkulatora
# zabezpieczyć dzielenie przez zero