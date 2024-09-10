def encrypt(text):
    # Reemplazar caracteres
    encrypted_text = text.replace('a', '@')\
                         .replace('e', '1')\
                         .replace('i', '2')\
                         .replace('o', '0')\
                         .replace('u', '3')
    
    # Invertir el texto
    return encrypted_text[::-1]

def decrypt(encrypted_text):
    # Invertir el texto
    reversed_text = encrypted_text[::-1]
    
    # Reemplazar caracteres
    return reversed_text.replace('3', 'u')\
                        .replace('0', 'o')\
                        .replace('2', 'i')\
                        .replace('1', 'e')\
                        .replace('@', 'a')

def main():
    print("Elige una opción:")
    print("1. Encriptar")
    print("2. Desencriptar")
    
    option = input("Ingresa una opcion: ")
    
    if option == '1':
        text = input("Ingresa el texto que deseas encriptar: ")
        encrypted = encrypt(text)
        print("Texto encriptado:", encrypted)
    elif option == '2':
        encrypted_text = input("Ingresa el texto que deseas desencriptar: ")
        decrypted = decrypt(encrypted_text)
        print("Texto desencriptado:", decrypted)
    else:
        print("Opción no válida. Por favor, elige 1 o 2.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()