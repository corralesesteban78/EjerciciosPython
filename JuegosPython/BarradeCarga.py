import time

Mb  = float(input("Ingrese el tamaño del archivo (MB): "))
Sg = float(input("Ingrese el tiempo de carga (segundos): "))

print(f"\nIniciando subida de {Mb} MB...\n")

Carga = 20 
incremento = 100 / Carga
tiempo = Sg / Carga

for i in range(Carga + 1):
    porcentaje = int(i * incremento)
    
    llenos = int(porcentaje / 5)  
    vacios = 20 - llenos
    barra = "[" + "#" * llenos + "-" * vacios + "]"
    
    print(f"\r{barra} {porcentaje}%", end="")
    
    time.sleep(tiempo)

print(f"\n\n¡Archivo de {Mb} MB subido con éxito!")