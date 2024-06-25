# Cadena a verificar como palíndromo
cadena = "Anita lava la Tina"

# Eliminar espacios en blanco y convertir a minúsculas
cadena = cadena.replace(" ", "").lower()

# Comparar la cadena con su versión invertida
es_palindromo = cadena == cadena[::-1]

# Imprimir el resultado
print(f'¿"{cadena}" es un palíndromo?: {es_palindromo}')