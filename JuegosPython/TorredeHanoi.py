import os 

def limpiar_pantalla():
    #Limpiar consola patra la animacion
    os.system('cls' if os.name == 'nt' else 'clear')

def dibujar_torres(torres, n):
    #Dibuja el estado de las torres
    limpiar_pantalla()
    print("\n"+"==="*15)
    print("TORRE DE HANOI".center(45))
    print("==="*15+"\n")
#Ancho maximo que ocupara el disco
    ancho_columna = n *2 + 3
    #Dinujsr desde arriba hacia abajo
    for i in range(n - 1, -1,-1):
        fila = ""
        for poste in ['A','B','C']:
            if i < len(torres[poste]):
                tamano_disco = torres[poste][i]
                #crear dibujo del disco[===]
                disco_str ="[" + "=" * ((tamano_disco * 2) -1)+"]"
                #centrar e disco
                fila += disco_str.center(ancho_columna)
            else:
                #si no hay disco, dibujar espacio vacio
                fila += "|".center(ancho_columna)
        print(fila)
#Dibujar la base base
    print("-" * (ancho_columna * 3))
    print("A",center(ancho_columna) + "B",center(ancho_columna) + "C",center(ancho_columna))
    print("\n"+"==="*15)

def jugar_hanoi(n=3):
    #Funcion principal
    #Iniciar
    torres = {'A': list(range( n , 0 , -1)), 'B': [], 'C': []}
    movimientos = 0

    while len(torres['B']) < n:
        dibujar_torres(torres, n)
        print(f"Movimiento: {movimientos}\n")
        print("Instrucciones: Ingrese el poste de origen y el destino separadop por un espacio")
        print("Ejemplo: A C para mover el disco superior a A hacia B")
        print("Escribe Q para salir")

        entrada = input("Ingrese su movimiento: ").strip().upper()

        if entrada == 'Q':
            print("Gracias por jugar a la Torre de Hanoi. Hasta luego")
            return
        partes = entrada.split()
        if len(partes) != 2 or partes[0] not it torres or partes[1] not in torres:
          print("Entrada invalida. Por favor, asegurate de usar las letras A, B o C")
          input("Presione Enter para continuar...")
          continue
 

if __name__ == "__main__":
    #jugar_hanoi()uncion que inicia el juego
    dibujar_torres()