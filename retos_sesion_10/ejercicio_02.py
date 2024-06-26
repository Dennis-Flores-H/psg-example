# Menús de los restaurantes mexicano e italiano
menu_mexicano = {"Tacos", "Enchiladas", "Guacamole", "Tamales"}
menu_italiano = {"Pizza", "Pasta", "Lasagna", "Tiramisú"}

# Unir los menús para crear el menú de comida fusión
menu_fusion = menu_mexicano | menu_italiano

# Imprimir el nuevo menú de comida fusión
print("Menú de comida fusión:", menu_fusion)
