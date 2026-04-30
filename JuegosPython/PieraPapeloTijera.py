import random, time
eleccion = ["piedra", "papel", "tijera"]

print ("-"*50)
print ("="*50)
print ("-"*13, "PIEDRA, PAPEL O TIJERA", "-"*13)
print ("="*50)
print ("-"*50)
time.sleep(3)
while True:
    user = input("Eliga piedra, papel o tijera. Si deseas terminar el juego escribe 'Salir':").lower().strip()

    if user == "salir":
        print ("-"*50)
        print ("Ha terminado el juego. Gracias por jugar :)")
        print ("-"*50)
        break
    if user not in eleccion:
        print ("I"*50)
        print ("Seleccionn no valida. Vuelva a intentar")
        print ("I"*50)
        continue
    pc = random.choice(eleccion)
    print(f"Tu eleccion {user}") 
    time.sleep(3)
    print(f"Eleccion del pc: {pc}")

    if user == pc:
     print ("-"*50)
     print ("Empate :0")
     print ("-"*50)
    elif (user == "piedra" and pc == "tijera") or \
         (user == "tijera" and pc == "papel") or \
         (user == "papel" and pc == "piedra"):
          print ("-"*50)
          print ("Haz ganado :)")
          print ("-"*50)
    else:
     print ("-"*50)
     print ("Haz perdido :(")
     print ("-"*50)
