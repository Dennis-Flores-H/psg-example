# Cadena a verificar como palíndromo
cadena = input("Ingrese la cadena: ")
#cadena = "Anita lava la Tina"
copia = cadena
# Eliminar espacios en blanco y convertir a minúsculas
cadena = cadena.replace(" ", "").lower()
# Comparar la cadena con su versión invertida
es_palindromo = cadena == cadena[::-1]
# Imprimir el resultado
print(f'¿"{copia}" es un palíndromo?: {es_palindromo}')