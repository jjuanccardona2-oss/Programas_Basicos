def main():
    palabra = input("Ingrese una palabra: ").lower()

    contador = 0
    for letra in palabra:
        if letra == 'a':
            contador += 1

    print("La letra 'a' aparece", contador, "veces")


if __name__ == "__main__":
    main()
