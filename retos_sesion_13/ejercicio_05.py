# Imprimir un tablero de ajedrez de 8x8 con los caracteres # y *
# Dimensiones del tablero
filas = 8
columnas = 8

# Iterar sobre las filas
for fila in range(filas):
    # Iterar sobre las columnas
    for columna in range(columnas):
        # Determinar el carácter a imprimir basado en la posición
        if (fila + columna) % 2 == 0:
            print("#", end=" ")  # Imprimir # para las posiciones pares
        else:
            print("*", end=" ")  # Imprimir * para las posiciones impares
    print()  # Salto de línea después de imprimir cada fila
