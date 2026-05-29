import os
import sys
#🧱📍

MAPA_INICIAL = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', '$', ' ', ' ', '#'],
    ['#', ' ', '.', '@', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#'],
]

mapa = [fila[:] for fila in MAPA_INICIAL]


def dibujar_mapa(matriz):
    """Limpia la terminal y dibuja el mapa actual con las instrucciones."""
   
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
    return None, None

def mover(direccion):
    """
    Contiene toda la lógica de validación de colisiones y movimiento.
    Retorna True si el movimiento fue válido, False si no.
    """
    
    deltas = {
        'w': (-1, 0),
        's': (1, 0),
        'a': (0, -1),
        'd': (0, 1),
    }

    if direccion not in deltas:
        return False  

    df, dc = deltas[direccion]
    fila_j, col_j = obtener_posicion_jugador(mapa)

    if fila_j is None:
        return False  

    nueva_f = fila_j + df
    nueva_c = col_j + dc

  
    if nueva_f < 0 or nueva_f >= len(mapa) or nueva_c < 0 or nueva_c >= len(mapa[0]):
        return False  

    celda_destino = mapa[nueva_f][nueva_c]

    if celda_destino == '#':
        return False

    
    if celda_destino in ('$', '*'):
       
        caja_f = nueva_f + df
        caja_c = nueva_c + dc


        if caja_f < 0 or caja_f >= len(mapa) or caja_c < 0 or caja_c >= len(mapa[0]):
            return False  

        celda_tras_caja = mapa[caja_f][caja_c]

        if celda_tras_caja not in (' ', '.'):
            return False  

        
        mapa[caja_f][caja_c] = '*' if celda_tras_caja == '.' else '$'

   
        mapa[nueva_f][nueva_c] = '.' if celda_destino == '*' else ' '

  
    elif celda_destino not in (' ', '.'):
        return False  

    mapa[nueva_f][nueva_c] = '@'

  
    mapa[fila_j][col_j] = ' ' 

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
         
            dibujar_mapa(mapa)
            print(f"Tecla '{entrada}' no válida. Usa W/A/S/D para moverte o Q para salir.")


if __name__ == "__main__":
    juego()