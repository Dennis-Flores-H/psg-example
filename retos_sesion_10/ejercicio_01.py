# Platos pedidos por Anita y Pepito
platos_anita = {"Sushi", "Pizza", "Tacos", "Hamburguesa", "Pasta", "Alitas"}
platos_pepito = {"Pizza", "Tacos", "Ensalada", "Pasta", "Helado", "Milanesa"}

# Encontrar la intersección (platos en común)
platos_comunes = platos_anita & platos_pepito

# Calcular la cantidad de platos en común y el total de platos únicos
num_platos_comunes = len(platos_comunes)
total_platos_unicos = len(platos_anita | platos_pepito)

# Calcular el porcentaje de platos en común
porcentaje_comun = (num_platos_comunes / total_platos_unicos) * 100

# Decidir si siguen saliendo basándose en el porcentaje
seguir_saliendo = porcentaje_comun > 50

# Imprimir resultados
print("Platos en común:", platos_comunes)
print("Número de platos en común:", num_platos_comunes)
print("Total de platos únicos:", total_platos_unicos)
print("Porcentaje de platos en común:", porcentaje_comun)
print("¿Seguirán saliendo?")
print(seguir_saliendo)
