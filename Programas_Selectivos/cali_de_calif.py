# Clasificacion de calificaciones
# Pedimos la calificacion al usuario
nota = float(input("Ingrese la calificacion: "))

# Hacemos una serie de condicionales if anidados
# Asi clasificamos la calificacion en letras
if nota >= 90:
    letra = "A"
elif nota >= 80:
    letra = "B"
elif nota >= 70:
    letra = "C"
elif nota >= 60:
    letra = "D"
else:
    letra = "F"

# Imprimimos el resultado de la nota
print("La calificacion es:", letra)
