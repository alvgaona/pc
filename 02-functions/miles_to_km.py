"""
Escribir un programa de Python que convierta
millas a kilómetros. Se debe imprimir los siguientes mensajes:
    1. Bienvenido <nombre>
    2. Ingrese millas a convertir:
    3. La conversión resulta: <resultado> km
"""


def miles_to_km(miles):
    """
    Calcula millas a kilometros
    """
    return miles * 1.6


def main():
    miles = input("Ingrese las millas a convertir: ")
    km = miles_to_km(float(miles))
    print(f"La conversión resulta: {km} km.")


if __name__ == '__main__':
    main()
