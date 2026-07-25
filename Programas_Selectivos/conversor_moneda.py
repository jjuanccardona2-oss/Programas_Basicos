tasas = {
    "USD": 0.054,     # Dolar estadounidense
    "EUR": 0.050,     # Euro
    "THB": 1.90,      # Baht tailandes
    "JPY": 8.10,      # Yen japones
    "KRW": 74.50,     # Won surcoreano
    "AUD": 0.083,     # Dolar australiano
    "PEN": 0.20,      # Sol peruano
    "CAD": 0.075,     # Dolar canadiense
    "VES": 3.30,      # Bolivar venezolano
    "ARS": 55.00      # Peso argentino
}

monto_mxn = float(input("Ingrese el monto en pesos mexicanos (MXN): "))
moneda = input("Convertir a (USD, EUR, THB, JPY, KRW, AUD, PEN, CAD, VES, ARS): ").upper()

match moneda:
    case "USD" | "EUR" | "THB" | "JPY" | "KRW" | "AUD" | "PEN" | "CAD" | "VES" | "ARS":
        resultado = monto_mxn * tasas[moneda]
        print(f"{monto_mxn:.2f} MXN equivalen a {resultado:.2f} {moneda}")
    case _:
        print("Moneda no reconocida. Opciones validas: USD, EUR, THB, JPY, KRW, AUD, PEN, CAD, VES, ARS")
