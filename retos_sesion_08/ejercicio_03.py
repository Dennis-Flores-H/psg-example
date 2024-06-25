# Ingreso de la cadena por teclado
cadena = input("Ingresa una cadena: ")

# Almacenamiento en una tupla
tupla_almacenada = tuple(cadena)

# Concatenación con las tuplas adicionales
tupla_concatenada = ('¡', ) + tupla_almacenada + ('!', )

# Impresión del resultado concatenado
print("Resultado concatenado:", tupla_concatenada)

# Repetición de la tupla final 3 veces
resultado_repetido = tupla_concatenada * 3

# Impresión del nuevo resultado
print("Resultado repetido 3 veces:", resultado_repetido)
