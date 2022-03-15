"""
Escribir un programa que convierta dolares a las siguientes 3 monedas
a partir del input del usuario:
    
    Cotizaciones:
        1 USD 0.94 CHF
        1 USD 200 ARS
        1 USD 6.75 CNY
    
    User input: 
        dollars: dolares a convertir
        coin: moneda a convertir
"""


def usd_to_cny(dollars: float) -> float:
    return dollars * 6.75

def usd_to_chf(dollars: float) -> float:
    return dollars * 0.94

def usd_to_ars(dollars: float) -> float:
    return dollars * 200



def main():
    dollars = float(input("Ingrese USD: "))
    coin = input("Ingrese moneda: ")
        
    if coin == 'CNY':
        print(f"{usd_to_cny(dollars):.2f} Chinese Yuan")
    elif coin == 'CHF':
        print(f"{usd_to_chf(dollars):.2f} Swiss Francs")
    elif coin == 'ARS':
        print(f"{usd_to_ars(dollars):.2f} Pesos Argentinos")
    else:
        print("Moneda no valida.")
        
        
if __name__ == '__main__':
    main()
