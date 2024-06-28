def inicializar_tablero():
    """
    Inicializa el tablero de tres en raya con espacios en blanco.
    """
    return [[" " for _ in range(3)] for _ in range(3)]

def imprimir_tablero(tablero):
    """
    Imprime el tablero de tres en raya.
    """
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)

def verificar_ganador(tablero):
    """
    Verifica si hay un ganador en el tablero.
    Devuelve el símbolo del ganador ('X' o 'O') o None si no hay ganador.
    """
    # Verificar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return tablero[i][0]
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return tablero[0][i]
    
    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return tablero[0][2]
    
    return None

def tablero_lleno(tablero):
    """
    Verifica si el tablero está lleno.
    """
    for fila in tablero:
        if " " in fila:
            return False
    return True

def tres_en_raya():
    """
    Función principal para jugar tres en raya.
    """
    tablero = inicializar_tablero()
    jugador_actual = "X"
    
    while True:
        imprimir_tablero(tablero)
        
        jugada = input(f"Jugador {jugador_actual}, ingrese su jugada fila,columna Ej: 0,0 o 'salir' para terminar: ").lower()
        if jugada == "salir":
            print("¡Juego terminado!")
            break
        
        if len(jugada) == 3 and jugada[1] == ',' and jugada[0].isdigit() and jugada[2].isdigit():
            fila, columna = int(jugada[0]), int(jugada[2])
            if 0 <= fila < 3 and 0 <= columna < 3 and tablero[fila][columna] == " ":
                tablero[fila][columna] = jugador_actual
            else:
                print("La posición es inválida o ya está ocupada. Intente de nuevo.")
                continue
        else:
            print("Entrada inválida. Intente de nuevo.")
            continue
        
        ganador = verificar_ganador(tablero)
        if ganador:
            imprimir_tablero(tablero)
            print(f"¡El jugador {ganador} ha ganado!")
            break
        
        if tablero_lleno(tablero):
            imprimir_tablero(tablero)
            print("¡Empate! El tablero está lleno.")
            break
        
        # Cambiar al otro jugador
        jugador_actual = "O" if jugador_actual == "X" else "X"

# Ejecutar el juego de tres en raya
tres_en_raya()
