"""
Programa para determinar si una persona puede votar.
Requisito: mayoría de edad (18 años o mas).
"""

# Solicitar datos al usuario
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

# Verificar si puede votar usando match/case
match edad >= 18:
    case True:
        print(f"{nombre}, tienes {edad} años. ¡Puedes votar!")
    case False:
        faltan = 18 - edad
        print(f"{nombre}, tienes {edad} años. Aun no puedes votar. "
              f"Te faltan {faltan} año(s) para cumplir la mayoría de edad.")
