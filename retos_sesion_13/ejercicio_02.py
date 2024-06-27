# Inicialización de variables
contador = 0
numero = 2

# Imprimir los primeros 20 números primos
print("Los primeros 20 números primos son:")
while contador < 20:
    es_primo = True
    # Verificar si numero es primo
    if numero > 1:
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break
        if es_primo:
            print(numero, end=" ")
            contador += 1
    numero += 1
print()