# Crea un ciclo infinito que reciba un número por teclado y verifique si es un número primo, 
# termina la ejecución si se ingresa el número 0
while True:
    numero = int(input("Ingrese un número (o '0' para terminar): "))
    
    if numero == 0:
        print("¡Adiós!")
        break
    
    if numero < 2:
        print(f"El número {numero} no es un número primo.")
        continue
    
    es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    
    if es_primo:
        print(f"El número {numero} es un número primo.")
    else:
        print(f"El número {numero} no es un número primo.")
