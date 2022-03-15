def usd_to_cny(dollars: float) -> float:
    return dollars * 6.75

def usd_to_chf(dollars: float) -> float:
    return dollars * 0.94

def usd_to_ars(dollars: float) -> float:
    return dollars * 200

# %%

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
        
    # CHF, ARS, CNY
    # 1 USD 0.94 CHF
    # 1 USD 200 ARS
    # 1 USD 6.75 CNY
       

if __name__ == '__main__':
    main()


# %%
def main():
    dollars = float(input("Ingrese USD: "))
    coin = input("Ingrese moneda: ")
    
    ok = False
    
    if coin == 'CNY':
        result = usd_to_cny(dollars)
        message = 'Chinese Yuan'
        ok = True
    elif coin == 'CHF':
        result = usd_to_chf(dollars)
        message = 'Swiss Francs'
        ok = True
    elif coin == 'ARS':
        result = usd_to_ars(dollars)
        message = 'Pesos Argentinos'
        ok = True
    else:
        print("Moneda no valida.")
        
    # CHF, ARS, CNY
    # 1 USD 0.94 CHF
    # 1 USD 200 ARS
    # 1 USD 6.75 CNY

    # f-strings
    if ok:
        print(f"{result:.2f} {message}")

if __name__ == '__main__':
    main()
