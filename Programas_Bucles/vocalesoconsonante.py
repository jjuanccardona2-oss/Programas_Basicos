def main():
    while True:
        letra = input("Ingrese letra (espacio termina): ")

        if letra == " ":
            break

        letra = letra.lower()

        if letra in "aeiou":
            print("Vocal")
        else:
            print("Consonante")

    print("Programa finalizado")


if __name__ == "__main__":
    main()
