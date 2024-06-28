def invertir_cadena(cadena):
    """
    Esta función recibe una cadena y devuelve la cadena invertida.

    Parámetros:
    cadena (str): La cadena a invertir.

    Devuelve:
    str: La cadena invertida.
    """
    return cadena[::-1]

# Ejemplo de uso
cadena = "Hola Mundo"
cadena_invertida = invertir_cadena(cadena)
print(f"La cadena invertida de '{cadena}' es: '{cadena_invertida}'")
