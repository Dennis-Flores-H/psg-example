print("Tabla de Verdad - Puerta")
print("Operador XNOR")
print("Para las luces: True = Encendida, False = Apagada")
print("Para la puerta: True = Abierta, False = Cerrada")

luz_1 = True
luz_2 = True
puerta = not ((luz_1 or luz_2) and not (luz_1 and luz_2))
print (luz_1, "and", luz_2, " \t\tPuerta: ", puerta)

luz_1 = True
luz_2 = False
puerta = not ((luz_1 or luz_2) and not (luz_1 and luz_2))
print (luz_1, "and", luz_2, " \tPuerta: ", puerta)

luz_1 = False
luz_2 = True
puerta = not ((luz_1 or luz_2) and not (luz_1 and luz_2))
print (luz_1, "and", luz_2, " \tPuerta: ", puerta)

luz_1 = False
luz_2 = False
puerta = not ((luz_1 or luz_2) and not (luz_1 and luz_1))
print (luz_1, "and", luz_2, " \tPuerta: ", puerta)
