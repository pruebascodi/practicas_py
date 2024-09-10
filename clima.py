import random

def simular_clima(dias, temp_inicial, prob_lluvia_inicial):
    # Validar entradas
    if dias <= 0:
        raise ValueError("El número de días debe ser positivo.")
    if not (0 <= prob_lluvia_inicial <= 100):
        raise ValueError("La probabilidad de lluvia debe estar entre 0 y 100.")

    temp = temp_inicial
    prob_lluvia = prob_lluvia_inicial

    temp_max = temp
    temp_min = temp
    dias_lluvia = 0

    print(f"Pronóstico del clima para los próximos {dias} días:")
    for i in range(dias):
        # Verificar si llueve
        llueve = random.random() * 100 <= prob_lluvia
        
        # Mostrar condiciones del día actual
        print(f"Día {i + 1}: Temperatura = {temp}°C, Lluvia = {'Sí' if llueve else 'No'}")
        
        # Actualizar contadores de temperatura máxima y mínima
        if temp > temp_max:
            temp_max = temp
        if temp < temp_min:
            temp_min = temp
        
        # Contador de días con lluvia
        if llueve:
            dias_lluvia += 1
            # Disminuir la temperatura si llueve
            temp -= 1
        
        # Ajustar probabilidad de lluvia para el próximo día
        if temp > 25:
            prob_lluvia = min(100, prob_lluvia + 20)
        elif temp < 5:
            prob_lluvia = max(0, prob_lluvia - 20)
        
        # Ajustar temperatura para el próximo día con 10% de posibilidad
        if random.random() * 100 < 10:
            temp += random.choice([-2, 2])

    print(f"\nTemperatura máxima: {temp_max}°C")
    print(f"Temperatura mínima: {temp_min}°C")
    print(f"Días con lluvia: {dias_lluvia}")

# Ejemplo de uso
dias = int(input("Ingrese el número de días para la predicción: "))
temp_inicial = float(input("Ingrese la temperatura inicial en °C: "))
prob_lluvia_inicial = float(input("Ingrese la probabilidad inicial de lluvia (0-100%): "))

try:
    simular_clima(dias, temp_inicial, prob_lluvia_inicial)
except ValueError as e:
    print(e)
