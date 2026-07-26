def main():
    suma = 0
    contador = 0

    while True:
        try:
            num = float(input("Numero positivo (negativo sale): "))
        except ValueError:
            print("Entrada no valida. Intente de nuevo.")
            continue

        if num < 0:
            break

        if num > 0:
            suma += num
            contador += 1

    if contador > 0:
        media = suma / contador
        print("Media:", media)
    else:
        print("No se ingresaron positivos")


if __name__ == "__main__":
    main()
