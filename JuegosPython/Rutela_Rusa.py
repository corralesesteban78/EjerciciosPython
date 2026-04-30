import random, time 
print("="*50)
print("Bienvenido al Simluador de Ruleta Rusa")
print("="*50)

input("Poner la bala en el Tambor (Presiona Enter)")
bala = random.randint(1,6)
time.sleep(0.5)

disparos = 0 
while True:
  input("Girar el tambor(Presiona Enter)")
  recamara = random.randint(1,6)
  input("Apuntar y disparar (Presione Enter)")
  time.sleep(1)

  if recamara == bala:
   print ("PUM, Has perdidp, la bala estaba en la recamara")
   break
  else:
   disparos += 1
   print ("Has sobrevivido a este intendo")
   print("Intentos de disparos ",disparos)

   if disparos == 5:
    print("Felicidades,haz ganado al sobrevidir a 5 intentos")
    break

print("="*50)
print("Fin del jeugo, Gracias por jugar")
print("="*50)
