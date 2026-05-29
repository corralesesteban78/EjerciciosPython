import os
import sys

# Mapa obligatorio del taller (hardcoded)
MAPA_INICIAL = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', '$', ' ', ' ', '#'],
    ['#', ' ', '.', '@', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#'],
]

# Estado global del mapa (copia profunda del inicial)
mapa = [fila[:] for fila in MAPA_INICIAL]


def dibujar_mapa(matriz):
    """Limpia la terminal y dibuja el mapa actual con las instrucciones."""
    # Limpiar pantalla (funciona en Windows y Unix)
    os.system('cls' if os.name == 'nt' else 'clear')

    print("=" * 20)
    print("   S O K O B A N")
    print("=" * 20)

    for fila in matriz:
        print(''.join(fila))

    print()
    print("Controles:")
    print("  W = Arriba   S = Abajo")
    print("  A = Izquierda  D = Derecha")
    print("  Q = Salir")
    print()


def obtener_posicion_jugador(matriz):
    """Recorre la matriz y retorna (fila, columna) del jugador (@)."""
    for i, fila in enumerate(matriz):
        for j, celda in enumerate(fila):
            if celda == '@':
                return i, j
    return None, None  # No debería ocurrir, pero evita crash


def mover(direccion):
    """
    Contiene toda la lógica de validación de colisiones y movimiento.
    Retorna True si el movimiento fue válido, False si no.
    """
    # Mapeo de dirección a delta (fila, columna)
    deltas = {
        'w': (-1, 0),
        's': (1, 0),
        'a': (0, -1),
        'd': (0, 1),
    }

    if direccion not in deltas:
        return False  # Tecla no reconocida

    df, dc = deltas[direccion]
    fila_j, col_j = obtener_posicion_jugador(mapa)

    if fila_j is None:
        return False  # Jugador no encontrado

    # Posición destino del jugador
    nueva_f = fila_j + df
    nueva_c = col_j + dc

    # Verificar límites del mapa para la posición destino
    if nueva_f < 0 or nueva_f >= len(mapa) or nueva_c < 0 or nueva_c >= len(mapa[0]):
        return False  # Fuera de límites

    celda_destino = mapa[nueva_f][nueva_c]

    # Caso 1: Destino es pared → no se mueve
    if celda_destino == '#':
        return False

    # Caso 2: Destino es una caja o caja sobre meta → intentar empujar
    if celda_destino in ('$', '*'):
        # Posición detrás de la caja
        caja_f = nueva_f + df
        caja_c = nueva_c + dc

        # Verificar límites para la posición detrás de la caja
        if caja_f < 0 or caja_f >= len(mapa) or caja_c < 0 or caja_c >= len(mapa[0]):
            return False  # Empujaría la caja fuera del mapa

        celda_tras_caja = mapa[caja_f][caja_c]

        # Solo se puede empujar si el espacio detrás es libre o es meta
        if celda_tras_caja not in (' ', '.'):
            return False  # Pared u otra caja → no se puede

        # Mover la caja
        # ¿La caja llega a una meta?
        mapa[caja_f][caja_c] = '*' if celda_tras_caja == '.' else '$'

        # ¿La caja salía de una meta? → deja la meta libre
        mapa[nueva_f][nueva_c] = '.' if celda_destino == '*' else ' '

    # Caso 3: Destino es suelo libre o meta → solo mover jugador
    elif celda_destino not in (' ', '.'):
        return False  # Seguridad extra

    # Mover al jugador a su nueva posición
    mapa[nueva_f][nueva_c] = '@'

    # Restaurar la celda anterior del jugador
    # Si el jugador estaba sobre una meta, dejarla visible
    mapa[fila_j][col_j] = ' '  # El mapa original nunca pone @ sobre ., así que siempre es espacio

    return True


def verificar_victoria(matriz):
    """Retorna True si no quedan cajas sin ubicar (no hay '$' en el mapa)."""
    for fila in matriz:
        if '$' in fila:
            return False
    return True


def juego():
    """Bucle principal del juego (Game Loop)."""
    global mapa

    dibujar_mapa(mapa)

    while True:
        entrada = input("Tu movimiento: ").strip().lower()

        if entrada == 'q':
            print("\n¡Hasta luego! Gracias por jugar.")
            sys.exit(0)

        if entrada in ('w', 'a', 's', 'd'):
            mover(entrada)
            dibujar_mapa(mapa)

            if verificar_victoria(mapa):
                print("🎉 ¡FELICITACIONES! ¡Resolviste el nivel!")
                print("Todas las cajas están en su lugar.")
                break
        else:
            # Tecla inválida: redibujar sin crashear
            dibujar_mapa(mapa)
            print(f"Tecla '{entrada}' no válida. Usa W/A/S/D para moverte o Q para salir.")


if __name__ == "__main__":
    juego()