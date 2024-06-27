# Datos del cliente (edad y monto de compra)
edad_cliente = 25  # Ejemplo: 25 años
monto_compra = 1200  # Ejemplo: Compra de $1200

# Determinar el descuento aplicable utilizando estructuras condicionales (elif)
if edad_cliente >= 18 and monto_compra > 1000:
    descuento = 0.1  # 10%
elif edad_cliente < 18 and monto_compra > 500:
    descuento = 0.05  # 5%
else:
    descuento = 0.02  # 2%

monto_con_descuento = monto_compra * (1 - descuento)

# Mostrar el monto de la compra con el descuento aplicado
print(f"Monto de la compra con descuento: ${monto_con_descuento:.2f}")
