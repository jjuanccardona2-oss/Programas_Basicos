import random

def main():
    secreto = random.randint(1, 100)

    while True:
        intento = int(input("Adivina (1-100): "))

        if intento < secreto:
            print("Demasiado bajo")
        elif intento > secreto:
            print("Demasiado alto")
        else:
            print("Correcto! Era", secreto)
            break

    print("Juego terminado. El numero era", secreto)


if __name__ == "__main__":
    main()
