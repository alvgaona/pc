"""
Un instagramer que reseña restaurantes desea automatizar 
la calificación y el cálculo del costo total incluyendo 
propina de cada cena mediante un script de python. 
El programa debe pedir el ingreso del nombre del restaurante, 
la calificación (':(', ':|', ':)',':D'), el costo del menú y el 
porcentaje a dejar de propina. Finalmente se debe imprimir un 
resumen con la descripción de los datos ingresados y el gasto total.

Para el cálculo del gasto total incluir redondeo al entero más 
cercano. Guardar el programa en un archivo que se llame menu.py.
"""


def expenditure(menu_cost: float, tip: float):
    return float(menu_cost) + float(tip)


def main():
    print("Ingrese los siguientes datos:")
    name = input("Nombre del restaurant: ")
    grade = input("Calificación (:(, :|, :), :D): ")
    menu_cost = input("Costo del menu (en AR$): ")
    tip = input('Propina: ')

    print("\n")

    print(name)
    print('-' * len(name))
    print(f'Total: {expenditure(menu_cost, tip)}')
    print('Calificación: ' + grade)


if __name__ == '__main__':
    main()
