# Amigos de Jhon Doe y Jess Doe representados como conjuntos
amigos_jhon = {"Alice", "Bob", "Charlie", "David", "Eve"}
amigos_jess = {"Alice", "Bob", "Frank", "Grace"}

# Amigos en común utilizando la intersección de conjuntos
amigos_comunes = amigos_jhon & amigos_jess

# Verificar si tienen amigos en común
if amigos_comunes:
    print(f"Jhon Doe y Jess Doe tienen amigos en común: {amigos_comunes}")
else:
    print("Jhon Doe y Jess Doe no tienen amigos en común.")
