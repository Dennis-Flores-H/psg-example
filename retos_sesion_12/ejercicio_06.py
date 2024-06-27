# Solicitar al usuario que ingrese dos números y la operación a realizar
num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))
operacion = input("Operación (+, -, *, /): ")

# Verificar la operación ingresada y calcular el resultado
if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: división por cero"
else:
    resultado = "Operación no válida"

# Mostrar el resultado de la operación
print("-------------")
print(f"Resultado: {resultado}")