# Definición de los números
numero_1 = 123
numero_2 = 890

# Comprobación de paridad
paridad_numero1 = numero_1 % 2 == 0  # True si número_1 es par, False si es impar
paridad_numero2 = numero_2 % 2 == 0  # True si número_2 es par, False si es impar

resultado = not ((paridad_numero1 or paridad_numero2) and not (paridad_numero1 and paridad_numero2))
print("Tienen la misma paridad?")
print(resultado)