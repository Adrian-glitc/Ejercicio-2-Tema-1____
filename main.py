       
from Palabras import CalculadoraInteresCompuesto
# Uso de la clase
if __name__ == "__main__":
    calculadora = CalculadoraInteresCompuesto(capital_inicial=1000)
    calculadora.leer_tasa_interes()
    calculadora.leer_anios()
    calculadora.mostrar_resultado()
    
