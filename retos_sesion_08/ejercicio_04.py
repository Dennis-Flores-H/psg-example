# Definir la tupla con las notas del estudiante
notas = (34, 61, 80, 20, 12, 69, 32, 60, 61, 51, 90, 23, 15)

# Calcular el promedio de las notas
promedio = sum(notas) / len(notas)

# Determinar si el estudiante aprobó el semestre (True si promedio >= 51, False si no)
resultado = promedio >= 51

# Mostrar los resultados
print("Notas del estudiante:", notas)
print("Promedio:", promedio)
print("¿El estudiante aprobo?")
print(resultado)
