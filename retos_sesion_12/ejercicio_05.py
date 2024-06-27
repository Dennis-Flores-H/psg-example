# Solicitar al usuario que ingrese su nombre y gustos musicales
nombre = input("Ingrese su nombre: ")
gustos_musicales = input("Ingrese sus gustos musicales (separados por una coma): ")

# Verificar si se ingresó un nombre válido (truthiness)
if nombre:  # Verifica si la cadena no está vacía
    print("Nombre válido.")
    
    # Convertir los gustos musicales en una lista
    gustos_lista = gustos_musicales.split(",")
    
    # Verificar si "rock" está en la lista de gustos musicales
    if "rock" in gustos_lista:
        print("Le gusta el rock.")
    else:
        print("No le gusta el rock.")
else:
    print("No se ingresó ningún nombre.")
