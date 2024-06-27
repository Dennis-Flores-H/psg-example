# Inicializar los dos primeros números de la serie de Fibonacci
a, b = 0, 1

# Imprimir los primeros 20 números de Fibonacci
print("Los primeros 20 números de la serie de Fibonacci son:")
for i in range(20):
    print(a, end=" ")
    a, b = b, a + b
print()