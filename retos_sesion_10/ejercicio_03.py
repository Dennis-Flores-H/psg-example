# Lugares visitados por cada mochilero
mochilero_a = {"París", "Londres", "Nueva York", "Tokio", "Perú", "Chile", "Colombia", "Bolivia"}
mochilero_b = {"Londres", "Roma", "Nueva York", "Sidney", "Argentina", "Brasil", "Panamá", "Bolivia"}

# Encontrar los lugares que ha visitado el mochilero_a y que no ha visitado el mochilero_b
lugares_unicos_a = mochilero_a - mochilero_b

# Encontrar los lugares que ha visitado el mochilero_b y que no ha visitado el mochilero_a
lugares_unicos_b = mochilero_b - mochilero_a

# Imprimir los resultados
print("Lugares que ha visitado mochilero_a y que mochilero_b no ha visitado:", lugares_unicos_a)
print("Lugares que ha visitado mochilero_b y que mochilero_a no ha visitado:", lugares_unicos_b)
