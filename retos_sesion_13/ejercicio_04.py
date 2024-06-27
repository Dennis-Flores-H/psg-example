while True:
     # Solicita al usuario que ingrese una palabra y convierte todo a minúsculas
    palabra = input("Ingrese una palabra (o 'salir' para terminar): ").lower()
    
    if palabra == 'salir':
        print("¡Adiós!")
        break
     # Eliminar espacios en blanco
    palabra = palabra.replace(" ", "")
    # Verifica si la palabra es un palíndromo comparándola con su reverso
    if palabra == palabra[::-1]:
        print(f"¡La palabra '{palabra}' es un palíndromo!")
    else:
        print(f"La palabra '{palabra}' no es un palíndromo.")
