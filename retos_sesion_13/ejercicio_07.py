# Crear una serie de números del 1 al 100, si el número es divisible por 3 imprimir Fizz, 
# si el número es divisible por 5 imprimir Buzz, si el número es divisible por 3 y 5 imprimir FizzBuzz
for numero in range(1, 101):
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)
