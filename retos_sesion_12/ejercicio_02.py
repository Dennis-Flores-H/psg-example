# Supongamos que tenemos una variable booleana que indica si el usuario ha iniciado sesión
usuario_iniciado_sesion = False

# Verificar si el usuario ha iniciado sesión usando operador ternario
mensaje = "Acceso permitido." if usuario_iniciado_sesion else "Error: Debes iniciar sesión para acceder."

# Mostrar el mensaje
print(mensaje)
