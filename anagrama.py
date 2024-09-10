 

def anagramas(palabra1, palabra2):
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()
    
    # Verificar si las palabras son exactamente iguales
    if palabra1 == palabra2:
        return False
    
    # Comparar las palabras ordenadas
    return sorted(palabra1) == sorted(palabra2)

# Solicitar al usuario que ingrese las palabras
palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

# Llamar a la función y mostrar el resultado
if anagramas(palabra1, palabra2):
    print("Las palabras son anagramas.")
else:
    print("Las palabras no son anagramas.")