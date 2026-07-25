
def main():
	consulta = input("Ingrese nombre de artista, pelicula o serie: ").lower()

	match consulta:
		case "inception":
			info = "Pelicula de ciencia ficcion dirigida por Christopher Nolan."
		case "beatles":
			info = "Banda britanica de rock formada en 1960."
		case "rick and morty":
			info = "Serie animada de comedia y ciencia ficcion."
		case "stranger things":
			info = "Serie de terror y ciencia ficcion de Netflix."
		case "avengers":
			info = "Pelicula de superheroes del MCU."
		case _:
			info = "No se encontro informacion."

	print("Informacion:", info)


if __name__ == "__main__":
	main()
