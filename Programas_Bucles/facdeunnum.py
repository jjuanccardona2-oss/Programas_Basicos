"""
Programa: Calculadora de Factorial
Descripcion: Calcula el factorial de un numero ingresado por el usuario,
             con validación para numeros negativos.
"""

def calcular_factorial(num):
    """Calcula el factorial de un numero entero no negativo."""
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial


def main():
    while True:
        try:
            num = int(input("Ingrese un numero para calcular su factorial (o 'salir' para terminar): "))
        except ValueError:
            print("Por favor ingrese un numero entero valido.\n")
            continue

        if num < 0:
            print("El factorial no esta definido para numeros negativos.\n")
            continue

        resultado = calcular_factorial(num)
        print(f"El factorial de {num} es: {resultado}\n")

        continuar = input("¿Desea calcular otro factorial? (s/n): ").lower()
        if continuar != 's':
            print("¡Programa finalizado!")
            break


if __name__ == "__main__":
    main()
