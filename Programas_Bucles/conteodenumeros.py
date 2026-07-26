"""
Programa: Conteo de numeros
Descripcion: Solicita al usuario una cantidad de numeros y cuenta
             cuantos son mayores, menores e iguales a cero.
"""

def main():
    try:
        n = int(input("Cantidad de numeros a ingresar: "))
    except ValueError:
        print("Entrada invalida. Por favor ingrese un numero entero.")
        return

    mayores = 0
    menores = 0
    iguales = 0

    for i in range(n):
        while True:
            try:
                num = int(input(f"Numero {i + 1}: "))
                break
            except ValueError:
                print("Entrada invalida. Ingrese un numero entero.")

        if num > 0:
            mayores += 1
        elif num < 0:
            menores += 1
        else:
            iguales += 1

    print("\nResultados:")
    print("Mayores a 0:", mayores)
    print("Menores a 0:", menores)
    print("Iguales a 0:", iguales)


if __name__ == "__main__":
    main()
