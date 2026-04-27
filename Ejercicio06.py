edad = int(input("Escribe tu edad: "))

if edad >= 0 and edad <= 12:
 print("Eres un niño")
elif edad >= 13 and edad <= 17:
 print("Eres un Adolecente")
elif edad >= 18 and edad <= 64:
 print("Eres un adulto")
elif edad < 0:
 print("Edad no valida")
else:
 print ("Eres un adulto mayor")

