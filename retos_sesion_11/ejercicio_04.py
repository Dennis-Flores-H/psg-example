# Crear el diccionario inicial de hábitats en peligro y especies asociadas
habitats = {
    "polo norte": {"especies": {"oso polar", "morsa", "ballena"}},
    "amazonas": {"especies": {"tigre", "mono", "guacamayo"}}
}
print(habitats)

# Añadir dos hábitats más al diccionario utilizando update()
habitats.update({
    "sabana": {"especies": {"león", "cebra", "elefante"}},
    "selva lluviosa": {"especies": {"jaguar", "loro", "boa constrictor"}}
})
print("\nPolo Norte:", habitats["polo norte"])
print("Amazonas:", habitats["amazonas"])
print("Sabana:", habitats["sabana"])
print("Selva lluviosa:", habitats["selva lluviosa"])

# Verificar si el hábitat 'amazonas' existe en el diccionario de hábitats
existe_amazonas = "amazonas" in habitats
print("\n¿Existe el hábitat 'amazonas' en el diccionario de hábitats?", existe_amazonas)

# Añadir la especie 'anaconda' al diccionario de especies dentro del hábitat 'amazonas'
habitat_amazonas = habitats["amazonas"] # Acceder al diccionario de especies dentro del hábitat 'amazonas'
especies_amazonas = habitat_amazonas["especies"] # Acceder al conjunto de especies dentro del hábitat 'amazonas'
especies_amazonas.add("anaconda") # Añadir la especie 'anaconda' al conjunto de especies

# Mostrar el diccionario final
print("\nDiccionario final de hábitats en peligro:")
print("Polo Norte:", habitats["polo norte"])
print("Amazonas:", habitats["amazonas"])
print("Sabana:", habitats["sabana"])
print("Selva lluviosa:", habitats["selva lluviosa"])
