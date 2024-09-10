def palindromo(texto):
    texto = ''.join(c.lower() for c in texto if c.isalnum())
    
    # Comparar el texto normalizado con su reverso
    return texto == texto[::-1]

# Ejemplo de uso
texto = input("Ingrese un texto para verificar si es un palíndromo: ")
if palindromo(texto):
    print("El texto es un palíndromo.")
else:
    print("El texto no es un palíndromo.")