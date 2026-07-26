def main():
    num = int(input("Numero entero: "))

    if num == 0:
        digitos = 1
    else:
        digitos = 0
        if num < 0:
            num = abs(num)
        while num > 0:
            num //= 10
            digitos += 1

    print("El numero tiene", digitos, "digitos")


if __name__ == "__main__":
    main()
