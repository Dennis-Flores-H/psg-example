# Correccion: Declaramos el valor de pi de manera estática
pi = 3.141592653589793

# Creamos la función anónima
area_circulo = lambda radio: pi * radio**2

# Calculamos el área del círculo con radio 5
radio = 5
resultado = area_circulo(radio)

# Redondeamos el área a 3 decimales usando format
resultado = "{:.3f}".format(resultado)

print(f"El área de un círculo con radio {radio} es: {resultado}")
