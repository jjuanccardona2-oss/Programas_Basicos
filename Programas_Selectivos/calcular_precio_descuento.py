precio = float(input("Ingrese el monto de la compra: "))

match precio:
    case p if p <= 100:
        descuento = 0
    case p if p <= 200:
        descuento = 0.05
    case p if p <= 500:
        descuento = 0.10
    case p if p > 500:
        descuento = 0.15
    case _:
        descuento = 0

monto_descuento = precio * descuento
precio_final = precio - monto_descuento

print(f"Monto original: {precio:.2f}")
print(f"Descuento aplicado: {descuento * 100:.0f}%")
print(f"Monto de descuento: {monto_descuento:.2f}")
print(f"Precio final a pagar: {precio_final:.2f}")
