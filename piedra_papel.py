def obtener_eleccion(nombre):
    """Función para obtener una elección válida del usuario."""
    while True:
        eleccion = input(f"{nombre}, elige piedra, papel o tijera: ").strip().lower()
        if eleccion in ['piedra', 'papel', 'tijera']:
            return eleccion
        print("Elección inválida. Por favor elige entre piedra, papel o tijera.")

def determinar_ganador(eleccion1, eleccion2):
    """Función para determinar el ganador entre dos elecciones."""
    if eleccion1 == eleccion2:
        return 'empate'
    elif (eleccion1 == 'piedra' and eleccion2 == 'tijera') or \
         (eleccion1 == 'papel' and eleccion2 == 'piedra') or \
         (eleccion1 == 'tijera' and eleccion2 == 'papel'):
        return 'usuario1'
    else:
        return 'usuario2'

def juego_piedra_papel_tijera():
    """Función principal para jugar piedra, papel o tijera entre dos usuarios."""
    # Pedir los nombres de los usuarios
    usuario1 = input("Ingrese el nombre del primer usuario: ")
    usuario2 = input("Ingrese el nombre del segundo usuario: ")

    victorias_usuario1 = 0
    victorias_usuario2 = 0
    rondas = 3  # Número de rondas a jugar

    for ronda in range(1, rondas + 1):
        print(f"\nRonda {ronda}")
        eleccion1 = obtener_eleccion(usuario1)
        eleccion2 = obtener_eleccion(usuario2)

        ganador = determinar_ganador(eleccion1, eleccion2)

        if ganador == 'empate':
            print(f"Ambos eligieron {eleccion1}. ¡Es un empate!")
        elif ganador == 'usuario1':
            victorias_usuario1 += 1
            print(f"{usuario1} ganó esta ronda.")
        else:
            victorias_usuario2 += 1
            print(f"{usuario2} ganó esta ronda.")
    
    # Imprimir resultados finales
    print("\nResultados finales:")
    print(f"{usuario1} ganó {victorias_usuario1} veces.")
    print(f"{usuario2} ganó {victorias_usuario2} veces.")

    if victorias_usuario1 > victorias_usuario2:
        print(f"{usuario1} es el ganador del juego.")
    elif victorias_usuario2 > victorias_usuario1:
        print(f"{usuario2} es el ganador del juego.")
    else:
        print("El juego terminó en empate.")

# Ejecutar el juego
juego_piedra_papel_tijera()