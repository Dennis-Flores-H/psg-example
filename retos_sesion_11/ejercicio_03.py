# Crear un diccionario a partir de la tupla proporcionada
tupla = (('perro', '🐶'), ('gato', '🐱'), ('aves', ['🐦', '🐧']))
animales = dict(tupla)

# Obtener y eliminar el valor de la clave 'aves'
valor_aves = animales.pop('aves')
print("Valor de 'aves' eliminado:", valor_aves)

# Modificar el valor de la clave 'gato' por '😺'
animales['gato'] = '😺'

# Cambiar la clave 'perro' por 'perros' y su valor por ['🐶', '🐩']
animales['perros'] = ['🐶', '🐩']
del animales['perro']

# Mostrar el diccionario final
print("Diccionario final:", animales)
