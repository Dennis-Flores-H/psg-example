# Crear un diccionario para almacenar la información del animal
animal = {
    "especie": "Tigre",
    "habitat": "Selva",
    "dieta": "Carnívoro",
    "estado_de_salud": "Bueno",
    "edad": 5,
    "responsables": ["Juan Pérez", "María López"]
}

# Acceder y mostrar información del animal
print("Especie:", animal["especie"])
print("Hábitat:", animal["habitat"])
print("Dieta:", animal["dieta"])
print("Estado de salud:", animal["estado_de_salud"])
print("Edad:", animal["edad"])
print("Responsables del cuidado:", animal["responsables"])

# Agregar nueva información (por ejemplo, peso)
animal["peso"] = 200  # Peso en kg
print("Información del animal actualizada con peso:", animal)
