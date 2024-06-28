def calcular_promedio(calificaciones):
    """
    Calcula el promedio de una lista de calificaciones.

    Parámetros:
    calificaciones (list): Lista de calificaciones (números enteros o flotantes).

    Devuelve:
    float: Promedio de las calificaciones.
    """
    total = sum(calificaciones)  # Sumar todas las calificaciones
    cantidad = len(calificaciones)  # Contar la cantidad de calificaciones
    promedio = total / cantidad  # Calcular el promedio
    return promedio

# Lista de calificaciones
calificaciones = [20, 40, 60, 51, 13]

# Calcular el promedio
promedio = calcular_promedio(calificaciones)

# Imprimir el resultado
print(f"El promedio de las calificaciones es: {promedio}")
