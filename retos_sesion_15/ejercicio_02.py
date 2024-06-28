# Definimos una excepción personalizada para frutas no permitidas
class FrutaNoPermitidaException(Exception):
    pass

# Lista de frutas permitidas
frutas_permitidas = ["🍅", "🍇", "🍈", "🍉", "🍊", "🍌", "🍍", "🍑"]
canasta = []
while True:
    try:
        fruta = input("Ingresa una fruta (o escribe 'salir' para terminar): ").strip().lower()
        if fruta == "salir":
            break
        if fruta not in frutas_permitidas:
            raise FrutaNoPermitidaException("No ingresa esta fruta a la canasta")
        
        canasta.append(fruta)
    except FrutaNoPermitidaException as e:
        print("🚫 Error:", e)
    except KeyboardInterrupt:
        print('🚫 Para salir escriba "salir"')
    except Exception as e:
        print("💀 Error:", e)
    else:
        print("🎉 Fruta agregada")
    finally:
        print("Frutas en la canasta:", canasta)