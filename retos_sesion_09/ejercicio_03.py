# Crear una lista de personas con 10 nombres
lista_personas = ["Ana", "Pedro", "María", "Juan", "Luis", "Sofía", "Carlos", "Laura", "Diego", "Elena"]

# Obtener una sublista del índice 2 al 7 (sin incluir el 7)
sublista = lista_personas[2:7]

# Buscar si "Jhon" está en la lista original
existe_jhon = "Jhon" in lista_personas

# Ordenar la sublista alfabéticamente
sublista_ordenada = sorted(sublista)

# Ordenar la lista original alfabéticamente de forma descendente
lista_personas.sort(reverse=True)

# Imprimir resultados
print("Lista original de personas:")
print(lista_personas)

print("\nSublista del índice 2 al 7:")
print(sublista)

print("\n¿Existe 'Jhon' en la lista original?")
print(existe_jhon)

print("\nSublista ordenada alfabéticamente:")
print(sublista_ordenada)

print("\nLista original ordenada alfabéticamente de forma descendente:")
print(lista_personas)