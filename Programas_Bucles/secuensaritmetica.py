
def main():
	inicio = int(input("Primer numero: "))
	diferencia = int(input("Diferencia: "))
	limite = int(input("Limite maximo: "))

	num = inicio

	while True:
		print(num, end=" ")
		num += diferencia

		if num > limite:
			break

	print("\nSecuencia aritmetica desde", inicio, "hasta", limite)


if __name__ == "__main__":
	main()
