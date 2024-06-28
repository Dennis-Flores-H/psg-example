# Definimos una excepción personalizada para saldo insuficiente
class SaldoInsuficienteException(Exception):
    pass

saldo = 5000 #saldo inicial
while(True):
    try:
        monto = float(input("Ingrese el monto a retirar: "))
        if monto > saldo:
            raise SaldoInsuficienteException("Saldo insuficiente.")
        elif monto > 1000:
            raise Exception("El monto no puede ser mayor a 1000")
        else:
            print(f"Retirando {monto}...")
            saldo -= monto
            print(f"Nuevo saldo: {saldo}")
    except ValueError:
        print("Error: ¡Ingrese un monto válido!")
    except SaldoInsuficienteException as e:
        print("🚫 Error:", e)
        print("Saldo: ",saldo)
    except Exception as e:
        print("💀 Error:", e)
    else: 
        print("Retiro realizado con exito")
    finally:
        print("¡Gracias por utilizar nuestro cajero!\n")