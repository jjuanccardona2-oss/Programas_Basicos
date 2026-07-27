def reemplazar_manual(texto, car_viejo, car_nuevo):
    resultado = ""
    contador = 0
    for letra in texto:
        if letra == car_viejo:
            resultado += car_nuevo
            contador += 1
        else:
            resultado += letra
    return resultado, contador


if __name__ == "__main__":
    texto = input("Cadena: ")
    car_viejo = input("Caracter a reemplazar: ")
    car_nuevo = input("Caracter nuevo: ")

    if len(car_viejo) != 1 or len(car_nuevo) != 1:
        print("Debe ingresar un solo caracter")
    else:
        texto_mod, num = reemplazar_manual(texto, car_viejo, car_nuevo)
        texto_mod2 = texto.replace(car_viejo, car_nuevo)
        print("Manual:", texto_mod, "| Reemplazos:", num)
        print("Con replace:", texto_mod2)
        if texto_mod == texto_mod2:
            print("Los resultados coinciden")
