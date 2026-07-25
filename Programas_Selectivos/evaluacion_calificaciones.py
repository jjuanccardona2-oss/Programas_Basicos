"""
Programa para evaluar calificaciones y convertirlas a letra.
Escala:
    90 - 100 -> A
    80 - 89  -> B
    70 - 79  -> C
    60 - 69  -> D
    0  - 59  -> F
"""

nota = int(input("Ingrese la calificacion (0-100): "))

match nota:
    case n if 90 <= n <= 100:
        letra = "A"
    case n if 80 <= n <= 89:
        letra = "B"
    case n if 70 <= n <= 79:
        letra = "C"
    case n if 60 <= n <= 69:
        letra = "D"
    case n if 0 <= n <= 59:
        letra = "F"
    case _:
        letra = "Calificacion invalida"

print("Calificacion en letra:", letra)
