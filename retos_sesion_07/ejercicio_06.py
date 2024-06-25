# Método center()
print("\n1. METODO CENTER")
# Cadena original
cadena = "Python es genial!"
# Centrar la cadena dentro de un campo de ancho 30
cadena_centro = cadena.center(30)
# Imprimir los resultados
print("Cadena original:", cadena)
print("Cadena centrada:", cadena_centro)

#Método endswith()
print("\n2. METODO ENDSWITH")
# Cadena original
cadena = "Python es genial!"
# Verificar si la cadena termina con el sufijo "genial!"
termina_con_genial = cadena.endswith("genial!")
print("La cadena termina con el sufijo: 'genial'?")
print(termina_con_genial)

#Metodo islower()
print("\n3. METODO ISLOWER")
# Cadena con todos los caracteres alfabéticos en minúsculas
cadena_1 = "python es genial!"
# Cadena con algunos caracteres alfabéticos en mayúsculas
cadena_2 = "Python Es Genial!"
# Verificar si las cadenas están en minúsculas
es_minuscula_1 = cadena_1.islower()
es_minuscula_2 = cadena_2.islower()
# Imprimir los resultados
print(f'¿La cadena "{cadena_1}" está en minúsculas?: {es_minuscula_1}')
print(f'¿La cadena "{cadena_2}" está en minúsculas?: {es_minuscula_2}')

#Método lstrip()
print("\n4. METODO LSTRIP")
# Cadena con espacios en blanco al inicio
cadena_1 = "   Python es genial!"
# Cadena con caracteres específicos al inicio
cadena_2 = "&&&Python es genial!"
# Eliminar espacios en blanco al inicio de la cadena
cadena_sin_espacios = cadena_1.lstrip()
# Eliminar caracteres 'x' al inicio de la cadena
cadena_sin_caracteres = cadena_2.lstrip('&')
# Imprimir los resultados
print(f'Cadena original 1: "{cadena_1}"')
print(f'Cadena con lstrip() aplicada: "{cadena_sin_espacios}"')
print(f'Cadena original 2: "{cadena_2}"')
print(f'Cadena con lstrip("&") aplicada: "{cadena_sin_caracteres}"')

#Método zfill()
print("\n4. METODO ZFILL")
# Definimos una cadena numérica original
numero_1 = "121"
numero_2 = "-42"
# Aplicamos zfill() con un ancho de 8 caracteres
numero_zfilled_1 = numero_1.zfill(8)
numero_zfilled_2 = numero_2.zfill(8)
# Imprimimos los resultados
print("Número original:", numero_1)
print("Número completado a 8 espacios:", numero_zfilled_1)
print("Número original:", numero_2)
print("Número completado a 8 espacios:", numero_zfilled_2)