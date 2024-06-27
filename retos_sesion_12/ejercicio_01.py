# Solicitar al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))

# Verificar si el número es par o impar utilizando operador ternario
resultado = "par" if numero % 2 == 0 else "impar"

# Mostrar el resultado
print(f"El número {numero} es {resultado}.")
