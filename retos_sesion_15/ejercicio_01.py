while True:
    try:
        num1 = input("Ingrese el primer número (o 'salir' para terminar): ")
        if num1 == "salir":
            break
        num1 = float(num1)
        num2 = input("Ingrese el segundo número (o 'salir' para terminar): ")
        if num2 == "salir":
            break
        num2 = float(num2)
        operacion = input("Ingrese la operación a realizar (+, -, *, /): ")
        if operacion == "salir":
            break
        
        if operacion not in ('+', '-', '*', '/'):
            raise ValueError("Operación no válida")
        
        if operacion == '+':
            resultado = num1 + num2
        elif operacion == '-':
            resultado = num1 - num2
        elif operacion == '*':
            resultado = num1 * num2
        elif operacion == '/':
            resultado = num1 / num2
        
    except ValueError as e:
        print(f"🎭 Error: {e}")
    except TypeError as e:
        print(f"T Error: {e}")
    except ZeroDivisionError as e:
        print(f"0️⃣ Error: {e}")
    except KeyboardInterrupt:
        print('🚫 Para salir escriba "salir"')
    except Exception as e:
        print(f"💀 Error inesperado: {e}")
    else:
        print(f"Resultado de {num1} {operacion} {num2} = {resultado}")
        print("Operación completada.\n")