# Crear un diccionario para almacenar información de comidas de animales
comidas = {
    "carne": {"animales": ["león", "tigre"]},
    "frutas": {"animales": ["mono", "elefante"]},
    "verduras": {"animales": ["conejo", "tortuga"]}
}
print(comidas)

# Añadir 4 alimentos más al diccionario usando update(clave=valor)
comidas.update(
    pescado={"animales": ["foca", "pingüino"]},
    hojas={"animales": ["jirafa", "panda"]},
    insectos={"animales": ["rana", "lagarto"]},
    semillas={"animales": ["pájaro", "hamster"]}
)
print("\nCarne:", comidas["carne"])
print("Frutas:", comidas["frutas"])
print("Verduras:", comidas["verduras"])
print("Pescado:", comidas["pescado"])
print("Hojas:", comidas["hojas"])
print("Insectos:", comidas["insectos"])
print("Semillas:", comidas["semillas"])

# Verificar si la comida 'carne' existe en el diccionario
existe_carne = "carne" in comidas
print("\n¿Existe la comida 'carne' en el diccionario de comidas?", existe_carne)

# Eliminar la comida 'frutas' del diccionario
frutas = comidas.pop("frutas")
existe_frutas = "frutas" in comidas
print("\n¿Existe la comida 'frutas' en el diccionario de comidas?", existe_frutas)
# Mostrar el diccionario final
print("\nDiccionario de comidas después de las modificaciones:", comidas)