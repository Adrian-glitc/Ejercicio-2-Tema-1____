class CalculadoraInteresCompuesto:
    def __init__(self, capital_inicial):
        self.capital_inicial = capital_inicial

    def leer_tasa_interes(self):
        while True:
            try:
                tasa_interes = float(input("Introduce la tasa de interés anual (entre 1% y 10%): "))
                if 1 <= tasa_interes <= 10:
                    self.tasa_interes = tasa_interes / 100  # Convertir a decimal
                    break
                else:
                    print("Por favor, introduce un valor entre 1 y 10.")
            except ValueError:
                print("Entrada no válida. Por favor, introduce un número.")

    def leer_anios(self):
        while True:
            try:
                anios = int(input("Introduce el número de años: "))
                if anios > 0:
                    self.anios = anios
                    break
                else:
                    print("Por favor, introduce un número positivo.")
            except ValueError:
                print("Entrada no válida. Por favor, introduce un número entero.")

    def calcular_capital_final(self):
        return self.capital_inicial * ((1 + self.tasa_interes) ** self.anios)

    def mostrar_resultado(self):
        capital_final = self.calcular_capital_final()
        print(f"El capital final después de {self.anios} años es: {capital_final:.2f}")
        
        
from Palabras import CalculadoraInteresCompuesto
# Uso de la clase
if __name__ == "__main__":
    calculadora = CalculadoraInteresCompuesto(capital_inicial=1000)
    calculadora.leer_tasa_interes()
    calculadora.leer_anios()
    calculadora.mostrar_resultado()
    
