print("Ejercicio 16: Adivina el número")
import random
numero_secreto = random.randint(1, 20)
intentos = 5
print("¡Bienvenido al juego de adivinar el número!")
for intento in range(1, intentos + 1):
    adivinanza = int(input(f"Intento {intento} de {intentos}. Ingresa un número entre 1 y 20: "))
    if adivinanza < numero_secreto:
        print("Demasiado bajo.")
    elif adivinanza > numero_secreto:
        print("Demasiado alto.")
    else:
        print(f"¡Felicidades! Adivinaste el número secreto {numero_secreto} en {intento} intentos.")
        break
else:
    print(f"Lo siento, no adivinaste el número secreto. Era {numero_secreto}.")
