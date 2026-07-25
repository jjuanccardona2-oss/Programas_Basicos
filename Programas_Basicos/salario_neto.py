print("=== CALCULO DEL SALARIO NETO ===")

salario_bruto = float(input("Ingrese el salario bruto: "))
porcentaje_impuestos = float(input("Ingrese el porcentaje de impuestos: "))
deducciones = float(input("Ingrese el monto de las deducciones: "))

impuestos = salario_bruto * (porcentaje_impuestos / 100)
salario_neto = salario_bruto - impuestos - deducciones

print(f"El salario neto es: {salario_neto:.2f}")