# Lista de productos disponibles con sus precios (en centavos).
productos = {
    1: {"nombre": "Galletas", "precio": 300},  # Precio en centavos
    2: {"nombre": "Confite", "precio": 600}
}

# Función para simular la máquina expendedora
def maquina_expendedora(monedas, seleccion):
    # Calcular el total de dinero ingresado
    total_dinero = sum(monedas)

    # Verificar si la selección del producto es válida
    if seleccion not in productos:
        return "Selección inválida. Por favor, elige un producto válido."

    # Obtener el producto seleccionado y su precio
    producto = productos[seleccion]
    precio = producto["precio"]

    # Verificar si el dinero ingresado es suficiente
    if total_dinero < precio:
        return f"Dinero insuficiente. Ingresaste {total_dinero} centavos, pero el {producto['nombre']} cuesta {precio} centavos."

    # Calcular el cambio
    cambio = total_dinero - precio
    return f"Dispensando {producto['nombre']}. Tu cambio es {cambio} centavos."

# Solicitar la selección del producto al usuario
print("Productos disponibles:")
for key, value in productos.items():
    print(f"{key}. {value['nombre']} - {value['precio']} centavos")

try:
    seleccion = int(input("Por favor, selecciona un producto (1 o 2): "))

    # Solicitar al usuario las monedas ingresadas
    monedas = []
    print("Introduce las monedas (valores permitidos: 200, 500, 1000). Escribe '0' para finalizar:")
    while True:
        moneda = int(input("Introduce una moneda: "))
        if moneda == 0:
            break
        if moneda in [200, 500, 1000]:
            monedas.append(moneda)
        else:
            print("Moneda no válida, solo se aceptan monedas de 200, 500, 1000 centavos.")

    # Llamar a la función de la máquina expendedora con las entradas del usuario
    resultado = maquina_expendedora(monedas, seleccion)
    print(resultado)

except ValueError:
    print("Entrada no válida. Por favor, introduce números enteros.")
