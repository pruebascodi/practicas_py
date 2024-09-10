import random
import string

def generar_contrasena(longitud=12, mayusculas=False, numeros=False, simbolos=False):
    if longitud < 8 or longitud > 16:
        raise ValueError("La longitud debe estar entre 8 y 16 caracteres.")
    
    caracteres = string.ascii_lowercase
    if mayusculas:
        caracteres += string.ascii_uppercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Debes seleccionar al menos un tipo de carácter.")

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

# Ejemplo de uso
longitud = int(input("Ingrese la longitud de la contraseña (8-16): "))
mayusculas = input("¿Incluir letras mayúsculas? (si/no): ").lower() == 'si'
numeros = input("¿Incluir números? (si/no): ").lower() == 'si'
simbolos = input("¿Incluir símbolos? (si/no): ").lower() == 'si'

try:
    contrasena = generar_contrasena(longitud, mayusculas, numeros, simbolos)
    print("Contraseña generada:", contrasena)
except ValueError as e:
    print(e)
