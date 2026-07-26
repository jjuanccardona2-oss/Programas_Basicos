def main():
    while True:
        print("1.Suma 2.Resta 3.Multiplicacion 4.Division 5.Salir")
        op = int(input("Opcion: "))

        if op == 5:
            break

        a = float(input("Primer numero: "))
        b = float(input("Segundo numero: "))

        match op:
            case 1:
                print(a + b)
            case 2:
                print(a - b)
            case 3:
                print(a * b)
            case 4:
                if b != 0:
                    print(a / b)
                else:
                    print("Error: division por cero")
            case _:
                print("Opcion invalida")

        resp = input("Desea continuar? (s/n): ").lower()
        if resp == 'n':
            break


if __name__ == "__main__":
    main()
