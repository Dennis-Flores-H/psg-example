def calculadora_flexible(**kwargs):
    """
    Realiza cálculos matemáticos basados en operaciones pasadas como argumentos de palabras clave.

    Las operaciones pueden ser 'suma', 'resta', 'multiplicación' y 'división'. 
    Cada operación debe ser un par clave-valor, donde la clave es la operación y el valor es una lista de operandos.

    Parámetros:
    **kwargs: Diccionario de operaciones y sus operandos.

    Devuelve:
    dict: Diccionario con los resultados de las operaciones.
    """
    resultados = {}
    
    # Suma
    if 'suma' in kwargs:
        resultados['suma'] = sum(kwargs['suma'])

    # Resta
    if 'resta' in kwargs:
        valores = kwargs['resta']
        resultados['resta'] = valores[0] - sum(valores[1:])

    # Multiplicación
    if 'multiplicación' in kwargs:
        resultado_multiplicacion = 1
        for valor in kwargs['multiplicación']:
            resultado_multiplicacion *= valor
        resultados['multiplicación'] = resultado_multiplicacion

    # División
    if 'división' in kwargs:
        valores = kwargs['división']
        resultado_division = valores[0]
        for valor in valores[1:]:
            resultado_division /= valor
        resultados['división'] = resultado_division
    
    return resultados

# Ejemplo de uso
operaciones = {
    'suma': [10, 20, 40],
    'resta': [100, 20, 10],
    'multiplicación': [2, 3, 5],
    'división': [100, 5]
}

# Calcular y mostrar los resultados
resultados = calculadora_flexible(**operaciones)
for operacion, resultado in resultados.items():
    print(f"El resultado de la {operacion} es: {resultado}")