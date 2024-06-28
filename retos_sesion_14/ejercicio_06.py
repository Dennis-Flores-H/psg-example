def obtener_numeros_pares(numeros):
    """
    Esta función recibe una lista de números y devuelve una lista con solo los números pares.

    Parámetros:
    numeros (list): La lista de números a filtrar.

    Devuelve:
    list: Una lista que contiene solo los números pares.
    """
    # Filtrar los números pares utilizando una lista de comprensión
    numeros_pares = [num for num in numeros if num % 2 == 0]
    return numeros_pares

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = obtener_numeros_pares(numeros)
print(f"Los números pares de la lista son: {numeros_pares}")
