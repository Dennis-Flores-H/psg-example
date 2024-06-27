# Tupla de estudiantes con sus calificaciones
estudiantes = [('Juan', 51), ('Pedro', 80), ('Maria', 90), ('Ana', 40), ('Luis', 30)]

# Iterar sobre la tupla e imprimir las felicitaciones a los que aprobaron
print("Felicitaciones a los estudiantes que aprobaron:")
for estudiante, calificacion in estudiantes:
    if calificacion >= 51:
        print(f"{estudiante} ha aprobado con {calificacion} puntos!")
