def main():
    N = int(input("Numero positivo: "))
    i = 1

    while True:
        if i % 2 != 0:
            print(i, end=" ")

        i += 1

        if i > N:
            break

    print("\nFin. Se mostraron los impares hasta", N)


if __name__ == "__main__":
    main()
