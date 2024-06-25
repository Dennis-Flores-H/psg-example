print("Operador XNOR")

# Caso 1: a = True, b = True
a = True
b = True
resultado = not ((a or b) and not (a and b))
print(resultado)  # Debe imprimir True

# Caso 2: a = True, b = False
a = True
b = False
resultado = not ((a or b) and not (a and b))
print(resultado)  # Debe imprimir True

# Caso 3: a = False, b = True
a = False
b = True
resultado = not ((a or b) and not (a and b))
print(resultado)  # Debe imprimir False

# Caso 4: a = False, b = False
a = False
b = False
resultado = not ((a or b) and not (a and b))
print(resultado)  # Debe imprimir True