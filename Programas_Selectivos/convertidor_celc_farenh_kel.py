"""
Programa para convertir grados Celsius a Fahrenheit o Kelvin.
Formulas:
    Fahrenheit = (C * 9/5) + 32
    Kelvin     = C + 273.15
"""

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
opcion = input("Convertir a (F)ahrenheit o (K)elvin?: ").upper()

match opcion:
    case "F":
        resultado = (celsius * 9 / 5) + 32
        print(f"{celsius} grados Celsius equivalen a {resultado:.2f} grados Fahrenheit")
    case "K":
        resultado = celsius + 273.15
        print(f"{celsius} grados Celsius equivalen a {resultado:.2f} grados Kelvin")
    case _:
        print("Opcion invalida. Ingrese F o K.")
