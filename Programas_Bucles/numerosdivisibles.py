"""
Programa: Multiplos de 3 y 5
Descripcion: Muestra todos los numeros entre 1 y 100 que son
             divisibles tanto por 3 como por 5.
"""

def main():
    print("Numeros divisibles por 3 y 5 (1-100):")

    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(i, end=" ")

    print()  # salto de linea final


if __name__ == "__main__":
    main()
