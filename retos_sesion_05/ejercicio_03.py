# Cantidad de segundos a convertir
segundos_totales = 288325

# Calcular días, horas, minutos y segundos
dias = segundos_totales // 86400
segundos_restantes = segundos_totales % 86400

horas = segundos_restantes // 3600
segundos_restantes = segundos_restantes % 3600

minutos = segundos_restantes // 60
segundos = segundos_restantes % 60

# Imprimir el resultado
print(segundos_totales, "segundos equivalen a:")
print(dias, "días,", horas, "horas,", minutos, "minutos y", segundos, "segundos")
