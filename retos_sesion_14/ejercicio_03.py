def fibonacci(n_esimo):
    """
    Calcula el N-ésimo número de la serie de Fibonacci utilizando recursión.
    
    Parámetros:
    n (int): El índice del número de Fibonacci que se desea calcular.

    Devuelve:
    int: El N-ésimo número de la serie de Fibonacci.
    """
    # Casos base
    if(n_esimo < 2):
        return(n_esimo)
    # Caso recursivo
    else:
        return fibonacci(n_esimo - 1) + fibonacci(n_esimo - 2)

# Ejemplo de uso
n_esimo = 5 # número de la serie de Fibonacci: 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597
print(f"El número {n_esimo} de la serie de Fibonacci es: {fibonacci(n_esimo - 1)}")
