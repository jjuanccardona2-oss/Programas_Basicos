"""
Programa para determinar la estacion del ano segun el numero de mes.
Rangos (hemisferio norte):
    12, 1, 2  -> Invierno
    3, 4, 5   -> Primavera
    6, 7, 8   -> Verano
    9, 10, 11 -> Otono
"""

mes = int(input("Ingrese el numero de mes (1-12): "))

match mes:
    case 12 | 1 | 2:
        estacion = "Invierno"
    case 3 | 4 | 5:
        estacion = "Primavera"
    case 6 | 7 | 8:
        estacion = "Verano"
    case 9 | 10 | 11:
        estacion = "Otono"
    case _:
        estacion = "Mes invalido"

print("Estacion:", estacion)
