# Crear el diccionario inicial del arca con las especies y su cantidad inicial
arca = {
    "perro": 2,
    "gato": 2,
    "tigre": 2,
    "mono": 2,
    "unicornio": 0,
    "jirafa": 1
}
print(arca)

# Añadir dos especies más al arca utilizando update()
arca.update({
    "elefante": 2,
    "león": 1
})
print("\nArca con nuevas especies añadidas:")
print(arca)

# Obtener lista de animales en el arca iterando el diccionario
print("\nLista de animales en el arca:")
iterador = iter(arca.items())
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)

# Verificar si la especie 'dragon' existe en el arca
especie_dragon = 'dragon' in arca
print("\n¿La especie 'dragon' está en el arca?", especie_dragon)

# Eliminar la especie 'unicornio' del arca
del arca["unicornio"]
print("\nArca después de eliminar 'unicornio':")
print(arca)

# Modificar el valor de la especie 'jirafa' por 2
arca['jirafa'] = 2
print("\nArca después de modificar 'jirafa':")
print(arca)

# Vaciar completamente el arca después del diluvio
arca.clear()
print("\nArca vacía después del diluvio:")
print(arca)
