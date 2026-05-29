import math

def imprimir_menu():
    print("\n" + "="*30)
    print("   MENÚ DE FIGURAS GEOMÉTRICAS")
    print("="*30)
    print("1. Triángulo")
    print("2. Cuadrado")
    print("3. Rectángulo")
    print("4. Círculo")
    print("5. Pentágono")
    print("6. Salir")
    print("="*30)

def dibujar_figuras():
    while True:
        imprimir_menu()
        opcion = input("Elija una opción (1-6): ")

        if opcion == "6":
            print("¡Gracias por usar el generador! Saliendo...")
            break

        if opcion in ["1", "2", "3", "4", "5"]:
            try:
                n = int(input("Ingrese el tamaño (base/radio/lado): "))
            except ValueError:
                print("Error: Ingrese un número entero válido.")
                continue

            print("\nResultado:\n")

            # 1. TRIÁNGULO
            if opcion == "1":
                for i in range(1, n + 1):
                    print("* " * i)

            # 2. CUADRADO
            elif opcion == "2":
                for i in range(n):
                    print("* " * n)

            # 3. RECTÁNGULO
            elif opcion == "3":
                for i in range(n):
                    print("* " * (n * 2))

            # 4. CÍRCULO (Lógica de radio y distancia)
            elif opcion == "4":
                radio = n
                for i in range((2 * radio) + 1):
                    for j in range((2 * radio) + 1):
                        # Ecuación del círculo: x^2 + y^2 = r^2
                        distancia = math.sqrt((i - radio)**2 + (j - radio)**2)
                        if distancia < radio + 0.5:
                            print("*", end=" ")
                        else:
                            print(" ", end=" ")
                    print()

            # 5. PENTÁGONO (Combinación de Triángulo y Rectángulo)
            elif opcion == "5":
                # Parte superior (Punta)
                for i in range(1, n, 2):
                    espacios = (n - i) // 1
                    print("  " * espacios + "* " * i)
                # Parte inferior (Base)
                for i in range(n // 2):
                    print("* " * n)
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    dibujar_figuras()