# Listas originales de productos y precios
productos = ["Manzanas", "Pan", "Leche", "Huevo", "Arroz"]
precios = [2.5, 0.5, 5.0, 0.8, 1.5]
print("Lista de productos:", productos)
print("Lista de precios:", precios)

# Agregar 5 productos nuevos al final de las listas
productos.extend(["Pasta", "Sal", "Cereal", "Galletas", "Chocolate"])
precios.extend([2.2, 2.5, 4.5, 3.2, 2.8])
print("\nAgregar 5 productos nuevos al final de las listas")
print("Lista de productos:", productos)
print("Lista de precios:", precios)

# Eliminar el producto "Leche" de las listas
index_leche = productos.index("Leche")
productos.pop(index_leche)
precios.pop(index_leche)
print("\nEliminar el producto con el nombre 'Leche' de las listas")
print("Lista de productos:", productos)
print("Lista de precios:", precios)

# Determinar el costo de los productos "Pan" y "Huevo"
print("\nDeterminar el costo de los productos 'Pan' y 'Huevo'")
costo_pan = precios[productos.index("Pan")]
costo_huevo = precios[productos.index("Huevo")]
print("Precio de 'Pan':", costo_pan)
print("Precio de 'Huevo':", costo_huevo)

# Determinar el producto más caro y más barato
print("\nDeterminar el producto más caro y más barato")
producto_mas_caro = productos[precios.index(max(precios))]
producto_mas_barato = productos[precios.index(min(precios))]
print("Producto más caro:", producto_mas_caro)
print("Producto más barato:", producto_mas_barato)

# Cuántos productos hay en total
print("\n¿Cuántos productos tienes en total?")
total_productos  = len(productos)
print("Total de productos:", total_productos)

# Calcular el costo total de los productos
print("\n¿Cuanto cuesta el total de los productos?")
total_costo = sum(precios)
print("Costo total de los productos:", total_costo)

# Ordenar alfabéticamente productos y precios
print("\nOrdenar alfabéticamente productos y precios")
productos_precios_ordenados = sorted(zip(productos, precios))
productos_ordenados, precios_ordenados = zip(*productos_precios_ordenados)
print("Productos ordenados alfabéticamente:", productos_ordenados)
print("Precios correspondientes ordenados:", precios_ordenados)

# Eliminar todos los productos de las listas
print("\nEliminar todos los productos de las listas")
productos.clear()
precios.clear()
print("Lista de productos después de eliminar todo:", productos)
print("Lista de precios después de eliminar todo:", precios)