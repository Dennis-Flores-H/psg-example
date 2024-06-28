import math

# Crear la función anónima
area_circulo = lambda radio: math.pi * radio**2

# Calcular el área del círculo con radio 5
radio = 5
resultado = area_circulo(radio)
# Redondear el área a 3 decimales usando format
resultado = "{:.3f}".format(resultado)

print(f"El área de un círculo con radio {radio} es: {resultado}")
