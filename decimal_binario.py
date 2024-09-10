def decimal_a_binario(decimal):
    if decimal == 0:
        return "0"
    
    binario = ""
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal = decimal // 2
    
    return binario

def binario_a_decimal(binario):
    decimal = 0
    longitud = len(binario)
    
    for i in range(longitud):
        digito = int(binario[longitud - i - 1])
        decimal += digito * (2 ** i)
    
    return decimal

# Solicitar al usuario la opción deseada

print("Seleccione una opción de conversion:")
print("1. Convertir de decimal a binario")
print("2. Convertir de binario a decimal")

opcion = int(input("Ingrese el número de la opción deseada: "))

if opcion == 1:
    decimal = int(input("Ingrese un número decimal: "))
    print(f"El número binario es: {decimal_a_binario(decimal)}")
elif opcion == 2:
    binario = input("Ingrese un número binario: ")
    print(f"El número decimal es: {binario_a_decimal(binario)}")
else:
    print("Opción no válida.")